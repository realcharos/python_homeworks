def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")