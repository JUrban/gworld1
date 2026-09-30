import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- Universal finite-dimensional reachability arguments only. The concrete
   monomial lift and the imported equation-to-EDT0L construction are separate. -/
namespace ControlledSpan

variable {K V E Q : Type*} [Field K] [AddCommGroup V] [Module K V]

def run (T : E → V →ₗ[K] V) : List E → V → V
  | [], x => x
  | e :: w, x => T e (run T w x)

noncomputable def stage (T : E → V →ₗ[K] V) (S : Set V) : ℕ → Submodule K V
  | 0 => Submodule.span K S
  | n + 1 => stage T S n ⊔ ⨆ e, (stage T S n).map (T e)

theorem stage_le_succ (T : E → V →ₗ[K] V) (S : Set V) (n : ℕ) :
    stage T S n ≤ stage T S (n+1) := le_sup_left

theorem stage_mono (T : E → V →ₗ[K] V) (S : Set V) : Monotone (stage T S) :=
  monotone_nat_of_le_succ (stage_le_succ T S)

theorem step_mem (T : E → V →ₗ[K] V) (S : Set V) (n : ℕ) (e : E)
    {v : V} (hv : v ∈ stage T S n) : T e v ∈ stage T S (n+1) := by
  exact (show (stage T S n).map (T e) ≤ stage T S (n+1) from
    (le_iSup (fun e => (stage T S n).map (T e)) e).trans le_sup_right)
    (Submodule.mem_map.mpr ⟨v, hv, rfl⟩)

theorem stable_tail (T : E → V →ₗ[K] V) (S : Set V) (n : ℕ)
    (h : stage T S n = stage T S (n+1)) (k : ℕ) :
    stage T S (n+k) = stage T S n := by
  induction k with
  | zero => simp
  | succ k ih =>
    calc
      stage T S (n+(k+1)) = stage T S (n+k) ⊔ ⨆ e, (stage T S (n+k)).map (T e) := by
        rw [← Nat.add_assoc, stage]
      _ = stage T S n ⊔ ⨆ e, (stage T S n).map (T e) := by rw [ih]
      _ = stage T S n := h.symm

theorem bounded_run_mem (T : E → V →ₗ[K] V) (S : Set V)
    (w : List E) {x : V} (hx : x ∈ S) {n : ℕ} (hn : w.length ≤ n) :
    run T w x ∈ stage T S n := by
  induction w generalizing n with
  | nil => exact stage_mono T S (Nat.zero_le n) (Submodule.subset_span hx)
  | cons e w ih =>
    cases n with
    | zero => simp at hn
    | succ n => exact step_mem T S n e (ih (by simpa using hn))

theorem stage_eq_bounded_span (T : E → V →ₗ[K] V) (S : Set V) (n : ℕ) :
    stage T S n = Submodule.span K
      {v | ∃ w x, x ∈ S ∧ w.length ≤ n ∧ run T w x = v} := by
  apply le_antisymm
  · induction n with
    | zero =>
      apply Submodule.span_mono
      intro x hx
      exact ⟨[], x, hx, by simp, rfl⟩
    | succ n ih =>
      apply sup_le
      · exact ih.trans (Submodule.span_mono (by
          rintro v ⟨w, x, hx, hw, rfl⟩
          exact ⟨w, x, hx, Nat.le_step hw, rfl⟩))
      · apply iSup_le
        intro e
        apply Submodule.map_le_iff_le_comap.mpr
        apply ih.trans
        apply Submodule.span_le.mpr
        rintro v ⟨w, x, hx, hw, rfl⟩
        exact Submodule.subset_span ⟨e::w, x, hx, by simpa using hw, rfl⟩
  · apply Submodule.span_le.mpr
    rintro v ⟨w, x, hx, hw, rfl⟩
    exact bounded_run_mem T S w hx hw

theorem stable_contains_all_runs (T : E → V →ₗ[K] V) (S : Set V)
    (n : ℕ) (h : stage T S n = stage T S (n+1))
    (w : List E) {x : V} (hx : x ∈ S) : run T w x ∈ stage T S n := by
  have hm := bounded_run_mem T S w hx (show w.length ≤ n+w.length by omega)
  rwa [stable_tail T S n h w.length] at hm

theorem stable_zero_iff (T : E → V →ₗ[K] V) (S : Set V)
    (n : ℕ) (h : stage T S n = stage T S (n+1)) (ell : V →ₗ[K] K) :
    (∀ w x, x ∈ S → ell (run T w x) = 0) ↔ stage T S n ≤ LinearMap.ker ell := by
  constructor
  · intro hz
    rw [stage_eq_bounded_span]
    apply Submodule.span_le.mpr
    rintro v ⟨w, x, hx, _, rfl⟩
    exact hz w x hx
  · intro hz w x hx
    exact hz (stable_contains_all_runs T S n h w hx)

theorem bounded_nonzero_witness (T : E → V →ₗ[K] V) (S : Set V)
    (n : ℕ) (h : stage T S n = stage T S (n+1)) (ell : V →ₗ[K] K)
    (hnz : ∃ w x, x ∈ S ∧ ell (run T w x) ≠ 0) :
    ∃ w x, x ∈ S ∧ w.length ≤ n ∧ ell (run T w x) ≠ 0 := by
  by_contra hn
  push_neg at hn
  have hz : stage T S n ≤ LinearMap.ker ell := by
    rw [stage_eq_bounded_span]
    apply Submodule.span_le.mpr
    rintro v ⟨w, x, hx, hw, rfl⟩
    exact hn w x hx hw
  obtain ⟨w, x, hx, hw⟩ := hnz
  exact hw ((stable_zero_iff T S n h ell).mpr hz w x hx)

section Finite
variable [FiniteDimensional K V]

theorem exists_stable_stage (T : E → V →ₗ[K] V) (S : Set V) :
    ∃ n ≤ Module.finrank K V, stage T S n = stage T S (n+1) := by
  by_contra hn
  push_neg at hn
  have growth (n : ℕ) (hb : n ≤ Module.finrank K V + 1) :
      n ≤ Module.finrank K (stage T S n) := by
    induction n with
    | zero => omega
    | succ n ih =>
      have hd := Submodule.finrank_lt_finrank_of_lt
        (lt_of_le_of_ne (stage_le_succ T S n) (hn n (by omega)))
      have hi := ih (by omega)
      omega
  have hg := growth (Module.finrank K V + 1) (by omega)
  have hu := (stage T S (Module.finrank K V + 1)).finrank_le
  omega

theorem dimension_stage_stable (T : E → V →ₗ[K] V) (S : Set V) :
    stage T S (Module.finrank K V) = stage T S (Module.finrank K V + 1) := by
  obtain ⟨n, hn, hs⟩ := exists_stable_stage T S
  obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le hn
  rw [hk, stable_tail T S n hs k]
  simpa [Nat.add_assoc] using (stable_tail T S n hs (k+1)).symm

theorem dimension_bounded_test (T : E → V →ₗ[K] V) (S : Set V)
    (ell : V →ₗ[K] K) :
    (∀ w x, x ∈ S → ell (run T w x) = 0) ↔
      (∀ w x, x ∈ S → w.length ≤ Module.finrank K V → ell (run T w x) = 0) := by
  constructor
  · intro h w x hx _; exact h w x hx
  · intro h
    apply (stable_zero_iff T S _ (dimension_stage_stable T S) ell).mpr
    rw [stage_eq_bounded_span]
    apply Submodule.span_le.mpr
    rintro v ⟨w, x, hx, hw, rfl⟩
    exact h w x hx hw

end Finite

inductive Reach (src dst : E → Q) (T : E → V →ₗ[K] V)
    (initial : Set Q) (seed : Q → V) : Q → V → Prop
  | start (q : Q) (hq : q ∈ initial) : Reach src dst T initial seed q (seed q)
  | step (e : E) (v : V) (hv : Reach src dst T initial seed (src e) v) :
      Reach src dst T initial seed (dst e) (T e v)

theorem reach_mem_closed_family (src dst : E → Q) (T : E → V →ₗ[K] V)
    (initial : Set Q) (seed : Q → V) (W : Q → Submodule K V)
    (hi : ∀ q ∈ initial, seed q ∈ W q)
    (he : ∀ e v, v ∈ W (src e) → T e v ∈ W (dst e))
    {q : Q} {v : V} (h : Reach src dst T initial seed q v) : v ∈ W q := by
  induction h with
  | start q hq => exact hi q hq
  | step e v _ ih => exact he e v ih

theorem zero_certificate_sound (src dst : E → Q) (T : E → V →ₗ[K] V)
    (initial final : Set Q) (seed : Q → V) (W : Q → Submodule K V)
    (hi : ∀ q ∈ initial, seed q ∈ W q)
    (he : ∀ e v, v ∈ W (src e) → T e v ∈ W (dst e))
    (ell : V →ₗ[K] K) (hz : ∀ q ∈ final, W q ≤ LinearMap.ker ell) :
    ∀ q v, q ∈ final → Reach src dst T initial seed q v → ell v = 0 := by
  intro q v hq hr
  exact hz q hq (reach_mem_closed_family src dst T initial seed W hi he hr)

theorem reachable_span_test (src dst : E → Q) (T : E → V →ₗ[K] V)
    (initial final : Set Q) (seed : Q → V) (ell : V →ₗ[K] K) :
    (∀ q v, q ∈ final → Reach src dst T initial seed q v → ell v = 0) ↔
    (∀ q ∈ final, Submodule.span K {v | Reach src dst T initial seed q v}
      ≤ LinearMap.ker ell) := by
  constructor
  · intro h q hq
    exact Submodule.span_le.mpr (fun v hv => h q v hq hv)
  · intro h q v hq hv
    exact h q hq (Submodule.subset_span hv)

end ControlledSpan

#print axioms ControlledSpan.dimension_bounded_test
#print axioms ControlledSpan.zero_certificate_sound

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``ControlledSpan.stage_le_succ,
      ``ControlledSpan.stage_mono, ``ControlledSpan.step_mem,
      ``ControlledSpan.stable_tail, ``ControlledSpan.bounded_run_mem,
      ``ControlledSpan.stage_eq_bounded_span, ``ControlledSpan.stable_contains_all_runs,
      ``ControlledSpan.stable_zero_iff, ``ControlledSpan.bounded_nonzero_witness,
      ``ControlledSpan.exists_stable_stage, ``ControlledSpan.dimension_stage_stable,
      ``ControlledSpan.dimension_bounded_test, ``ControlledSpan.reach_mem_closed_family,
      ``ControlledSpan.zero_certificate_sound, ``ControlledSpan.reachable_span_test] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS controlled-span universal reachability and finite dimension bound"
