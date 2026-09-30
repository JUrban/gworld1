#!/usr/bin/env python3
"""Validate scope bookkeeping and build interim reports; not a proof checker."""

import csv
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text())


def binding(path):
    p = ROOT / path
    if p.resolve().is_relative_to(ROOT) is False or not p.is_file():
        raise ValueError(f"Not an available repository file: {path}")
    content = p.read_bytes()
    return {"path": path, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def links(paths):
    return ", ".join(f"[{p.rsplit('/', 1)[-1]}](../{p})" for p in paths)


def main():
    scope = read_json("research/result-scopes.json")
    source = read_json("data/problems.json")
    session = read_json("state/session.json")
    with (ROOT / "research/triage.csv").open(newline="") as f:
        triage = list(csv.DictReader(f))
    catalog = {p["id"]: p for p in source}
    by_triage = {p["id"]: p for p in triage}
    entries = {p["id"]: p for p in scope["entries"]}
    require(len(catalog) == len(source), "Repeated catalogue ID")
    require(len(by_triage) == len(triage), "Repeated triage ID")
    require(catalog.keys() == by_triage.keys(), "Catalogue/triage ID mismatch")
    require(len(entries) == len(scope["entries"]), "Repeated candidate ID")
    require(entries.keys() <= catalog.keys(), "Unknown candidate ID")
    candidate_statuses = {p["id"] for p in triage if "candidate" in p["status"]}
    require(candidate_statuses == entries.keys(), "Scope ledger disagrees with current candidate triage")
    assessed = datetime.fromisoformat(scope["assessed_utc"])
    require(datetime.fromisoformat(session["started_utc"]) <= assessed <=
            datetime.fromisoformat(session["deadline_utc"]), "Assessment outside research window")
    for path, sha in session["input_sha256"].items():
        require(binding(path)["sha256"] == sha, f"Frozen launch input changed: {path}")

    all_paths = {"research/result-scopes.json", "research/triage.csv", "data/problems.json",
                 "scripts/build_scope_ledger.py"}
    counts = Counter(catalogue_entries=len(catalog), established_novel_results=0)
    for p in scope["entries"]:
        pid = p["id"]
        components = p["components"]
        parts = [c["part"] for c in components]
        require(len(parts) == len(set(parts)), f"Repeated component: {pid}")
        require(set(parts) == set(catalog[pid]["parts_detected"] or ["entry"]),
                f"Incomplete or invented named-part accounting: {pid}")
        bases = {c["basis"] for c in components}
        if p["coverage"] == "whole_entry_candidate":
            require(bases <= {"candidate", "prior"} and "candidate" in bases,
                    f"Invalid whole-entry basis: {pid}")
            require("partial" not in by_triage[pid]["status"], f"Whole/partial mismatch: {pid}")
            counts["whole_entry_coverage_candidates"] += 1
            counts["whole_entries_with_named_parts" if catalog[pid]["parts_detected"]
                   else "unpartitioned_whole_entry_candidates"] += 1
        elif p["coverage"] == "partial_entry_candidate":
            require(bases == {"partial_candidate"}, f"Invalid partial-entry basis: {pid}")
            require(by_triage[pid]["status"] == "partial_candidate", f"Partial/whole mismatch: {pid}")
            counts["partial_entry_candidates"] += 1
        else:
            raise ValueError(f"Unrecognized coverage: {pid}")
        for c in components:
            if c["basis"] == "candidate":
                counts["complete_proposed_components"] += 1
            if c["part"] != "entry":
                counts["named_subpart_candidates" if c["basis"] == "candidate" else
                       "credited_prior_named_subparts" if c["basis"] == "prior" else
                       "partial_named_subparts"] += 1
        all_paths.update(p["proofs"] + p["audits"])
    excluded_ids = []
    for p in scope["selected_uncounted_work"]:
        require(p["id"] in catalog and p["id"] not in entries, f"Invalid exclusion: {p['id']}")
        excluded_ids.append(p["id"])
        all_paths.update(p["artifacts"])
    require(len(set(excluded_ids)) == len(excluded_ids), "Repeated selected uncounted ID")
    counts["uncounted_catalogue_entries"] = len(catalog) - len(entries)

    rows = []
    for p in source:
        pid = p["id"]
        statement = {key: p[key] for key in ("source_url", "source_path", "source_sha256",
                     "start_line", "start_byte", "end_byte", "fragment_sha256", "parts_detected")}
        rows.append({"id": pid, "category": p["category"], "statement_source": statement,
                     "triage": by_triage[pid],
                     "counted_coverage": entries[pid]["coverage"] if pid in entries else "uncounted",
                     "candidate_scope": entries.get(pid)})
    bindings = [binding(path) for path in sorted(all_paths)]
    ledger = {"schema_version": 1, "assessed_utc": scope["assessed_utc"], "phase": scope["phase"],
              "deadline_utc": session["deadline_utc"], "counts": dict(counts),
              "review_status": scope["review_status"], "novelty_status": scope["novelty_status"],
              "cautions": ["Whole-entry coverage combines proposed arguments with credited prior answers.",
                           "Complete proposed components are bookkeeping units, not established new theorems.",
                           "Uncounted entries include prior answers and unchecked status; they are not all open.",
                           "This script checks bookkeeping and file availability, not proof correctness or novelty.",
                           "This is an interim snapshot, not the deadline-frozen result."],
              "input_and_artifact_bindings": bindings,
              "selected_uncounted_work": scope["selected_uncounted_work"], "entries": rows}
    out = ROOT / "reports/result-scope-ledger.json"
    out.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")

    lines = ["# Interim result scope ledger", "",
             f"Assessment: **{scope['assessed_utc']}**. Research remains active until",
             f"**{session['deadline_utc']}**. This is not the frozen deadline result.", "",
             f"**{counts['whole_entry_coverage_candidates']} whole-entry coverage candidates, "
             f"{counts['partial_entry_candidates']} partial-entry candidates, "
             f"{counts['established_novel_results']} established novel results.**",
             "Whole-entry coverage combines the proposed arguments with explicitly credited",
             "prior answers. All candidate proofs and novelty assessments await independent",
             "specialist review. Separate implementations and formal fragments have the",
             "limited scopes described in the individual audits.", "",
             "## Entry and named-part accounting", "",
             "| Bookkeeping unit | Count |", "| --- | ---: |"]
    for key, title in [("unpartitioned_whole_entry_candidates", "Unpartitioned whole-entry candidates"),
                       ("whole_entries_with_named_parts", "Whole-entry candidates having named parts"),
                       ("named_subpart_candidates", "Complete proposed answers to named parts"),
                       ("credited_prior_named_subparts", "Credited prior named parts within those entries"),
                       ("partial_entry_candidates", "Other partial-entry candidates"),
                       ("uncounted_catalogue_entries", "Other catalogue entries, not counted here")]:
        lines.append(f"| {title} | {counts[key]} |")
    lines += ["", "The six unpartitioned answers and five proposed named-part answers make",
              "eleven proposed components across ten whole-entry candidates. Neither count",
              "is a count of established new theorems. Rank-restricted prior results inside",
              "a component are credited below and are not additional named parts.", "",
              "The other 183 catalogue entries are **not** asserted to be open. They include",
              "prior answers, partial results, failed approaches and unverified status.", "",
              "| Entry | Component basis | Current proposed result |", "| --- | --- | --- |"]
    for p in scope["entries"]:
        basis = "; ".join(f"{c['part']}: {c['basis'].replace('_', ' ')}" for c in p["components"])
        lines.append(f"| [{p['id']}](../problems/{p['id']}/README.md) | {basis} | {p['result']} |")
    lines += ["", "## Prior coverage, limits and controlling files", ""]
    for p in scope["entries"]:
        lines += [f"### {p['id']}", "", p["prior_scope"], "", p["limits"], "",
                  f"Proofs: {links(p['proofs'])}.", "", f"Audits: {links(p['audits'])}.", ""]
    lines += ["## Selected uncounted work", "",
              "This selection explains significant exclusions; it is not a complete list",
              "of prior answers or unsuccessful work.", "",
              "| Entry | Why it is not counted | Evidence |", "| --- | --- | --- |"]
    for p in scope["selected_uncounted_work"]:
        lines.append(f"| {p['id']} | {p['reason']} | {links(p['artifacts'])} |")
    lines += ["", "## Reproduction and complete inventory", "",
              "The [JSON ledger](result-scope-ledger.json) records all catalogue IDs, their",
              "current triage rows, original source locations and hashes, and the precise",
              "candidate components. Its artifact bindings identify this assessment's files.", "",
              "Regenerate after an explicit scope update with:", "", "```sh",
              "python3 scripts/run_recorded.py --name scope-ledger-NEW --cores 1 --memory-gb 2 \\",
              "  --timeout 60 --expect 'PASS result scope ledger' -- python3 scripts/build_scope_ledger.py",
              "```", "", "The script validates ID/part/count consistency, frozen launch-input hashes,",
              "and linked-file availability. It does not establish the correctness of a",
              "proof, a literature assessment, or a novelty claim. Historical claims remain",
              "in the append-only ledger and dated notes. The final report must distinguish",
              "the actual deadline snapshot from any later corrections.", ""]
    (ROOT / "reports/RESULT_SCOPE.md").write_text("\n".join(lines))
    print("PASS result scope ledger", json.dumps(dict(counts), sort_keys=True))
    print(f"Bound {len(bindings)} input/artifact files; retained all {len(rows)} catalogue IDs.")


if __name__ == "__main__":
    main()
