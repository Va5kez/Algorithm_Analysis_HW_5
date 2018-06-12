import sys
from src.fibonacci_dp import Fibonacci
from src.dikjstra import Dijkstra

def main():
    print ("Dijkstra\n")
    graph = {'s': {'a': 3, 'b': 2}, 'a': {'s': 4, 'b': 5, 'c': 9}, 'b': {'s': 5, 'a': 3, 'd': 3},
            'c': {'a': 3, 'd': 8, 'e': 5}, 'd': {'b': 2, 'c': 9, 'e': 6}, 'e': {'c': 4 , 'b': 5}}
    #Dijkstra(graph, 's', 'e')
    print ("Bellman Ford\n")
    print ("Fibonaccio Dynamic Programming way\n")
    fibo = int(input("Number for fibonacci : "))
    print ("Fibonacci of : ", fibo, " is " ,Fibonacci(fibo), "\n")

if __name__ == "__main__":
    main()
