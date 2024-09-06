# input data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# program
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(2, numbers[i]+1):
        if numbers[i] % j > 0 or numbers[i] == j:
            is_prime = True
        elif numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime is False:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])

print(f'Простые числа: {primes}')
print(f'Не простые числа: {not_primes}')