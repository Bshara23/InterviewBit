

def fizzBuzz(A):

    def helper(x):
        if x % 5 == 0 and x % 3 == 0:
            return "FizzBuzz"
        elif x % 3 == 0:
            return "Fizz"
        elif x % 5 == 0:
            return "Buzz"
        return x

    B = [i for i in range(1, A + 1)]
    return list(map(helper, B))

print(fizzBuzz(5))