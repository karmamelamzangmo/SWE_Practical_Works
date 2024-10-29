class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed

#exercise1.  Evaluating Postfix Expressions

def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():  # If the token is an operand
            stack.push(int(token))
        else:  # The token is an operator
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)
    
    return stack.pop()  # The result is the last item in the stack

# Test the function
print(evaluate_postfix("3 4 + 2 * 7 /"))  # Should print 2.0

#exercise2.  Implementing a Queue Using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.peek()
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

# Test the QueueUsingStacks
queue_stacks = QueueUsingStacks()
queue_stacks.enqueue(1)
queue_stacks.enqueue(2)
queue_stacks.enqueue(3)
print(queue_stacks.dequeue())  # Should print 1
print(queue_stacks.front())  # Should print 2
print(queue_stacks.is_empty())  # Should print False

#exercise3. Basic Task Scheduler Using a Queue

class TaskScheduler:
    def __init__(self):
        self.task_queue = Queue()

    def add_task(self, task):
        self.task_queue.enqueue(task)

    def process_tasks(self):
        while not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            print(f"Processing task: {task}")

# Test the TaskScheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.process_tasks()

#exercise4. Converting Infix Expressions to Postfix

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []
    
    for token in expression.split():
        if token.isalnum():  # If the token is an operand
            output.append(token)
        elif token in precedence:  # The token is an operator
            while (not stack.is_empty() and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)

# Test the function
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # Should print "3 4 2 * 1 5 - + /"