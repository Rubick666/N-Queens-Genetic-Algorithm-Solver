# Benchmarks & Experimental Results

This document outlines the quantitative results of the N-Queens Genetic Algorithm under various configurations.

## 1. Parameter Sensitivity (N=8)

| Mutation Rate | Crossover Rate | Average Generations | Success Rate |
| :--- | :--- | :--- | :--- |
| 20% | 50% | 166.25 | 100% |
| 20% | 100% | 76.7 | 100% |
| 30% | 50% | 195.4 | 100% |
| 30% | 100% | 215.0 | 100% |
| 50% | 50% | 87.5 | 100% |
| 50% | 100% | 96.25 | 100% |

*Observation: Higher crossover rates generally improve convergence speed, though the problem is easy enough that results vary due to initial random population.*

## 2. Crossover Strategy Exploration (N=8, 50 Runs)

| Crossover Method | Average Convergence Speed (Generations) |
| :--- | :--- |
| Cut and Fill | 101.58 |
| PMX | 78.0 |
| 2-Cut | 97.22 |
| 3-Cut | 103.28 |

*Observation: PMX provides the fastest average convergence. Increasing the number of cuts in the 2-cut/3-cut methods did not significantly affect performance.*

## 3. Survival Strategy Comparison (N=8)

| Strategy | Runs | Average Generations to Solution |
| :--- | :--- | :--- |
| Generational Replacement | 3 | 3.0 |
| Elitism | 3 | 2.0 |

*Observation: Elitism showed slightly faster and more stable convergence by preserving the top 2 individuals.*

## 4. Scalability Study

| N (Queens) | Average Generations (10 runs) |
| :--- | :--- |
| 8 | ~80 |
| 10 | 165.2 |
| 12 | N/A (Runtime exceeded limits) |
| 20 | N/A (Runtime exceeded limits) |

*Observation: While N=10 is solvable, N=12 and N=20 require significant optimization (e.g., O(N) conflict calculation) to prevent runtime bottlenecks.*