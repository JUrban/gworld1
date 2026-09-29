#!/usr/bin/env python3
"""F20 inputs with redundant universal commutator and conjugation identities.

Every added identity is independently parsed and freely reduced by GAP before
prover use. These are identities of arbitrary groups, not nilpotency axioms.
"""
import argparse
import hashlib
import json
from pathlib import Path

from generate_f20_equational import AXIOMS, make_hall


IDENTITIES = [
    ("comm_def", "cc(X,Y)=mul(mul(inv(X),inv(Y)),mul(X,Y))"),
    ("conj_def", "cj(X,Y)=mul(inv(Y),mul(X,Y))"),
    ("comm_swap", "cc(Y,X)=inv(cc(X,Y))"),
    ("comm_self", "cc(X,X)=one"),
    ("comm_one_l", "cc(one,X)=one"),
    ("comm_one_r", "cc(X,one)=one"),
    ("comm_inv_self", "cc(X,inv(X))=one"),
    ("conj_one_l", "cj(one,X)=one"),
    ("conj_one_r", "cj(X,one)=X"),
    ("conj_self", "cj(X,X)=X"),
    ("conj_product", "cj(X,mul(Y,Z))=cj(cj(X,Y),Z)"),
    ("product_conj", "cj(mul(X,Y),Z)=mul(cj(X,Z),cj(Y,Z))"),
    ("conj_inverse", "cj(inv(X),Y)=inv(cj(X,Y))"),
    ("conj_comm", "cj(X,Y)=mul(X,cc(X,Y))"),
    ("comm_product_l", "cc(mul(X,Y),Z)=mul(cj(cc(X,Z),Y),cc(Y,Z))"),
    ("comm_product_r", "cc(X,mul(Y,Z))=mul(cc(X,Z),cj(cc(X,Y),Z))"),
    ("comm_inverse_l", "cc(inv(X),Y)=cj(inv(cc(X,Y)),inv(X))"),
    ("comm_inverse_r", "cc(X,inv(Y))=cj(inv(cc(X,Y)),inv(Y))"),
    ("comm_conj", "cj(cc(X,Y),Z)=cc(cj(X,Z),cj(Y,Z))"),
    ("collection", "mul(X,Y)=mul(mul(Y,X),cc(X,Y))"),
    ("hall_witt", "mul(mul(cj(cc(cc(X,inv(Y)),Z),Y),cj(cc(cc(Y,inv(Z)),X),Z)),cj(cc(cc(Z,inv(X)),Y),X))=one"),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("output", type=Path)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    records = []
    for weight in (5, 6):
        hall = make_hall(weight + 1)

        def term(i):
            if hall[i]["weight"] < weight:
                return f"c{i + 1:03d}"
            a, b = hall[i]["parents"]
            return f"cc({term(a)},{term(b)})"

        formulas = [f"cnf({name},axiom,({eq}))." for name, eq in AXIOMS + IDENTITIES]
        for i, h in enumerate(hall):
            if not 1 < h["weight"] <= weight:
                continue
            a, b = map(term, h["parents"])
            if h["weight"] == weight:
                name, eq = f"rel_{i + 1:03d}", f"cc({a},{b})=one"
            else:
                name, eq = f"def_{i + 1:03d}", f"{term(i)}=cc({a},{b})"
            formulas.append(f"cnf({name},axiom,({eq})).")
        targets = [i for i, h in enumerate(hall) if h["weight"] == weight + 1]
        negative = next(i for i, h in enumerate(hall) if h["weight"] == weight - 1)
        for number, i in enumerate(targets + [negative], 1):
            kind = "target" if i in targets else "negative-control"
            filename = f"w{weight}-comm-{kind}-{number:02d}.p"
            content = "\n".join([
                "% F20 rank two; only Hall commutators of exactly the specified weight are killed.",
                "% cc(X,Y)=X^-1 Y^-1 X Y; cj(X,Y)=Y^-1 X Y.",
                "% Added identities hold in arbitrary groups. No nilpotency axiom.",
                *formulas, f"cnf(goal,negated_conjecture,({term(i)}!=one)).", "",
            ])
            (args.output / filename).write_text(content)
            records.append({"file": filename, "weight": weight, "encoding": "comm",
                            "kind": kind, "target_number": number, "hall_index": i + 1,
                            "parents": [x + 1 for x in hall[i]["parents"]], "word": hall[i]["word"],
                            "sha256": hashlib.sha256(content.encode()).hexdigest()})
    (args.output / "inputs.json").write_text(json.dumps(records, indent=2) + "\n")
    (args.output / "identities.json").write_text(json.dumps(AXIOMS + IDENTITIES, indent=2) + "\n")
    print(f"PASS F20 commutator inputs: {len(records)} files, {len(IDENTITIES)} added identities")


if __name__ == "__main__":
    main()
