def binarySequences(n):
    binary_sequence = [0, 0, 0, 1, 1, 1]

    if n < len(binary_sequence):
        return binary_sequence[n]
    else:
        for i in range(6, n+1):
            next_term = binary_sequence[i - 2] + binary_sequence[i - 3]
            binary_sequence.append(next_term)
    
    return binary_sequence[n]

n = int(input("Enter the number of terms: "))
print(f"The amount of binary sequences of length {n} that exists and begin with a 0, end with a 0, contain no two consecutive 0's, and contain no three consecutive 1's is {binarySequences(n)}.")
