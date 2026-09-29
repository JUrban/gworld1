import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Data.List.Sum
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- A concrete sequence of adjacent half-transfer words, in every finite
   dimension. This does not formalize the Lie encoding or N8 algorithm. -/
namespace N8Sweep
open Filter Topology

def l1 (xs : List ℝ) : ℝ := (xs.map abs).sum

noncomputable def halfPair (p : ℝ × ℝ) : ℝ × ℝ :=
  (p.1 / 2, p.2 + p.1 / 2)

theorem halfPair_iterate (a b : ℝ) (k : ℕ) :
    halfPair^[k] (a,b) = ((1/2 : ℝ)^k * a, b + (1-(1/2 : ℝ)^k)*a) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih]
    simp only [halfPair, pow_succ]
    congr 1 <;> ring

noncomputable def sweepFrom (q a : ℝ) : List ℝ → List ℝ
  | [] => [a]
  | b :: xs => q*a :: sweepFrom q (b+(1-q)*a) xs

noncomputable def retained (q a : ℝ) : List ℝ → ℝ
  | [] => 0
  | b :: xs => |q*a| + retained q (b+(1-q)*a) xs

noncomputable def residue (q a : ℝ) : List ℝ → ℝ
  | [] => a
  | b :: xs => residue q (b+(1-q)*a) xs

theorem l1_nonneg (xs : List ℝ) : 0 ≤ l1 xs := by
  unfold l1
  exact List.sum_nonneg (by intro x hx; obtain ⟨y, hy, rfl⟩ := List.mem_map.mp hx; exact abs_nonneg y)

theorem l1_cons (a : ℝ) (xs : List ℝ) : l1 (a::xs) = |a| + l1 xs := by
  simp [l1]

theorem sweep_length (q a : ℝ) (xs : List ℝ) :
    (sweepFrom q a xs).length = xs.length+1 := by
  induction xs generalizing a with
  | nil => simp [sweepFrom]
  | cons b xs ih => simp [sweepFrom, ih]

theorem sweep_sum (q a : ℝ) (xs : List ℝ) :
    (sweepFrom q a xs).sum = a + xs.sum := by
  induction xs generalizing a with
  | nil => simp [sweepFrom]
  | cons b xs ih => simp only [sweepFrom, List.sum_cons, ih]; ring

theorem sweep_l1 (q a : ℝ) (xs : List ℝ) :
    l1 (sweepFrom q a xs) = retained q a xs + |residue q a xs| := by
  induction xs generalizing a with
  | nil => simp [sweepFrom, retained, residue, l1]
  | cons b xs ih => simp only [sweepFrom, retained, residue, l1_cons, ih]; ring

theorem remainder_size (q a b : ℝ) (xs : List ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) :
    |b+(1-q)*a| + l1 xs ≤ |a| + l1 (b::xs) := by
  have h := abs_add_le b ((1-q)*a)
  rw [abs_mul, abs_of_nonneg (sub_nonneg.mpr hq1)] at h
  rw [l1_cons]
  nlinarith [abs_nonneg a]

theorem retained_bound (q a : ℝ) (xs : List ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) :
    retained q a xs ≤ (xs.length : ℝ)*q*(|a|+l1 xs) := by
  induction xs generalizing a with
  | nil => simp [retained, l1]
  | cons b xs ih =>
    have hi := ih (b+(1-q)*a)
    have hr := remainder_size q a b xs hq0 hq1
    have hlen : 0 ≤ (xs.length : ℝ)*q := mul_nonneg (Nat.cast_nonneg _) hq0
    have hm := mul_le_mul_of_nonneg_left hr hlen
    have hn := l1_nonneg (b::xs)
    simp only [retained, List.length_cons, Nat.cast_add, Nat.cast_one]
    rw [abs_mul, abs_of_nonneg hq0]
    nlinarith

theorem residue_error (q a : ℝ) (xs : List ℝ) :
    |residue q a xs - (a + xs.sum)| ≤ retained q a xs := by
  induction xs generalizing a with
  | nil => simp [residue, retained]
  | cons b xs ih =>
    have hi := ih (b+(1-q)*a)
    have heq : residue q (b+(1-q)*a) xs - (a+(b+xs.sum)) =
        (residue q (b+(1-q)*a) xs - (b+(1-q)*a+xs.sum)) - q*a := by ring
    simp only [residue, retained, List.sum_cons]
    rw [heq]
    exact (abs_sub_le _ _).trans (by linarith)

theorem zero_sum_sweep_bound (q a : ℝ) (xs : List ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (hzero : a+xs.sum=0) :
    l1 (sweepFrom q a xs) ≤ 2*(xs.length : ℝ)*q*(|a|+l1 xs) := by
  have he := residue_error q a xs
  rw [hzero, sub_zero] at he
  have hb := retained_bound q a xs hq0 hq1
  rw [sweep_l1]
  linarith

theorem zero_sum_sweep_tendsto (a : ℝ) (xs : List ℝ)
    (hzero : a+xs.sum=0) :
    Tendsto (fun k : ℕ => l1 (sweepFrom ((1/2 : ℝ)^k) a xs)) atTop (𝓝 0) := by
  have hpow : Tendsto (fun k : ℕ => (1/2 : ℝ)^k) atTop (𝓝 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  have hup : Tendsto
      (fun k : ℕ => 2*(xs.length : ℝ)*((1/2 : ℝ)^k)*(|a|+l1 xs)) atTop (𝓝 0) := by
    have h := (hpow.const_mul (2*(xs.length : ℝ))).mul_const (|a|+l1 xs)
    simpa using h
  apply squeeze_zero (fun k => l1_nonneg _) (fun k => ?_) hup
  exact zero_sum_sweep_bound _ a xs (pow_nonneg (by norm_num) _)
    (pow_le_one₀ (by norm_num) (by norm_num)) hzero

end N8Sweep

#print axioms N8Sweep.zero_sum_sweep_tendsto
open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Sweep.halfPair_iterate, ``N8Sweep.l1_nonneg,
      ``N8Sweep.l1_cons, ``N8Sweep.sweep_length, ``N8Sweep.sweep_sum,
      ``N8Sweep.sweep_l1, ``N8Sweep.remainder_size, ``N8Sweep.retained_bound,
      ``N8Sweep.residue_error, ``N8Sweep.zero_sum_sweep_bound,
      ``N8Sweep.zero_sum_sweep_tendsto] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 concrete half-transfer sweep convergence"
