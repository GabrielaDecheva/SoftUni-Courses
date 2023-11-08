results = {}
command = input()
while command != 'exam finished':
    if 'banned' not in command:
        user, language, points = command.split('-')
        if language not in results.keys():
            results[language] = {}
            results[language]['submissions'] = 0
            results[language][user] = int(points)
            results[language]['submissions'] += 1
        else:
            if user in results[language].keys():
                for key, value in results.items():
                    for nested_key, nested_value in value.items():
                        if nested_key == user and nested_value < int(points):
                            results[key][nested_key] = int(points)
                results[language]['submissions'] += 1
            else:
                results[language][user] = int(points)
                results[language]['submissions'] += 1

    else:
        user, banned = command.split('-')
        for key, value in results.items():
            for nested_key, nested_value in value.items():
                if nested_key == user:
                    results[key][nested_key] = 'banned'
    command = input()

print('Results:')
for key, value in results.items():
    for nested_key, nested_value in value.items():
        if nested_value != 'banned' and nested_key != 'submissions':
            print(f'{nested_key} | {nested_value}')

print('Submissions:')
for key, value in results.items():
    for nested_key, nested_value in value.items():
        if nested_key == 'submissions':
            print(f'{key} - {results[key][nested_key]}')


