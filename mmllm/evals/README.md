# Fundamental Concepts

## Logarithms

Logarithms are the inverse of exponential functions. They are used extensively in probabilistic mathematics. I have included some revision on core identities.

**Exponential Identity**:

Given $a \gt 0$, $a \neq 1$, and $c \gt 0$

$$ a^b = c \equiv \log_a c = b$$

**Power Rule**:

$$ \log_a b^n = n \log_a b $$

**Product Rule**:

$$\log_a(f(x)g(x)) = \log_a f(x) + \log_a g(x)$$

**Quotient Rule**:

$$\log_a\frac{f(x)}{g(x)} = \log_a f(x) - \log_a g(x)$$

## Probability Distributions

**Probability Distributions**, are sets of real numbers mapped from a set of things like "states", "conditions", or "events". Many mathmatical models use very simple examples of **Discrete** events, like outcomes of a coin toss ($n=2, p=0.5$), or a 6-sided dice roll ($n=6, p=1/6$). They are referred to them as **Sample Spaces**, $\Omega$. Sample spaces are our inputs, probabilities are the output. The uncertainty that governs the probability of events before it has resolved into a single state is referred to as **Entropy**.

Using abstract algebra we can see how these simple Sample Spaces are Abelian groups. All of the outcomes are equallity likely, so the probability, $p$, of each state is equal to $1/n$ where $n$ is the number of possible outcomes, or the size of the group, $|G|$. These are useful in the intuition building of many real-world examples. These kinds of examples are referred to as **Uniform Distributions**. Since each of the events are equally likely to happen, it is said to have **Maximum Entropy**. In Maximum Entropy scenarios any certainty of the event is equallty uncertain, but the tradeoff is that you are assuming less about the event.

In more complex models the probability of these Sample Spaces are more randomly distributed. In any scenario, the sum of all probabilities is equal to 1, meaning a single probability is always $0 \leq p \leq 1$.

$$\sum_{x \in \Omega} p(x) = 1$$

More real-world examples form **Continuous** probability distributions. These events follow the mathematical definition of continuity. The probability of a continuous events uses functions, $f(x)$. Continuous distributions has a lot of overlap with discrete events, but have key differences. They have applications in machine learning, physics, finance, and biology.

$$\int_{\Omega} f(x)\,dx  = 1$$

## Central Limit Theorem

What happens if you keep combining more and more of these Abelian group states together? (e.g., rolling 10, 100, or 1,000 dice and adding them).This is where the Central Limit Theorem (CLT) emerges:You start with individual states mapping to identical real numbers (Uniform).As you combine them, the probabilities cluster heavily toward the identity/average states.The "randomly distributed" real numbers smooth out into a perfect, bell-shaped curve known as the Normal (Gaussian) Distribution.