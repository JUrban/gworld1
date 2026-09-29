import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Algebra.BigOperators.Module
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- Abstract full-block implication only. The group/Lie identification of
   these hypotheses remains in the written N8 proof. -/
namespace N8Block

open scoped BigOperators

variable {K W M : Type*} [Field K]
variable [AddCommGroup W] [Module K W] [AddCommGroup M] [Module K M]

theorem triangular_vanishes (t : ℕ) (b : K) (hb : b ≠ 0)
    (F : ℕ → W) (c : ℕ → ℕ → K)
    (heq : ∀ j < t, b • F j + ∑ k ∈ Finset.range j, c j k • F k = 0) :
    ∀ j < t, F j = 0 := by
  intro j
  induction j using Nat.strong_induction_on with
  | h j ih =>
    intro hj
    have hsum : (∑ k ∈ Finset.range j, c j k • F k) = 0 := by
      apply Finset.sum_eq_zero
      intro k hk
      have hkj : k < j := Finset.mem_range.mp hk
      rw [ih k hkj (lt_trans hkj hj), smul_zero]
    have h := heq j hj
    rw [hsum, add_zero] at h
    exact (smul_eq_zero.mp h).resolve_left hb

theorem later_column_vanishes (t : ℕ) (F : ℕ → W)
    (hF : ∀ j < t, F j = 0) (d : ℕ → K) :
    (∑ i ∈ Finset.Ioc t (2*t), d i • F (2*t-i)) = 0 := by
  apply Finset.sum_eq_zero
  intro i hi
  have hi' := Finset.mem_Ioc.mp hi
  have hj : 2*t-i < t := by omega
  rw [hF _ hj, smul_zero]

theorem block_annihilated {I : Type*} (t : ℕ) (b : K) (hb : b ≠ 0)
    (F : ℕ → W) (c : ℕ → ℕ → K)
    (heq : ∀ j < t, b • F j + ∑ k ∈ Finset.range j, c j k • F k = 0)
    (phi : M →ₗ[K] W) (A : Submodule K M) (B : I → M)
    (hA : A ≤ LinearMap.ker phi) (d : I → ℕ → K)
    (hB : ∀ s, phi (B s) = ∑ i ∈ Finset.Ioc t (2*t), d s i • F (2*t-i)) :
    A ⊔ Submodule.span K (Set.range B) ≤ LinearMap.ker phi := by
  have hF := triangular_vanishes t b hb F c heq
  refine sup_le hA (Submodule.span_le.mpr ?_)
  rintro _ ⟨s, rfl⟩
  rw [LinearMap.mem_ker, hB s]
  exact later_column_vanishes t F hF (d s)

theorem block_quadratic_not_mem {I : Type*} (t : ℕ) (b : K) (hb : b ≠ 0)
    (F : ℕ → W) (c : ℕ → ℕ → K)
    (heq : ∀ j < t, b • F j + ∑ k ∈ Finset.range j, c j k • F k = 0)
    (phi : M →ₗ[K] W) (A : Submodule K M) (B : I → M)
    (hA : A ≤ LinearMap.ker phi) (d : I → ℕ → K)
    (hB : ∀ s, phi (B s) = ∑ i ∈ Finset.Ioc t (2*t), d s i • F (2*t-i))
    (q : M) (Q : W) (hQ : Q ≠ 0) (hq : phi q = (b*b) • Q) :
    q ∉ A ⊔ Submodule.span K (Set.range B) := by
  intro hmem
  have hzero := block_annihilated t b hb F c heq phi A B hA d hB hmem
  rw [LinearMap.mem_ker, hq, smul_eq_zero] at hzero
  exact hzero.elim (mul_ne_zero hb hb) hQ

theorem quadratic_three_roots (q l c : W) (hq : q ≠ 0)
    (x y z : K)
    (hx : x^2 • q + x • l + c = 0)
    (hy : y^2 • q + y • l + c = 0)
    (hz : z^2 • q + z • l + c = 0) :
    x = y ∨ x = z ∨ y = z := by
  by_cases hxy : x = y
  · exact Or.inl hxy
  by_cases hxz : x = z
  · exact Or.inr (Or.inl hxz)
  have hdxy : (x-y) • ((x+y) • q + l) = 0 := by
    calc
      _ = (x^2 • q + x • l + c) - (y^2 • q + y • l + c) := by module
      _ = 0 := by rw [hx, hy]; simp
  have hdxz : (x-z) • ((x+z) • q + l) = 0 := by
    calc
      _ = (x^2 • q + x • l + c) - (z^2 • q + z • l + c) := by module
      _ = 0 := by rw [hx, hz]; simp
  have hvxy : (x+y) • q + l = 0 :=
    (smul_eq_zero.mp hdxy).resolve_left (sub_ne_zero.mpr hxy)
  have hvxz : (x+z) • q + l = 0 :=
    (smul_eq_zero.mp hdxz).resolve_left (sub_ne_zero.mpr hxz)
  have hyz : (y-z) • q = 0 := by
    calc
      _ = ((x+y) • q + l) - ((x+z) • q + l) := by module
      _ = 0 := by rw [hvxy, hvxz]; simp
  exact Or.inr (Or.inr (sub_eq_zero.mp ((smul_eq_zero.mp hyz).resolve_right hq)))

theorem three_liftable_parameters (phi : M →ₗ[K] W)
    (S : Submodule K M) (hS : S ≤ LinearMap.ker phi)
    (q l c : M) (hq : phi q ≠ 0) (x y z : K)
    (hx : x^2 • q + x • l + c ∈ S)
    (hy : y^2 • q + y • l + c ∈ S)
    (hz : z^2 • q + z • l + c ∈ S) :
    x = y ∨ x = z ∨ y = z := by
  have project (u : K) (hu : u^2 • q + u • l + c ∈ S) :
      u^2 • phi q + u • phi l + phi c = 0 := by
    have h := hS hu
    simpa only [LinearMap.mem_ker, map_add, map_smul] using h
  exact quadratic_three_roots (phi q) (phi l) (phi c) hq x y z
    (project x hx) (project y hy) (project z hz)

end N8Block

#print axioms N8Block.block_quadratic_not_mem
#print axioms N8Block.three_liftable_parameters

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Block.triangular_vanishes,
      ``N8Block.later_column_vanishes, ``N8Block.block_annihilated,
      ``N8Block.block_quadratic_not_mem, ``N8Block.quadratic_three_roots,
      ``N8Block.three_liftable_parameters] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 full-block separation and two-parameter-value bound"
