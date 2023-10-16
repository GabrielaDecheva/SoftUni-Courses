input_strings = input().split()
palindrome_word = input()
palindromes_list = []
for current_word in input_strings:
    if current_word == current_word[::-1]:
        palindromes_list.append(current_word)

print(palindromes_list)
print(f'Found palindrome {palindromes_list.count(palindrome_word)} times')
