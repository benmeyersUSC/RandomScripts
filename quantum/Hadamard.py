import numpy as np

def print_qubit_state(state, name):
    """Pretty print a qubit state"""
    print(f"{name} state:")
    print(f"Amplitude |0⟩: {state[0]:.4f}")
    print(f"Amplitude |1⟩: {state[1]:.4f}")
    print(f"Probability |0⟩: {np.abs(state[0])**2:.4f}")
    print(f"Probability |1⟩: {np.abs(state[1])**2:.4f}")
    print()

def main():
    # Define the Hadamard gate
    H = (1 / np.sqrt(2)) * np.array([
        [1,  1],
        [1, -1]
    ])

    # Define initial qubit states
    zero_state = np.array([1, 0])   # |0⟩ state
    one_state = np.array([0, 1])    # |1⟩ state

    # Print the Hadamard gate matrix
    print("Hadamard Gate Matrix:")
    print(H)
    print()

    # Visualize transformation of |0⟩ state
    print("Transforming |0⟩ state:")
    print_qubit_state(zero_state, "Initial |0⟩")
    zero_transformed = np.dot(H, zero_state)
    print_qubit_state(zero_transformed, "After Hadamard |0⟩")

    # Visualize transformation of |1⟩ state
    print("Transforming |1⟩ state:")
    print_qubit_state(one_state, "Initial |1⟩")
    one_transformed = np.dot(H, one_state)
    print_qubit_state(one_transformed, "After Hadamard |1⟩")

if __name__ == "__main__":
    main()