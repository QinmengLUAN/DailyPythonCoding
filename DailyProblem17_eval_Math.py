"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
Here's the function signature:

def eval(expression):
  # Fill this in.

print eval('- (3 + ( 2 - 1 ) )')
# -4
"""
def eval(expression):
  # Fill this in.
  dic = ""
  dic[")"] = "("
  exp = expression.split()
  stack = []
  sym = 1
  for e in exp:
    if e != ")":
        stack.append(e)
    else:
        helper()

def helper(stack):
    tmp = 0
    while stack[-1] != "(":
        t = stack.pop()
        if t == "+":
            sym = 1
        elif t == "-":
            sym = -1
            



print eval('- (3 + ( 2 - 1 ) )')
# -4