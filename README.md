# Hadamard-matrix-multiples-of-4
Displaying the Hadamard matrix of multiples of 4 graphically

▎Overview

This Python script generates a Hadamard matrix of a specified order  n  (where  n  must be a multiple of 4), computes its transpose, and verifies the property that the product of the Hadamard matrix and its transpose equals  nI , where  I  is the identity matrix of the same order. The script also visualizes the generated Hadamard matrix using matplotlib.

▎Requirements

To run this script, you need to have the following Python libraries installed:

• numpy

• matplotlib

You can install these libraries using pip if you haven't already:

pip install numpy matplotlib


▎Functions

▎1. hadamard(n)

Generates a Hadamard matrix of order  n .

Parameters:

• n (int): The order of the Hadamard matrix. Must be a multiple of 4.

Returns:

• A Hadamard matrix of size  n × n .

▎2. identity_matrix(n)

Generates an identity matrix of order  n .

Parameters:

• n (int): The order of the identity matrix.

Returns:

• An identity matrix of size  n × n .

▎3. transpose_matrix(matrix)

Computes the transpose of a given matrix.

Parameters:

• matrix (numpy.ndarray): The matrix to be transposed.

Returns:

• The transposed matrix.

▎4. plot_matrix(matrix)

Plots a visual representation of the given matrix using a heatmap.

Parameters:

• matrix (numpy.ndarray): The matrix to be plotted.

▎Usage

1. Run the script in a Python environment.

2. When prompted, enter an integer value for the order of the Hadamard matrix. Ensure that this value is a multiple of 4.

3. The script will generate and display the Hadamard matrix, verify the relationship  HH' = nI , and plot the Hadamard matrix.

▎Example

Enter Order Of Hadamard Matrix: 8


▎Important Notes

• The script checks if the input order  n  is a multiple of 4. If not, it prints an error message and exits.

• The generated Hadamard matrix is visualized using a color map for better understanding.

• The verification step checks if the product of the Hadamard matrix and its transpose equals  nI . If true, it confirms that the generated Hadamard matrix is correct.

▎License

This project is licensed under the MIT License - see the LICENSE file for details.

▎Acknowledgments

This implementation is based on properties of Hadamard matrices and their applications in various fields such as signal processing and error correction codes.
