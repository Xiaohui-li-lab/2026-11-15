#!/usr/bin/env python3
"""
Concept Decomposition-Recombination Benchmark (CDRB)
Simulates classical vs. quantum operation counts for conceptual recombination.
"""

import numpy as np
import matplotlib.pyplot as plt

def classical_ops(n, k=1.0):
    """Classical 0/1 bit-based decomposition-recombination."""
    return k * (2.0 ** n)

def quantum_ops(n, k=1.0):
    """Quantum superposition-based decomposition-recombination."""
    return k * (2.0 ** (n / 2.0))

def constraint_entropy(rigidities, eps=1e-12):
    """
    Compute constraint entropy from a vector of concept rigidities in [0,1].
    C = -sum r_i * log(r_i)
    """
    r = np.clip(rigidities, eps, 1.0)
    return -np.sum(r * np.log(r))

def decomposition_potential(n_units, n_max, success_rates):
    """
    Compute decomposition potential.
    D = sum (n_j / N_max) * f_j
    """
    n_units = np.asarray(n_units)
    success_rates = np.asarray(success_rates)
    return np.sum((n_units / n_max) * success_rates)

if __name__ == "__main__":
    n_values = np.arange(1, 51)
    k = 1.0

    O_classical = classical_ops(n_values, k)
    O_quantum = quantum_ops(n_values, k)

    # Save benchmark data
    np.savetxt(
        "cdrb_benchmark_data.csv",
        np.column_stack([n_values, O_classical, O_quantum]),
        delimiter=",",
        header="n,classical_ops,quantum_ops",
        comments=""
    )

    # Plot
    plt.figure(figsize=(10, 6))
    plt.semilogy(n_values, O_classical, label=r"Classical $O=2^n$", linewidth=2)
    plt.semilogy(n_values, O_quantum, label=r"Quantum $O=2^{n/2}$", linewidth=2)
    plt.xlabel("Number of semantic units $n$", fontsize=12)
    plt.ylabel("Normalized operation count", fontsize=12)
    plt.title("CDRB: Classical vs. Quantum Conceptual Recombination", fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("cdrb_benchmark.png", dpi=300)
    plt.show()

    # Demonstration of constraint entropy and decomposition potential
    rigidities = np.array([0.95, 0.90, 0.85, 0.20, 0.15])  # high rigidity for first 3 concepts
    print(f"Constraint entropy: {constraint_entropy(rigidities):.3f}")

    n_units = [8, 6, 10, 4, 5]
    n_max = 20
    success_rates = [0.9, 0.8, 0.85, 0.95, 0.9]
    print(f"Decomposition potential: {decomposition_potential(n_units, n_max, success_rates):.3f}")
