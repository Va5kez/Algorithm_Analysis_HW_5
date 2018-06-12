import sys
from src.fibonacci_dp import Fibonacci

def main():
    print ("Dijkstra\n")
    print ("Bellman Ford\n")
    print ("Fibonaccio Dynamic Programming way\n")
    fibo = input("Number for fibonacci : ")
    print "Fibonacci of : ", fibo, " is " ,Fibonacci(fibo), "\n"

if __name__ == "__main__":
    main()
