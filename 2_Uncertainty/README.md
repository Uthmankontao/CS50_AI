# CS50AI — Uncertainty

This repository contains my work for the **Uncertainty** chapter of [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/weeks/2/).

It includes both the lecture code samples and the two main projects: **PageRank** and **Heredity**.

---

## 📂 Repository Structure

### 1. `lecture/`
This folder contains **code samples** from the lectures and notes of the *Uncertainty* chapter.  
It includes:
- Simple implementations of conditional probability.
- Demonstrations of probability distributions.
- Small Bayesian Networks examples.
- Markov and Hidden Markov Models demos.

👉 Goal: practice probability manipulations before implementing the projects.

---

### 2. `pagerank/`
Implementation of the **PageRank** algorithm, originally used by Google to rank web pages.

Two approaches are implemented:
1. **Sampling (Random Surfer Model)**: approximation using a random walker.
2. **Iteration**: recursive computation of probabilities until convergence.

### 3. `heredity/`

Implementation of a probabilistic AI to estimate the probability that a person has a certain number of copies of a gene and whether they express a related genetic trait.

The model is based on a Bayesian Network, accounting for:

1. The probability of gene transmission from parents.

2. Mutation probability.

3. Probability of expressing the trait given gene copies.