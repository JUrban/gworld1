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
  Finsupp.lmapDomain ℚ ℚ (fun v : Fin m → ℕ => Fin.cons j v)

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
  change Finsupp.mapDomain exponents (Finsupp.single v c) = Finsupp.single (exponents v) c
  exact Finsupp.mapDomain_single

@[simp] theorem realize_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    realize m (Finsupp.single v c) = Finsupp.single (word v) c := by
  change Finsupp.mapDomain word (Finsupp.single v c) = Finsupp.single (word v) c
  exact Finsupp.mapDomain_single

theorem realize_injective (m : ℕ) : Function.Injective (realize m) := by
  apply Finsupp.mapDomain_injective
  intro v w h
  exact List.ofFn_injective (FreeMonoid.ofList.injective h)

theorem exponents_increment {m : ℕ} (i : Fin m) (v : Fin m → ℕ) :
    exponents (increment i v) = Finsupp.single i 1 + exponents v := by
  classical
  ext k
  by_cases h : k = i <;> simp [exponents, increment, h, add_comm]

theorem exponents_cons {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.cons j v) =
      Finsupp.single 0 j + (exponents v).mapDomain Fin.succ := by
  classical
  ext k
  refine Fin.cases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply (Fin.succ_injective m)]
    simp [exponents]

theorem exponents_snoc {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.snoc v j) =
      Finsupp.single (Fin.last m) j + (exponents v).mapDomain Fin.castSucc := by
  classical
  ext k
  refine Fin.lastCases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply (Fin.castSucc_injective m)]
    simp [exponents]

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
    change MonoidAlgebra.single (word (Fin.cons j v)) c =
      MonoidAlgebra.single (FreeMonoid.of j) 1 * MonoidAlgebra.single (word v) c
    rw [MonoidAlgebra.single_mul_single, one_mul]
    congr 1
    simp only [word, List.ofFn_cons, FreeMonoid.ofList_cons]

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
    change MonoidAlgebra.single (word (Fin.snoc v j)) c =
      MonoidAlgebra.single (word v) c * MonoidAlgebra.single (FreeMonoid.of j) 1
    rw [MonoidAlgebra.single_mul_single, mul_one]
    congr 1

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

theorem sum_variables_ne_zero {m : ℕ} (hm : 0 < m) :
    (∑ i : Fin m, X i : MvPolynomial (Fin m) ℚ) ≠ 0 := by
  intro h
  have hh := congrArg (eval (fun _ => (1 : ℚ))) h
  simp only [map_sum, eval_X, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, mul_one, map_zero] at hh
  have hz : m = 0 := by exact_mod_cast hh
  omega

theorem deriv_injective {m : ℕ} (hm : 0 < m) : Function.Injective (deriv m) := by
  intro D F h
  apply (encode m).injective
  have hh := congrArg (encode m) h
  rw [encode_deriv, encode_deriv] at hh
  exact mul_left_cancel₀ (sum_variables_ne_zero hm) hh

theorem bracket_zero_word (m : ℕ) (c : ℚ) :
    bracket 0 (Finsupp.single (fun _ : Fin m => 0) c) = 0 := by
  apply (encode (m+1)).injective
  rw [encode_bracket_zero, encode_zero_word]
  simp [N8Polynomial.bracket0]

theorem positional_word_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : deriv (m+1) V = bracket 0 D)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, D = Finsupp.single (fun _ => 0) c) ∧ V = 0 := by
  obtain ⟨c, hc⟩ := positional_word_constant D V hdelta hdiag
  refine ⟨⟨c, hc⟩, deriv_injective (Nat.zero_lt_succ m) ?_⟩
  rw [hdelta, hc, bracket_zero_word, map_zero]

theorem deriv_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    deriv (m+1) (prepend j D) = prepend (j+1) D + prepend j (deriv m D) := by
  apply (encode (m+1)).injective
  rw [encode_deriv, map_add, encode_prepend, encode_prepend, encode_prepend, encode_deriv]
  simp only [N8Polynomial.delta, map_mul, map_sum, rename_X, Fin.sum_univ_succ, pow_succ]
  ring

def basisWord (w : List ℕ) : Assoc := Finsupp.single (FreeMonoid.ofList w) 1

def derivWord : List ℕ → Assoc
  | [] => 0
  | i :: w => E (i+1) * basisWord w + E i * derivWord w

def assocDeriv : Assoc →ₗ[ℚ] Assoc :=
  Finsupp.linearCombination ℚ (fun w => derivWord (FreeMonoid.toList w))

theorem assocDeriv_single (w : FreeMonoid ℕ) (c : ℚ) :
    assocDeriv (Finsupp.single w c) = c • derivWord (FreeMonoid.toList w) := by
  exact Finsupp.linearCombination_single ℚ c w

theorem derivWord_ofFn (m : ℕ) (v : Fin m → ℕ) :
    derivWord (List.ofFn v) = realize m (deriv m (Finsupp.single v 1)) := by
  classical
  induction m with
  | zero => simp [derivWord, deriv]
  | succ m ih =>
    let a := v 0
    let u := Fin.tail v
    have hv : v = Fin.cons a u := (Fin.cons_self_tail v).symm
    have hs : Finsupp.single (Fin.cons a u) (1 : ℚ) = prepend a (Finsupp.single u 1) := by
      simp [prepend, Finsupp.lmapDomain_apply]
    rw [hv, List.ofFn_cons, derivWord, hs, deriv_prepend, map_add,
      realize_prepend, realize_prepend]
    rw [← ih u, realize_single]
    rfl

theorem assocDeriv_realize {m : ℕ} (D : Words m) :
    assocDeriv (realize m D) = realize m (deriv m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf]
  | single v c =>
    rw [realize_single, assocDeriv_single]
    have hs : Finsupp.single v c = c • Finsupp.single v (1 : ℚ) := by simp
    rw [hs, map_smul, map_smul, ← derivWord_ofFn]
    rfl

theorem assocDeriv_generator (j : ℕ) : assocDeriv (E j) = E (j+1) := by
  rw [E, assocDeriv_single]
  simp only [FreeMonoid.toList_of, derivWord, basisWord, FreeMonoid.ofList_nil,
    ← MonoidAlgebra.one_def, mul_one, mul_zero, add_zero, one_smul]

theorem ambient_positional_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, D = Finsupp.single (fun _ => 0) c) ∧ realize (m+1) V = 0 := by
  have hd : deriv (m+1) V = bracket 0 D := by
    apply realize_injective (m+1)
    simpa only [← assocDeriv_realize, realize_bracket] using hdelta
  obtain ⟨hc, hv⟩ := positional_word_separation D V hd hdiag
  exact ⟨hc, by rw [hv, map_zero]⟩

theorem basisWord_nil : basisWord [] = 1 := by
  rfl

theorem basisWord_cons (j : ℕ) (w : List ℕ) :
    basisWord (j :: w) = E j * basisWord w := by
  simp only [basisWord, E, MonoidAlgebra.single_mul_single, one_mul,
    FreeMonoid.ofList_cons]

theorem basisWord_append (u v : List ℕ) :
    basisWord (u ++ v) = basisWord u * basisWord v := by
  simp only [basisWord, MonoidAlgebra.single_mul_single, one_mul,
    FreeMonoid.ofList_append]

theorem derivWord_append (u v : List ℕ) :
    derivWord (u ++ v) = derivWord u * basisWord v + basisWord u * derivWord v := by
  induction u with
  | nil => simp [derivWord, basisWord_nil]
  | cons j u ih =>
    simp only [List.cons_append, derivWord, basisWord_append, basisWord_cons, ih]
    noncomm_ring

theorem single_eq_smul_basis (w : FreeMonoid ℕ) (c : ℚ) :
    (Finsupp.single w c : Assoc) = c • basisWord (FreeMonoid.toList w) := by
  simp [basisWord, Finsupp.smul_single]

theorem assocDeriv_mul (F G : Assoc) :
    assocDeriv (F * G) = assocDeriv F * G + F * assocDeriv G := by
  classical
  induction F using Finsupp.induction_linear with
  | zero => simp
  | add F H hf hh => simp [add_mul, map_add, hf, hh, add_assoc, add_left_comm, add_comm]
  | single u c =>
    induction G using Finsupp.induction_linear with
    | zero => simp
    | add G H hg hh => simp [mul_add, map_add, hg, hh, add_assoc, add_left_comm, add_comm]
    | single v d =>
      rw [MonoidAlgebra.single_mul_single, assocDeriv_single, assocDeriv_single,
        assocDeriv_single, FreeMonoid.toList_mul, derivWord_append, smul_add,
        single_eq_smul_basis v d, single_eq_smul_basis u c]
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul]

theorem basisWord_replicate (j m : ℕ) : basisWord (List.replicate m j) = E j ^ m := by
  induction m with
  | zero => simp [basisWord_nil]
  | succ m ih => simp only [List.replicate_succ, basisWord_cons, ih, pow_succ']

theorem realize_zero_word (m : ℕ) (c : ℚ) :
    realize m (Finsupp.single (fun _ : Fin m => 0) c) = c • E 0 ^ m := by
  rw [realize_single, single_eq_smul_basis]
  simp only [word, FreeMonoid.toList_ofList, List.ofFn_const, basisWord_replicate]

theorem associative_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, realize m D = c • E 0 ^ m) ∧ realize (m+1) V = 0 := by
  obtain ⟨⟨c, hc⟩, hv⟩ := ambient_positional_separation D V hdelta hdiag
  exact ⟨⟨c, by rw [hc, realize_zero_word]⟩, hv⟩

theorem diagonalVars_sum (m : ℕ) : (∑ i, N8Polynomial.diagonalVars m i) = 0 := by
  simp only [N8Polynomial.diagonalVars, Fin.sum_cons, Fin.sum_snoc]
  have hc : (C (-1/2) : MvPolynomial (Fin m) ℚ) = -(1/2) := by norm_num
  rw [hc]
  ring

theorem restriction_delta_zero {m : ℕ} (D : Words (m+2)) :
    N8Polynomial.restriction (encode (m+2) (deriv (m+2) D)) = 0 := by
  rw [encode_deriv]
  simp [N8Polynomial.restriction, N8Polynomial.delta, diagonalVars_sum]

theorem restriction_bracket {m : ℕ} (j : ℕ) (D : Words (m+1)) :
    N8Polynomial.restriction (encode (m+2) (bracket j D)) =
      (C (-1/2) * ∑ i : Fin m, X i) ^ j *
        N8Polynomial.restriction (encode (m+2) (bracket 0 D)) := by
  simp only [bracket, LinearMap.sub_apply, map_sub, encode_prepend, encode_append]
  simp [N8Polynomial.restriction, N8Polynomial.diagonalVars, mul_sub]

end N8Words

#print axioms N8Words.positional_word_constant
#print axioms N8Words.associative_separation

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
      ``N8Words.positional_word_constant, ``N8Words.sum_variables_ne_zero,
      ``N8Words.deriv_injective, ``N8Words.bracket_zero_word,
      ``N8Words.positional_word_separation, ``N8Words.deriv_prepend,
      ``N8Words.assocDeriv_single, ``N8Words.derivWord_ofFn,
      ``N8Words.assocDeriv_realize, ``N8Words.assocDeriv_generator,
      ``N8Words.ambient_positional_separation, ``N8Words.basisWord_nil,
      ``N8Words.basisWord_cons, ``N8Words.basisWord_append,
      ``N8Words.derivWord_append, ``N8Words.single_eq_smul_basis,
      ``N8Words.assocDeriv_mul, ``N8Words.basisWord_replicate,
      ``N8Words.realize_zero_word, ``N8Words.associative_separation,
      ``N8Words.diagonalVars_sum, ``N8Words.restriction_delta_zero,
      ``N8Words.restriction_bracket] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 ordered-word positional dictionary"
