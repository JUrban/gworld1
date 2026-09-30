import Mathlib.Algebra.FreeAlgebra
import Mathlib.LinearAlgebra.Finsupp.LSum
import Mathlib.Data.List.OfFn
import Mathlib.Data.Finsupp.Fin
import Mathlib.Algebra.MvPolynomial.Rename
import Lean.Util.CollectAxioms

/- The homogeneous word component of a free associative algebra and its
   positional polynomial dictionary. Earlier polynomial/analytic components
   are included unchanged by the checker. No free-Lie/group theorem here. -/
noncomputable section
namespace N8Words

open scoped BigOperators
open MvPolynomial

abbrev Words (m : ℕ) := (Fin m → ℕ) →₀ ℚ
abbrev Assoc := MonoidAlgebra ℚ (FreeMonoid ℕ)

def exponents {m : ℕ} (v : Fin m → ℕ) : Fin m →₀ ℕ :=
  Finsupp.equivFunOnFinite.symm v

def encode (m : ℕ) : Words m ≃ₗ[ℚ] MvPolynomial (Fin m) ℚ :=
  Finsupp.mapDomain.linearEquiv ℚ ℚ Finsupp.equivFunOnFinite.symm

def word {m : ℕ} (v : Fin m → ℕ) : FreeMonoid ℕ :=
  FreeMonoid.ofList (List.ofFn v)

def realize (m : ℕ) : Words m →ₗ[ℚ] Assoc :=
  Finsupp.lmapDomain ℚ ℚ word

def E (j : ℕ) : Assoc := Finsupp.single (FreeMonoid.of j) 1

def prepend {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  Finsupp.lmapDomain ℚ ℚ (Fin.cons j)

def append {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  Finsupp.lmapDomain ℚ ℚ (fun v => Fin.snoc v j)

def bracket {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  prepend j - append j

def increment {m : ℕ} (i : Fin m) (v : Fin m → ℕ) : Fin m → ℕ :=
  fun k => v k + if k = i then 1 else 0

def deriv (m : ℕ) : Words m →ₗ[ℚ] Words m :=
  ∑ i : Fin m, Finsupp.lmapDomain ℚ ℚ (increment i)

@[simp] theorem encode_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    encode m (Finsupp.single v c) = monomial (exponents v) c := by
  simp only [encode, Finsupp.mapDomain.coe_linearEquiv, Finsupp.mapDomain_single]
  rfl

@[simp] theorem realize_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    realize m (Finsupp.single v c) = Finsupp.single (word v) c := by
  simp [realize]

theorem realize_injective (m : ℕ) : Function.Injective (realize m) := by
  apply Finsupp.mapDomain_injective
  intro v w h
  exact List.ofFn_injective (FreeMonoid.ofList.injective h)

theorem exponents_increment {m : ℕ} (i : Fin m) (v : Fin m → ℕ) :
    exponents (increment i v) = Finsupp.single i 1 + exponents v := by
  classical
  ext k
  by_cases h : k = i <;> simp [exponents, increment, Finsupp.single_apply, h, eq_comm, add_comm]

theorem exponents_cons {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.cons j v) =
      Finsupp.single 0 j + (exponents v).mapDomain Fin.succ := by
  classical
  ext k
  refine Fin.cases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply Fin.succ_injective]
    simp [exponents, Finsupp.single_apply]

theorem exponents_snoc {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.snoc v j) =
      Finsupp.single (Fin.last m) j + (exponents v).mapDomain Fin.castSucc := by
  classical
  ext k
  refine Fin.lastCases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply Fin.castSucc_injective]
    simp [exponents, Finsupp.single_apply]

theorem encode_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    encode (m+1) (prepend j D) = X 0 ^ j * rename Fin.succ (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [prepend, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, encode_single]
    rw [exponents_cons, monomial_single_add, rename_monomial]

theorem encode_append {m : ℕ} (j : ℕ) (D : Words m) :
    encode (m+1) (append j D) = X (Fin.last m) ^ j * rename Fin.castSucc (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [append, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, encode_single]
    rw [exponents_snoc, monomial_single_add, rename_monomial]

theorem encode_bracket_zero {m : ℕ} (D : Words m) :
    encode (m+1) (bracket 0 D) = N8Polynomial.bracket0 (encode m D) := by
  simp [bracket, encode_prepend, encode_append, N8Polynomial.bracket0]

theorem deriv_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    deriv m (Finsupp.single v c) = ∑ i, Finsupp.single (increment i v) c := by
  classical
  simp [deriv, Finsupp.lmapDomain_apply]

theorem encode_deriv {m : ℕ} (D : Words m) :
    encode m (deriv m D) = N8Polynomial.delta (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp [N8Polynomial.delta]
  | add D F hd hf => simp [map_add, hd, hf, N8Polynomial.delta, mul_add]
  | single v c =>
    rw [deriv_single, map_sum]
    simp only [encode_single, exponents_increment, monomial_single_add, pow_one]
    simp [N8Polynomial.delta, Finset.sum_mul]

theorem realize_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (prepend j D) = E j * realize m D := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [prepend, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, realize_single]
    simp [word, List.ofFn_cons, E, ← MonoidAlgebra.single_mul_single]

theorem realize_append {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (append j D) = realize m D * E j := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, add_mul]
  | single v c =>
    simp only [append, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, realize_single]
    have hs : List.ofFn (Fin.snoc v j) = List.ofFn v ++ [j] := by
      rw [List.ofFn_succ']
      simp
    simp [word, hs, E, ← MonoidAlgebra.single_mul_single]

theorem realize_bracket {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (bracket j D) = E j * realize m D - realize m D * E j := by
  simp [bracket, realize_prepend, realize_append]

theorem exponents_zero (m : ℕ) : exponents (fun _ : Fin m => 0) = 0 := by
  ext i
  rfl

theorem encode_zero_word (m : ℕ) (c : ℚ) :
    encode m (Finsupp.single (fun _ => 0) c) = C c := by
  rw [encode_single, exponents_zero]
  rfl

theorem positional_word_constant {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : deriv (m+1) V = bracket 0 D)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    ∃ c : ℚ, D = Finsupp.single (fun _ => 0) c := by
  have hd := congrArg (encode (m+1)) hdelta
  rw [encode_deriv, encode_bracket_zero] at hd
  rw [encode_bracket_zero] at hdiag
  have hc := N8Polynomial.rational_diagonal_constant (encode m D) (encode (m+1) V) hd hdiag
  refine ⟨constantCoeff (encode m D), (encode m).injective ?_⟩
  rw [encode_zero_word]
  exact hc

end N8Words

#print axioms N8Words.positional_word_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Words.encode_single, ``N8Words.realize_single,
      ``N8Words.realize_injective, ``N8Words.exponents_increment,
      ``N8Words.exponents_cons, ``N8Words.exponents_snoc,
      ``N8Words.encode_prepend, ``N8Words.encode_append,
      ``N8Words.encode_bracket_zero, ``N8Words.deriv_single,
      ``N8Words.encode_deriv, ``N8Words.realize_prepend,
      ``N8Words.realize_append, ``N8Words.realize_bracket,
      ``N8Words.exponents_zero, ``N8Words.encode_zero_word,
      ``N8Words.positional_word_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 ordered-word positional dictionary"
