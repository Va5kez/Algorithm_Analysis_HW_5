def Fibonacci(number):
    fibo_array = [0, 1]
    if number < 2:
        return fibo_array[number]
    for x in range(2, number + 1):
        fibo_array.append(fibo_array[x-1] + fibo_array[x-2])
    return fibo_array[number]
