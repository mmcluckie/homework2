class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)
"""
Mason McLuckie
Homework 2
24/4/2024
"""



"""
1. postfixEval
Input type: a list of strings
Output type: a floating point number
"""
def postfixEval(expr):
    stack = Stack()
    output = 0
    for character in expr:
        if character.isdigit(): #First two statements help push numbers onto the stack
            stack.push(character)
        elif character[0] == '-' and character[1:].isdigit:  #This helps sort the negative numbers with limiting what is being read
            stack.push(-character[1:])
        else:
            op1 = stack.pop() #This portion deals with the actual math
            op2 = stack.pop()
            if character == '+':
                output = op1 + op2
            elif character == '-':
                output = op1 - op2
            elif character == '*':
                output = op1 * op2
            elif character == '/':
                output = op1 / op2
            stack.push(int(output))
    return int(stack.peek)



"""
2. validParentheses
Input type: a string
Output type: a Boolean
"""
def validParentheses(s):
    """Write your code here"""
    return



"""
3. reverseString
Input type: a string
Output type: a string
"""
def reverseString(s):
    """Write your code here"""
    return
        
        







