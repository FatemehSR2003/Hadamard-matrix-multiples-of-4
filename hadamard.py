import numpy as np
import matplotlib.pyplot as plt

# Generate a Hadamard matrix of order n
def hadamard(n):
    # Check if n is a multiple of 4, as Hadamard matrices require n to be a multiple of 4
    if n % 4 != 0:
        print("Error: n must be a multiple of 4 to generate a Hadamard matrix!") 
        exit()
        
    # Initialize the Hadamard matrix with a 1x1 matrix    
    hadamard_matrix = np.array([[1]])
    
    # Recursively build the Hadamard matrix by taking the Kronecker product with the base 2x2 Hadamard matrix
    while hadamard_matrix.shape[0] < n:
        hadamard_matrix = np.kron(hadamard_matrix, np.array([[1, 1], [1, -1]]))
    
    # Return the Hadamard matrix of n order
    return hadamard_matrix[:n, :n]  

# Generate an identity matrix of order n
def identity_matrix(n):
    identity = np.eye(n)
    return identity

# Transpose of Hadamard matrix
def transpose_matrix(matrix):
    transpose = np.transpose(matrix)
    return transpose

# Plot Hadamard matrix 
def plot_matrix(matrix):
    plt.imshow(matrix, cmap="OrRd")
    plt.title(f"Hadamard Matrix Of Order ", fontweight="bold", color="darkred") 
    plt.show()

# Get the order of the Hadamard matrix from the user
n = int(input("Enter Order Of Hadamard Matrix: ")) 

# Generate the Hadamard matrix of n order
matrix = hadamard(n)

# Transpose the Hadamard matrix
transposed_matrix = transpose_matrix(matrix)

# Compute the product of the transposed Hadamard matrix and the original Hadamard matrix
result_HH = np.dot(transposed_matrix, matrix)

# Generate an identity matrix of the same order as the Hadamard matrix
identity = identity_matrix(n)
nI = n * identity

# Check if HH'= nI
if result_HH.all() == nI.all():
    print("HH'= nI ---> The Hadamard matrix is Correct")
    # Plot the Hadamard matrix
    plot_matrix(matrix)
