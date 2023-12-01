import re

text = input()
pattern = r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)
mirror_words_list = []
if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match[1] == match[2][::-1]:
            mirror_words_list.append(f'{match[1]} <=> {match[2]}')
else:
    print(f'No word pairs found!')

if mirror_words_list:
    print('The mirror words are:')
    print(', '.join(mirror_words_list))
else:
    print('No mirror words!')


