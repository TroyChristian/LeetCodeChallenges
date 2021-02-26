def fibonacci_memo(input_value):
    fibonacci_cache = {}
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    if input_value == 1:
        value = 1
    elif input_value == 2:
        value = 1
    elif input_value > 2:
        value = fibonacci_memo(input_value - 1) + fibonacci_memo(input_value - 2)
    fibonacci_cache[input_value] = value
    return value

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
##    index = 0
##    fibs = [0,1]
##    while len(fibs) < n:
##        next_num = fibs[index] + fibs[index+1]
##        fibs.append(next_num)
##        index += 1
    n_minus_one = fib(n-1)
    n_minus_two = fib(n-2)
            
    return n_minus_one + n_minus_two

print(fib(8))
