from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required_files = [
    "README.md",
    "LICENSE",
    "docs/architecture.md",
    "docs/detection-coverage.md",
    "docs/mitre-attack-mapping.md",
    "docs/validation-results.md",
    "evidence/README.md",
    "tests/DET-003-privileged-role-assignment-test.kql",
    "tests/DET-004-sliding-window-test.kql",
    "tests/DET-007-positive-test.kql",
    "tests/DET-007-rolling-window-test.kql",
    "tests/DET-008-nsg-operations-test.kql",
    "tests/DET-009-policy-assignment-operations-test.kql",
    "tests/DET-010-key-vault-operations-test.kql",
]

for item in required_files:
    if not (ROOT / item).is_file():
        errors.append(f"Missing required file: {item}")

for number in range(3, 11):
    matches = list((ROOT / "rules").glob(f"DET-{number:03d}-*.kql"))
    if len(matches) != 1:
        errors.append(
            f"Expected one DET-{number:03d} rule; found {len(matches)}"
        )

for folder in ("rules", "queries", "tests"):
    for path in (ROOT / folder).glob("*.kql"):
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"Empty KQL file: {path.relative_to(ROOT)}")
        if any(line.rstrip() != line for line in content.splitlines()):
            errors.append(f"Trailing whitespace: {path.relative_to(ROOT)}")

evidence_readme = ROOT / "evidence/README.md"
if evidence_readme.is_file():
    content = evidence_readme.read_text(encoding="utf-8")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
        if target.startswith(("http://", "https://", "#")):
            continue
        if not (evidence_readme.parent / target).is_file():
            errors.append(f"Broken evidence reference: {target}")

if errors:
    print("Repository validation FAILED:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("Repository validation PASSED.")
print("Eight detection rules checked.")
print("Required tests and documentation checked.")
print("Evidence references checked.")
print("KQL static checks passed.")
print("KQL runtime execution is not performed by this validator.")
