widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

s = "aabaaba"

newline = 1
line_width = 0

for char in s:
    char_width = widths[ord(char) - ord('a')]

    if char_width + line_width > 100:
        newline += 1
        line_width = char_width
    else:
        line_width += char_width

print([newline, line_width])
