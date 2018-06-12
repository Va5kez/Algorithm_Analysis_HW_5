import sys
from src.fibonacci_dp import Fibonacci

def main():
    print ("Dijkstra\n")
    fibo = input("Number for fibonacci : ")
    print "Fibonacci of : ", fibo, " is " ,Fibonacci(fibo), "\n"
    print ("Bellman Ford\n")
    print ("Fibonaccio Dynamic Programming way\n")

if __name__ == "__main__":
    main()
