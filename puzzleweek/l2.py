def collatz_length(n, memo={}):
    if n in memo:
        return memo[n]

    length = 1
    original_n = n

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n in memo:
            length += memo[n]
            break

        length += 1

    memo[original_n] = length
    return length

# Calculate the sequence lengths for the first 12031203 positive integers
sequence_lengths = [collatz_length(i) for i in range(1, 12031204)]

# Calculate the median sequence length
sequence_lengths.sort()
median_index = len(sequence_lengths) // 2
median_sequence_length = sequence_lengths[median_index]

print(f"The median sequence length is: {median_sequence_length}")



        

