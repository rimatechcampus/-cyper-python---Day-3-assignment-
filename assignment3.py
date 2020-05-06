# ! factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# ! prime number


def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


if __name__ == '__main__':

    while True:
        option = int(input(
            'Please enter your choice\n1-press #1 for getting the factorial \n2-press #2 for getting the prime number\n3-press #0 for exit  '))

        if option == 1:
            n = int(input("Input a number to compute the factiorial : "))

            factorialRes = factorial(n)
            print(f'the resutl is {factorialRes}')
            print('\n')

        elif option == 2:
            n = int(input('Input a number to compute the prime number '))
            primeRes = test_prime(n)
            print(f'the result is {primeRes}')
            print('\n')
        elif option == 0:
            break
        else:
            print('please enter correct choice ')
            print('\n')
