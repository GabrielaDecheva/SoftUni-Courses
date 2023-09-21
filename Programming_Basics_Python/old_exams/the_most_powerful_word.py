import math

input_line = input()
total_sum = 0
powerful_word = ''
while input_line != 'End of words':
    word = input_line
    sum_symbols = 0
    for i in range(len(word)):
        sum_symbols += ord(word[i])
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y'\
            or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        sum_symbols = sum_symbols * len(word)
    else:
        sum_symbols = math.floor(sum_symbols / len(word))
    if sum_symbols > total_sum:
        powerful_word = word
        total_sum = sum_symbols
    input_line = input()

print(f"The most powerful word is {powerful_word} - {total_sum}")

