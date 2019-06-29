# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def square_of_sum(first_n):
    first = 1
    last = first_n
    pairs = first_n / 2

    return (((first + last) * pairs) ** 2)


def sum_of_squares(first_n):
    result = 0
    for x in range(1,first_n + 1):
        result += x**2
    return result


def main():
    a = sum_of_squares(100)
    b = square_of_sum(100)
    result = a - b
    print(str(result))

if __name__ == '__main__':
    main()    
    
