#!/usr/bin/env python3
"""Ground presentation consequences for F20; no nilpotency axiom is used.

The collection presentation names each Hall commutator of weight < c and
uses uv=vu[u,v].  Only commutators of exactly weight c are killed.
"""
import argparse
import hashlib
import json
from pathlib import Path


def inverse(word):
    return [-x for x in reversed(word)]


def reduce_word(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def make_hall(bound):
    hall = [{"weight": 1, "parents": None, "word": [1]},
            {"weight": 1, "parents": None, "word": [2]}]
    for weight in range(2, bound + 1):
        old = len(hall)
        for i in range(old):
            for j in range(i):
                u, v = hall[i], hall[j]
                if u["weight"] + v["weight"] != weight:
                    continue
                if u["parents"] and u["parents"][1] > j:
                    continue
                w = reduce_word(inverse(u["word"]) + inverse(v["word"]) + u["word"] + v["word"])
                hall.append({"weight": weight, "parents": [i, j], "word": w})
    assert [sum(h["weight"] == w for h in hall) for w in range(1, bound + 1)] == [2, 1, 2, 3, 6, 9, 18][:bound]
    return hall


AXIOMS = [
    ("assoc", "mul(mul(X,Y),Z)=mul(X,mul(Y,Z))"),
    ("left_id", "mul(one,X)=X"),
    ("right_id", "mul(X,one)=X"),
    ("left_inv", "mul(inv(X),X)=one"),
    ("right_inv", "mul(X,inv(X))=one"),
    ("inv_inv", "inv(inv(X))=X"),
    ("inv_prod", "inv(mul(X,Y))=mul(inv(Y),inv(X))"),
    ("inv_one", "inv(one)=one"),
]


def mul(a, b):
    return f"mul({a},{b})"


def comm(a, b):
    return mul(mul(f"inv({a})", f"inv({b})"), mul(a, b))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("output", type=Path)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    records = []
    for weight in (5, 6):
        hall = make_hall(weight + 1)
        for encoding in ("collect", "inverse"):
            def term(i):
                if hall[i]["weight"] < weight:
                    return f"c{i + 1:03d}"
                a, b = hall[i]["parents"]
                return comm(term(a), term(b))

            formulas = [f"cnf({name},axiom,({equation}))." for name, equation in AXIOMS]
            for i, h in enumerate(hall):
                if h["weight"] == 1 or h["weight"] > weight:
                    continue
                a, b = map(term, h["parents"])
                if h["weight"] == weight:
                    eq = f"{mul(a,b)}={mul(b,a)}" if encoding == "collect" else f"{comm(a,b)}=one"
                    name = f"rel_{i + 1:03d}"
                else:
                    eq = f"{mul(a,b)}={mul(mul(b,a),term(i))}" if encoding == "collect" else f"{term(i)}={comm(a,b)}"
                    name = f"def_{i + 1:03d}"
                formulas.append(f"cnf({name},axiom,({eq})).")
            targets = [i for i, h in enumerate(hall) if h["weight"] == weight + 1]
            # A lower-weight Hall word is nontrivial in the known class-(c-1)
            # nilpotent quotient, hence supplies a negative encoding control.
            negative = next(i for i, h in enumerate(hall) if h["weight"] == weight - 1)
            for number, i in enumerate(targets + [negative], 1):
                h = hall[i]
                a, b = map(term, h["parents"])
                eq = f"{mul(a,b)}!={mul(b,a)}" if encoding == "collect" else f"{term(i)}!=one"
                kind = "target" if i in targets else "negative-control"
                filename = f"w{weight}-{encoding}-{kind}-{number:02d}.p"
                content = "\n".join([
                    "% F20, rank two; [u,v]=u^-1 v^-1 u v.",
                    "% Constants cNNN name Hall commutators; they are not variables.",
                    "% No relation of weight greater than the requested weight is assumed.",
                    *formulas, f"cnf(goal,negated_conjecture,({eq})).", "",
                ])
                (args.output / filename).write_text(content)
                records.append({"file": filename, "weight": weight, "encoding": encoding,
                                "kind": kind, "target_number": number, "hall_index": i + 1,
                                "parents": [x + 1 for x in h["parents"]],
                                "word": h["word"],
                                "sha256": hashlib.sha256(content.encode()).hexdigest()})
        (args.output / f"hall-w{weight}.json").write_text(json.dumps(hall, indent=2) + "\n")
    (args.output / "inputs.json").write_text(json.dumps(records, indent=2) + "\n")
    print(f"PASS F20 ground encoding generation: {len(records)} files")
    for r in records:
        if r["weight"] == 6 and r["encoding"] == "collect":
            print(r["file"], r["hall_index"], r["parents"])


if __name__ == "__main__":
    main()
