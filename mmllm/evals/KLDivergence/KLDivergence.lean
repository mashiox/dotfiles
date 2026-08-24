import Mathlib

set_option linter.style.emptyLine false

open Finset

section KLDivergence

-- Define our finite sample space X
variable {X : Type*} [Fintype X]

-- P and Q are our probability distributions
variable (P Q : X → ℝ)

-- We define log as a general function to mirror your axiomatic approach
variable (log : ℝ → ℝ)

-- Axiom 1: Shannon Entropy
def H (P : X → ℝ) (log : ℝ → ℝ) : ℝ :=
  - ∑ x, P x * log (P x)

-- Axiom 2: Cross Entropy
def H_cross (P Q : X → ℝ) (log : ℝ → ℝ) : ℝ :=
  - ∑ x, P x * log (Q x)

-- Axiom 3: KL Divergence
noncomputable def D_KL (P Q : X → ℝ) (log : ℝ → ℝ) : ℝ :=
  ∑ x, P x * log (P x / Q x)

-- Recall: Log Quotient Rule
axiom log_quotient (A B : ℝ) : log (A / B) = log A - log B

-- Goal: Prove the identity H(P, Q) = H(P) + D_KL(P||Q)
-- We follow the algebraic steps: D_KL(P||Q) = H(P,Q) - H(P)
theorem kl_identity : H_cross P Q log - H P log = D_KL P Q log := by
  -- Sub in Ax 1 & Ax 2
  rw [H_cross, H]

  -- D_KL(P||Q) = [-\sum P(x)log(Q(x))] - [-\sum P(x)log(P(x))]
  -- This rearranges to: -\sum P(x)log Q(x) + \sum P(x)log P(x)
  have step1 : (- ∑ x, P x * log (Q x)) - (- ∑ x, P x * log (P x))
             = (∑ x, P x * log (P x)) - (∑ x, P x * log (Q x)) := by ring
  rw [step1]

  -- "= \sum P(x)log P(x) - \sum P(x)log Q(x)"
  rw [← sum_sub_distrib]

  -- "= \sum P(x) [ log P(x) - log Q(x) ]"
  have step2 : (∑ x, (P x * log (P x) - P x * log (Q x)))
             = ∑ x, P x * (log (P x) - log (Q x)) := by
    congr 1
    ext x
    ring
  rw [step2]

  -- Use log quotient rule backward: log P(x) - log Q(x) = log(P(x)/Q(x))
  have step3 : (∑ x, P x * (log (P x) - log (Q x)))
             = ∑ x, P x * log (P x / Q x) := by
    congr 1
    ext x
    rw [← log_quotient]
  rw [step3]

  -- "= D_KL(P||Q)"
  -- The goal matches the definition of D_KL perfectly now.
  rfl

end KLDivergence
