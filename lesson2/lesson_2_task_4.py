def fizz_buzz(n):
    """Печатает Fizz/Buzz/FizzBuzz для чисел от 1 до n (n приводится к int)."""
    n = int(n)
    if n < 1:
        return
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(17)
