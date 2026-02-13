class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverseList(self):
        currentNum = self.head
        prevNum = None

        while currentNum is not None:
            nextNode = currentNum.next
            currentNum.next = prevNum
            prevNum = currentNum
            currentNum = nextNode
        
        self.head = prevNum

listLatihan = LinkedList()
listLatihan.insert_at_end(1)
listLatihan.insert_at_end(2)
listLatihan.insert_at_end(3)
listLatihan.insert_at_end(4)
listLatihan.insert_at_end(5)

print("----- Sebelum direverse -----")
listLatihan.display()

print("\n----- Setelah direverse -----")
listLatihan.reverseList()
listLatihan.display()
