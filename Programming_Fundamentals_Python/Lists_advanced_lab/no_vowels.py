text = input()

new_text = [symbol for symbol in text if symbol.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(new_text))