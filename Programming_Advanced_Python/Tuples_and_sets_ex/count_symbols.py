occurrences = {}

for symbol in input():
    occurrences[symbol] = occurrences.get(symbol, 0) + 1
for symbol, count in sorted(occurrences.items()):
    print(f"{symbol}: {count} time/s")

# 2

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")