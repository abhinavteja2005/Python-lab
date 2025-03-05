# Stack implementation using a list
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)  # Output: [10, 20, 30]

# Pop elements from the stack
top_element = stack.pop()
print("Popped element:", top_element)  # Output: 30
print("Stack after popping:", stack)   # Output: [10, 20]

# Peek (view the top element without removing it)
if stack:
    print("Top element:", stack[-1])  # Output: 20
else:
    print("Stack is empty")

# Check if the stack is empty
print("Is stack empty?", len(stack) == 0)  # Output: False


# Queue implementation using deque

from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueues:", list(queue))  # Output: [10, 20, 30]

# Dequeue elements
front_element = queue.popleft()
print("Dequeued element:", front_element)   # Output: 10
print("Queue after dequeuing:", list(queue))  # Output: [20, 30]

# Peek (view the front element without removing it)
if queue:
    print("Front element:", queue[0])  # Output: 20
else:
    print("Queue is empty")

# Check if the queue is empty
print("Is queue empty?", len(queue) == 0)  # Output: False

# Priority queue implementation using heapq
import heapq

priority_queue = []

# Add elements with priorities
heapq.heappush(priority_queue, (2, "Task 2"))  # (priority, value)
heapq.heappush(priority_queue, (1, "Task 1"))
heapq.heappush(priority_queue, (3, "Task 3"))
print("Priority queue:", priority_queue)  # Output: [(1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3')]

# Remove elements in priority order
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Processing {task} with priority {priority}")
    # Output: Task 1, Task 2, Task 3 (in order of priority)
