import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- Universal finite-tuple bridge only. The positional encoding of free Lie
   elements and the full N8 algorithm are not formalized here. -/
namespace N8Bridge

open scoped BigOperators

def DeltaEquation {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) : Prop :=
  ∀ w, (∑ i, w i) * V w = P (Fin.tail w) - P (Fin.init w)

def DiagonalZero {m : ℕ} (V : (Fin (m + 1) → ℝ) → ℝ) : Prop :=
  ∀ w : Fin (m + 2) → ℝ, (∑ i, w i) = 0 →
    w 0 = w (Fin.last (m + 1)) → V (Fin.tail w) = V (Fin.init w)

theorem cyclic_boundary {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) (hdelta : DeltaEquation P V)
    (w : Fin (m + 1) → ℝ) (hzero : (∑ i, w i) = 0) :
    P (Fin.tail w) = P (Fin.init w) := by
  have h := hdelta w
  rw [hzero, zero_mul] at h
  linarith

theorem tail_snoc {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    Fin.tail (α := fun _ : Fin (n + 2) => ℝ) (Fin.snoc z a) =
      Fin.snoc (Fin.tail z) a := by
  have h := congrArg (Fin.tail (α := fun _ : Fin (n + 2) => ℝ))
    (Fin.cons_snoc_eq_snoc_cons (z 0) (Fin.tail z) a)
  simpa only [Fin.tail_cons, Fin.cons_self_tail] using h.symm

theorem init_cons {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    Fin.init (α := fun _ : Fin (n + 2) => ℝ) (Fin.cons a z) =
      Fin.cons a (Fin.init z) := by
  have h := congrArg (Fin.init (α := fun _ : Fin (n + 2) => ℝ))
    (Fin.cons_snoc_eq_snoc_cons a (Fin.init z) (z (Fin.last n)))
  simpa only [Fin.init_snoc, Fin.snoc_init_self] using h

theorem diagonal_midpoint {m : ℕ} (V : (Fin (m + 1) → ℝ) → ℝ)
    (hdiag : DiagonalZero V) (z : Fin m → ℝ) (a : ℝ)
    (ha : 2 * a + ∑ i, z i = 0) :
    V (Fin.snoc z a) = V (Fin.cons a z) := by
  have hz : (∑ i, (Fin.cons a (Fin.snoc z a)) i) = 0 := by
    rw [Fin.sum_cons, Fin.sum_snoc]
    linarith
  have hend : (Fin.cons (α := fun _ : Fin (m + 2) => ℝ) a (Fin.snoc z a)) 0 =
      (Fin.cons (α := fun _ : Fin (m + 2) => ℝ) a (Fin.snoc z a))
        (Fin.last (m + 1)) := by simp
  have h := hdiag (Fin.cons a (Fin.snoc z a)) hz hend
  rw [Fin.tail_cons, Fin.cons_snoc_eq_snoc_cons, Fin.init_snoc] at h
  exact h

theorem boundary_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) (a : ℝ) (ha : 2 * a + ∑ i, z i = 0) :
    2 * P z = P (Fin.snoc (Fin.tail z) a) + P (Fin.cons a (Fin.init z)) := by
  have hv := diagonal_midpoint V hdiag z a ha
  have hr := hdelta (Fin.snoc z a)
  have hl := hdelta (Fin.cons a z)
  simp only [Fin.sum_snoc, Fin.init_snoc, tail_snoc] at hr
  simp only [Fin.sum_cons, Fin.tail_cons, init_cons] at hl
  rw [← hv] at hl
  nlinarith

def shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) : Fin (n + 1) → ℝ :=
  Fin.cons (z 0 + a) (Fin.tail z)

def shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) : Fin (n + 1) → ℝ :=
  Fin.snoc (Fin.init z) (z (Fin.last n) + a)

theorem sum_shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    (∑ i, shiftFirst z a i) = (∑ i, z i) + a := by
  simp only [shiftFirst, Fin.sum_cons]
  rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem sum_shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    (∑ i, shiftLast z a i) = (∑ i, z i) + a := by
  simp only [shiftLast, Fin.sum_snoc]
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.init]
  ring

theorem transfer_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) (a : ℝ) (ha : 2 * a + ∑ i, z i = 0) :
    2 * P z = P (shiftFirst z a) + P (shiftLast z a) := by
  have hrzero : (∑ i, (Fin.snoc (shiftFirst z a) a) i) = 0 := by
    rw [Fin.sum_snoc, sum_shiftFirst]
    linarith
  have hlzero : (∑ i, (Fin.cons a (shiftLast z a)) i) = 0 := by
    rw [Fin.sum_cons, sum_shiftLast]
    linarith
  have hr := cyclic_boundary P V hdelta (Fin.snoc (shiftFirst z a) a) hrzero
  have hl := cyclic_boundary P V hdelta (Fin.cons a (shiftLast z a)) hlzero
  simp only [Fin.init_snoc, tail_snoc, shiftFirst, Fin.tail_cons] at hr
  simp only [Fin.tail_cons, init_cons, shiftLast, Fin.init_snoc] at hl
  change P (Fin.snoc (Fin.tail z) a) = P (shiftFirst z a) at hr
  change P (shiftLast z a) = P (Fin.cons a (Fin.init z)) at hl
  rw [← hr, hl]
  exact boundary_average P V hdelta hdiag z a ha

theorem transfer_average_half {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) :
    2 * P z = P (shiftFirst z (-(∑ i, z i) / 2)) +
      P (shiftLast z (-(∑ i, z i) / 2)) := by
  apply transfer_average P V hdelta hdiag
  ring

def rotate {m : ℕ} (w : Fin (m + 1) → ℝ) : Fin (m + 1) → ℝ :=
  Fin.snoc (Fin.tail w) (w 0)

theorem sum_rotate {m : ℕ} (w : Fin (m + 1) → ℝ) :
    (∑ i, rotate w i) = ∑ i, w i := by
  simp only [rotate, Fin.sum_snoc]
  rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem cyclic_invariance {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) (hdelta : DeltaEquation P V)
    (w : Fin (m + 1) → ℝ) (hzero : (∑ i, w i) = 0) :
    P (Fin.tail (rotate w)) = P (Fin.tail w) := by
  have hrzero : (∑ i, rotate w i) = 0 := by rw [sum_rotate, hzero]
  have h := cyclic_boundary P V hdelta (rotate w) hrzero
  simpa only [rotate, Fin.init_snoc] using h

noncomputable def clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) : Fin (n + 2) → ℝ :=
  Fin.cons (w 0 / 2) (shiftFirst (Fin.tail w) (w 0 / 2))

noncomputable def counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) : Fin (n + 2) → ℝ :=
  Fin.cons (w 0 / 2) (shiftLast (Fin.tail w) (w 0 / 2))

theorem sum_clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    (∑ i, clockwise w i) = ∑ i, w i := by
  simp only [clockwise, Fin.sum_cons, sum_shiftFirst]
  conv_rhs => rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem sum_counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    (∑ i, counterclockwise w i) = ∑ i, w i := by
  simp only [counterclockwise, Fin.sum_cons, sum_shiftLast]
  conv_rhs => rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem origin_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (w : Fin (n + 2) → ℝ) (hzero : (∑ i, w i) = 0) :
    2 * P (Fin.tail w) = P (Fin.tail (clockwise w)) +
      P (Fin.tail (counterclockwise w)) := by
  have ha : 2 * (w 0 / 2) + ∑ i, (Fin.tail w) i = 0 := by
    rw [Fin.sum_univ_succ] at hzero
    simp only [Fin.tail]
    linarith
  simpa only [clockwise, counterclockwise, Fin.tail_cons] using
    transfer_average P V hdelta hdiag (Fin.tail w) (w 0 / 2) ha

def l1 {m : ℕ} (z : Fin m → ℝ) : ℝ := ∑ i, |z i|

theorem l1_cons {m : ℕ} (a : ℝ) (z : Fin m → ℝ) :
    l1 (Fin.cons a z) = |a| + l1 z := by
  unfold l1
  rw [Fin.sum_univ_succ]
  simp only [Fin.cons_zero, Fin.cons_succ]

theorem l1_snoc {m : ℕ} (z : Fin m → ℝ) (a : ℝ) :
    l1 (Fin.snoc z a) = l1 z + |a| := by
  unfold l1
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.snoc_last, Fin.snoc_castSucc]

theorem l1_shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    l1 (shiftFirst z a) ≤ l1 z + |a| := by
  have hz : l1 z = |z 0| + l1 (Fin.tail z) := by
    rw [← l1_cons, Fin.cons_self_tail]
  rw [shiftFirst, l1_cons, hz]
  linarith [abs_add_le (z 0) a]

theorem l1_shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    l1 (shiftLast z a) ≤ l1 z + |a| := by
  have hz : l1 z = l1 (Fin.init z) + |z (Fin.last n)| := by
    rw [← l1_snoc, Fin.snoc_init_self]
  rw [shiftLast, l1_snoc, hz]
  linarith [abs_add_le (z (Fin.last n)) a]

theorem l1_clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    l1 (clockwise w) ≤ l1 w := by
  have hw : l1 w = |w 0| + l1 (Fin.tail w) := by
    rw [← l1_cons, Fin.cons_self_tail]
  have habs : |w 0 / 2| = |w 0| / 2 := by norm_num [abs_div]
  have hb := l1_shiftFirst (Fin.tail w) (w 0 / 2)
  rw [clockwise, l1_cons, hw, habs]
  rw [habs] at hb
  linarith

theorem l1_counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    l1 (counterclockwise w) ≤ l1 w := by
  have hw : l1 w = |w 0| + l1 (Fin.tail w) := by
    rw [← l1_cons, Fin.cons_self_tail]
  have habs : |w 0 / 2| = |w 0| / 2 := by norm_num [abs_div]
  have hb := l1_shiftLast (Fin.tail w) (w 0 / 2)
  rw [counterclockwise, l1_cons, hw, habs]
  rw [habs] at hb
  linarith

end N8Bridge

#print axioms N8Bridge.transfer_average_half

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Bridge.cyclic_boundary, ``N8Bridge.tail_snoc,
      ``N8Bridge.init_cons, ``N8Bridge.diagonal_midpoint,
      ``N8Bridge.boundary_average, ``N8Bridge.sum_shiftFirst,
      ``N8Bridge.sum_shiftLast, ``N8Bridge.transfer_average,
      ``N8Bridge.transfer_average_half, ``N8Bridge.sum_rotate,
      ``N8Bridge.cyclic_invariance, ``N8Bridge.sum_clockwise,
      ``N8Bridge.sum_counterclockwise, ``N8Bridge.origin_average,
      ``N8Bridge.l1_cons, ``N8Bridge.l1_snoc, ``N8Bridge.l1_shiftFirst,
      ``N8Bridge.l1_shiftLast, ``N8Bridge.l1_clockwise,
      ``N8Bridge.l1_counterclockwise] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 division-free positional averaging bridge"
