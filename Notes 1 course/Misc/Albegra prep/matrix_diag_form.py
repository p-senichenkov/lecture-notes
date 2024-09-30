#!/bin/python3

import numpy

def print_matrix(m: numpy.array) -> None:
    for row in m:
        for elem in row:
            print(elem, end=' ')
        print()

with open('matrix.txt', 'r') as file:
    lines = file.readlines()
    arrays = [numpy.fromstring(line, sep=' ', dtype=numpy.int32) for line in lines]

matrix = numpy.array(arrays)

print('Got matrix:')
print_matrix(matrix)

result = numpy.linalg.eig(matrix)

EIG_SIZE = len(result.eigenvalues)
diag_lines = []
for i in range(EIG_SIZE):
    line = []
    for j in range(i):
        line.append(0)
    line.append(result.eigenvalues[i])
    for j in range(i + 1, EIG_SIZE):
        line.append(0)
    diag_lines.append(line)
diag_matrix = numpy.array(diag_lines)
print('Diagonal form: ')
print_matrix(diag_matrix)

VECT_NUM = len(result.eigenvectors)
VECT_LEN = len(result.eigenvectors[0])
trans_lines = []
for line_num in range(VECT_LEN):
    line = []
    for elem_num in range(VECT_NUM):
        line.append(result.eigenvectors[elem_num][line_num])
    trans_lines.append(line)
trans_matrix = numpy.array(trans_lines)
print('Transition matrix:')
print_matrix(trans_matrix)
