# Function for the recursive method
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

n = int(input("Enter how many numbers you want: "))

# 1. Iterative Method (Using a loop)
print("Iterative: ", end="")
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print() # Just moves to a new line

# 2. Recursive Method (Function calling itself)
print("Recursive: ", end="")
for i in range(n):
    print(fib_rec(i), end=" ")
'''
Practical 1: Fibonacci (Recursive and Non-Recursive)
Aim: Implement recursive and non-recursive Fibonacci and analyze their time and space complexity.
Theory: The Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, ... where each term is the sum of the two before it.
F(n) = 0 if n = 0, F(n) = 1 if n = 1, F(n) = F(n-1) + F(n-2) if n > 1.
• Iterative: a loop keeps the last two terms and adds them (dynamic programming style).
• Recursive: the function calls itself for n-1 and n-2. The same subproblems are recomputed many times, so it is slow.
Algorithm (iterative):
1. a = 0, b = 1; print a, b.
2. Repeat for i = 3 to n: c = a + b; print c; a = b; b = c.
Algorithm (recursive): if n is 0 or 1, return n; else return fib(n-1) + fib(n-2).
Version
Time
Space
Iterative
O(n)
O(1)
Recursive
O(2^n)
O(n) (call stack depth)
'''
