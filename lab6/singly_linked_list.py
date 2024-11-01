class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
# Initialize the linked list and append elements
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Display the list
ll.display()  # Expected output: 1 -> 2 -> 3

# Insert element at position 1
ll.insert(4, 1)
ll.display()  # Expected output: 1 -> 4 -> 2 -> 3

# Delete element with data = 2
ll.delete(2)
ll.display()  # Expected output: 1 -> 4 -> 3

# Search for elements
print(ll.search(4))  # Expected output: 1
print(ll.search(5))  # Expected output: -1

# Reverse the linked list
ll.reverse()
ll.display()  # Expected output: 3 -> 4 -> 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        first = self.head
        second = other.head

        while first and second:
            if first.data < second.data:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next

        tail.next = first or second
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list
# Initialize the linked list and append elements
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Test find_middle method
print("Middle element:", ll.find_middle())  # Expected output: Middle element: 2

# Test has_cycle method (without cycle)
print("Has cycle:", ll.has_cycle())  # Expected output: Has cycle: False

# Add a cycle for testing (manually)
ll.head.next.next.next = ll.head  # Creates a cycle
print("Has cycle:", ll.has_cycle())  # Expected output: Has cycle: True
ll.head.next.next.next = None  # Remove cycle for further tests

# Add duplicate elements
ll.append(2)
ll.append(3)
ll.remove_duplicates()
ll.display()  # Expected output: 1 -> 2 -> 3 (duplicates removed)

# Test merge_sorted with another sorted linked list
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_ll = ll1.merge_sorted(ll2)
merged_ll.display()  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
