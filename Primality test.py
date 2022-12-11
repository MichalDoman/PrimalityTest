def main():
    print("-----------------------------------------------------------")
    print("             Welcome to Primality Test App!")
    print("Type in a number that you want to examine, and press ENTER:")
    print("-----------------------------------------------------------")

    running = True
    while running:
        primality_test(int(take_user_input()))
        continue


def take_user_input():
    """Takes input from users and checks if it is a digit. If not make user type in again.

    :return: users input if it is a digit.
    """
    print('')
    input_number = input('Your number: ')
    while not input_number.isdigit():
        input_number = input("This is not a valid input. Please, type in a natural number: ")
        continue

    return input_number


def primality_test(number):
    x = 1
    factors = [1, number]
    prime = True

    if number == 0:
        print('Zero is not a prime number, since it can be divided by every number there is.')
        print('However, it is neither prime nor composite, since composite numbers have a FINITE number of factors.')
        prime = False
        return prime

    if number == 1:
        print("In modern mathematics, 1 IS NOT considered a prime number.")
        print("It can only be divided by itself.")
        prime = False
        return prime

    while x ** 2 <= number:
        x += 1
        if number % x == 0:
            # Finding all the factors:
            if x not in factors:
                factors.append(x)
            y = int(number / x)
            if y not in factors:
                factors.append(y)
            prime = False
            # 2 is the only prime number that goes through the above if statement:
            if number == 2:
                prime = True

    if prime:
        print(f"{number} IS a prime number,")
    else:
        print(f"{number} IS NOT a prime number, it is composite.")

    factors.sort()
    number_of_divisors = len(factors)
    print(f"It can be divided by {factors}.")
    print(f"So, there are {number_of_divisors} factors.")
    if not prime:
        closest_small_prime = find_prime_number(number, '-')
        closest_big_prime = find_prime_number(number)
        print(f'The closest prime number smaller than {number}, is {closest_small_prime}.')
        print(f'And the closest bigger, is {closest_big_prime}.')

    return prime


def find_prime_number(number, sign=''):
    prime = 0
    prime = False

    if sign:
        modifier = -1
    else:
        modifier = 1

    if number % 2 == 0:
        number += (1 * modifier)
    else:
        number += (2 * modifier)

    while not prime:
        x = 1
        prime = True
        while x ** 2 <= number:
            x += 1
            if number % x == 0:
                prime = False
                number += (2 * modifier)
                break
            return number


if __name__ == '__main__':
    main()
