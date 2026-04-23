#Develop a queue implementation using Python's deque from the collection’s module. Add a method, safe_dequeue (), that removes the front element from the queue. 
#If the queue is empty, the method should: Print a message as, "Queue is empty, cannot dequeue."

class Queue:

    def __init__(self):
        self.queue = []

#Push

    def push(self,item):
        self.queue.insert(len(self.queue),item)
        print(f"Item [{item}] has been Pushed Into the Queue")


#Safe Pop

    def safe_dequeue(self):
        if len(self.queue) != 0:
            item = self.queue.pop(0)
            print(f"Item [{item}] has been Dequeue'd from the Queue")
        else:
            print("Queue is Empty!\nCannot Dequeue!")

#Peek

    def peek(self):
        print(f"Queue Top = {self.queue[0]}")

#Is_Empty

    def is_Empty(self):
        if len(self.queue) == 0:
            print("The Queue is Empty")
        else:
            print("The Queue is not empty")


#Display

    def display(self):
        print(f"Queue = {self.queue}")

#------------------------------------------------

q1 = Queue()

q1.is_Empty()
q1.display()

q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)

q1.peek()
q1.display()

q1.safe_dequeue()
q1.safe_dequeue()
q1.safe_dequeue()

q1.display()