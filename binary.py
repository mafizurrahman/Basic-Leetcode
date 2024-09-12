nums = [1, 5, 10, 1, 5, 5, 10]
total_count_ones = 0

for num in nums:
    binary_str = bin(num)[2:]  # Get binary representation without '0b' prefix
    count_ones = binary_str.count('1')
    total_count_ones += count_ones

print(total_count_ones)
