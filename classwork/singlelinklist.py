# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    # Insert at specific position (0-based index)
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        temp = self.head
        
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node

    # Traverse (print list)
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Delete by value
    def delete(self, key):
        temp = self.head

        # If head needs to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_beginning(5)
    sll.insert_at_position(15, 2)

    print("Linked List:")
    sll.traverse()

    print("After deleting 20:")
    sll.delete(20)
    sll.traverse()