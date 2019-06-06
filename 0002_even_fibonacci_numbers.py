# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.



def main():
    fibs = [2]
    first = 1
    second = 2

    for x in range(100):
        next = first + second
        first = second
        second = next
    
        if next > 4000000:
            break

        if next % 2 == 0: # only store even valued terms
            fibs.append(next)

    print(sum(fibs))

if __name__ == '__main__':
    main()
