#Name of Assignment:  Create a program that implements a stack using a list. Add a method, safe_pop(), which safely removes the top element from the stack. 
#If the stack is empty, the method should handle this condition by:
#- Printing a message as "Stack is empty, nothing to pop."
#- Returning None.


class Stack:

    def __init__(self):
        self.stack = []

#Push

    def push(self,item):
        self.stack.append(item)
        print(f"Item [{item}] has been pushed onto the stack")

#Pop / Safe_Pop

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty!\nCannot Pop!")
        else:
            item = self.stack.pop()
            print(f"Item [{item}] has been successfully popped from the Stack")

#Peek 

    def peek(self):
        top = self.stack[-1]
        print(f"Stack[Top] = {top}")


#Is_Empty

    def is_Empty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is not Empty")


#-----------------------------------------------------

stack1 = Stack()
stack1.is_Empty()

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

stack1.is_Empty()

stack1.peek()

stack1.safe_pop()
stack1.safe_pop()
stack1.safe_pop()
stack1.safe_pop()

stack1.is_Empty()