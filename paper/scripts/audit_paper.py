#!/usr/bin/env python3
"""Check editorial consistency and frozen artifact bindings, not mathematics."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

PAPER = Path(__file__).resolve().parents[1]
ROOT = PAPER.parent
BASE = "0d6b855fd6d9d9e5ddb5dbd186a2a590164c1341"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    issues = []
    checked_bindings = {}

    def check(condition, message):
        if not condition:
            issues.append(message)

    def verify_binding(b):
        path = ROOT / b["path"]
        good = path.is_file() and sha(path.read_bytes()) == b["sha256"]
        if "bytes" in b and path.exists():
            good = good and path.stat().st_size == b["bytes"]
        check(good, "Changed or missing binding: " + b["path"])
        checked_bindings[b["path"]] = good

    inputs = []

    def visit(name):
        path = PAPER / name
        check(path.is_file(), "Missing TeX input: " + name)
        if not path.is_file():
            return
        check(name not in inputs, "Duplicate/cyclic TeX input: " + name)
        if name in inputs:
            return
        inputs.append(name)
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", path.read_text()):
            visit(target if target.endswith(".tex") else target + ".tex")

    visit("main.tex")
    expected = {"main.tex", "preamble.tex"}
    for directory in ("sections", "appendices"):
        expected.update(p.relative_to(PAPER).as_posix() for p in (PAPER / directory).glob("*.tex"))
    check(set(inputs) == expected, "Unincluded TeX source")
    text = "\n".join((PAPER / p).read_text() for p in inputs)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    check(all(n == 1 for n in Counter(labels).values()), "Duplicate label")
    for label in re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text):
        check(label in labels, "Missing reference label: " + label)
    bibliography = (PAPER / "references.bib").read_text()
    keys = re.findall(r"@\w+\{([^,]+),", bibliography)
    check(all(n == 1 for n in Counter(keys).values()), "Duplicate bibliography key")
    cited = set()
    for group in re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", text):
        for key in group.split(","):
            cited.add(key)
            check(key in keys, "Missing citation: " + key)
    check(not re.search(r"(?<![\\a-zA-Z])q?quad(?=[^a-zA-Z]|$)", text),
          "Unescaped math spacing command")
    check(not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text), "Control character in TeX")

    entries = json.loads((PAPER / "data/entry-map.json").read_text())
    ledger = json.loads((ROOT / "reports/result-scope-ledger.json").read_text())
    scopes = json.loads((ROOT / "research/result-scopes.json").read_text())
    by_id = {e["id"]: e for e in scopes["entries"]}
    ids = [e["id"] for e in entries["entries"]]
    check(len(ids) == 12 and len(set(ids)) == 12 and set(ids) == set(by_id), "Entry coverage mismatch")
    check(entries["counts"] == ledger["counts"], "Deadline counts changed")
    check(entries["handoff_commit"] == BASE, "Wrong handoff commit")
    for entry in entries["entries"]:
        ident = entry["id"]
        check(entry["frozen_scope"] == by_id[ident], "Scope differs: " + ident)
        section = (PAPER / entry["section_file"]).read_text()
        check("\\entry{" + ident + "}" in section, "Missing statement: " + ident)
        check("\\label{" + entry["section_label"] + "}" in section, "Missing section: " + ident)
        check(sha((ROOT / "problems" / ident / "source-fragment.html").read_bytes()) ==
              entry["statement_fragment_sha256"], "Source fragment changed: " + ident)
        for b in [entry["source"], entry["rendered_statement"],
                  *entry["proof_bindings"], *entry["audit_bindings"]]:
            verify_binding(b)
    for b in ledger["input_and_artifact_bindings"]:
        verify_binding(b)
    session = json.loads((ROOT / "state/session.json").read_text())
    for path, digest in session["input_sha256"].items():
        verify_binding({"path": path, "sha256": digest})

    targets = {p for p in re.findall(r"\\record\{([^}]+)\}", text) if "#" not in p}
    targets.update("problems/" + ident + "/" + path for ident, path in
                   re.findall(r"\\evidence\{([^}]+)\}\{([^}]+)\}", text))
    for target in targets:
        found = subprocess.run(["git", "cat-file", "-e", BASE + ":" + target],
                               cwd=ROOT, capture_output=True).returncode == 0
        check(found, "Pinned artifact target missing: " + target)

    # A tracked working-tree comparison against the handoff includes staged edits.
    changed = git("diff", "--name-only", BASE, "--").decode().splitlines()
    check(all(p == "README.md" or p.startswith("paper/") for p in changed),
          "Research or state changed outside the paper and landing README")
    check(git("show", BASE + ":README.md") == (PAPER / "data/README-at-handoff.md").read_bytes(),
          "Archived README differs from handoff")
    markdown_targets = set()
    for document in (ROOT / "README.md", PAPER / "README.md"):
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if "://" not in target and not target.startswith(("#", "mailto:")):
                path = document.parent / target.split("#")[0]
                markdown_targets.add(str(path.relative_to(ROOT)))
                check(path.exists(), "Broken README target: " + str(path))

    pdf = PAPER / "gworld-experiment.pdf"
    extracted = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
    for ident in ids:
        check("Problem " + ident + "." in extracted, "PDF lacks statement: " + ident)
    for phrase in ("Vladimir Shpilrain", "shpilrain@yahoo.com", "101200949",
                   "2.676891785", "2.943737759", "ten entries", "two others"):
        check(phrase in extracted, "PDF lacks expected text: " + phrase)
    check("101200949" in extracted.split("\f")[0], "Funding not on first page")
    check("research visit" in extracted.split("\f")[0], "Visit footnote not on first page")
    check("??" not in extracted, "Unresolved reference in PDF")
    log = (PAPER / "data/build-log.txt").read_text()
    for pattern in (r"Overfull ", r"undefined", r"Missing character", r"multiply defined"):
        check(not re.search(pattern, log), "TeX log issue: " + pattern)
    build = json.loads((PAPER / "data/build-manifest.json").read_text())
    for b in build["inputs"] + build["outputs"]:
        check(sha((PAPER / b["path"]).read_bytes()) == b["sha256"],
              "Build source/output changed: " + b["path"])
    for filename in ("pdf-checks.json", "visual-review.json"):
        record = json.loads((PAPER / "data" / filename).read_text())
        check(record["pdf_sha256"] == sha(pdf.read_bytes()), "Stale PDF record: " + filename)
    package = json.loads((PAPER / "data/source-archive-manifest.json").read_text())
    check(package["passed"] and package["published_pdf_sha256"] == sha(pdf.read_bytes()),
          "Stale or failed source-archive check")
    check(sha((PAPER / package["archive"]["path"]).read_bytes()) == package["archive"]["sha256"],
          "Source archive hash mismatch")
    for path in [ROOT / "README.md", *PAPER.rglob("*")]:
        if path.is_file() and "build" not in path.relative_to(ROOT).parts:
            check(path.stat().st_size < 90000000, "Oversized file: " + str(path))
    result = {"checked_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Editorial consistency and artifact preservation; not mathematical verification.",
              "handoff_commit": BASE, "pdf_sha256": sha(pdf.read_bytes()),
              "tex_inputs": inputs, "entry_ids": ids, "counts": entries["counts"],
              "citation_keys": sorted(cited), "pinned_artifact_targets": sorted(targets),
              "readme_local_targets": sorted(markdown_targets),
              "checked_binding_paths": sorted(checked_bindings),
              "frozen_ledger_bindings": len(ledger["input_and_artifact_bindings"]),
              "changed_tracked_paths": changed, "issues": issues, "passed": not issues}
    (PAPER / "data/editorial-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"passed": not issues, "entries": len(ids), "bindings": len(checked_bindings),
                      "pinned_targets": len(targets), "issues": issues}, indent=2))
    return bool(issues)


if __name__ == "__main__":
    sys.exit(main())
