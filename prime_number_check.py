def prime_num_checker(number):
    is_prime = True
    for i in range(2, number -1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

n = int(input("Check this number: "))
prime_num_checker(number=n)