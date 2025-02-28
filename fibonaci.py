def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n+1]

fib_numbers = fibonacci(10)
print(f"Fibonacci sequence from 0 to 10: {fib_numbers}")

