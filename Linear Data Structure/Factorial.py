def factorial(n):
    if n == 2:
        return 1
    else:
      return n * factorial(n-1)

print(factorial(5))       

"""
Two Key Rules of Recursion
For a recursive function to work without crashing your computer, 
it must always have two things:
The Base Case: 
The condition that stops the recursion (like if n <= 1). Without this, 
it loops forever.
The Recursive Step: 
The line where the function calls itself, but with a smaller or modified input (like n - 1) 
so it moves closer to the base case.
"""
"When a function calls itself, it is called recursion"