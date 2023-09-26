number = int(input())
prime_number = True

if number <= 1:
    prime_number = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime_number = False
            break

print(prime_number)
