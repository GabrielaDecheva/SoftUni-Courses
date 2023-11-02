n = int(input())
my_dict = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in my_dict:
        my_dict[word].append(synonym)
    else:
        my_dict[word] = [synonym]

for word, synonym_list in my_dict.items():
    synonyms = ', '.join(synonym_list)
    print(f'{word} - {synonyms}')