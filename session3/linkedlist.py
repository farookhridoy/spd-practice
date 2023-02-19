# A linked list is a linear data structure that includes a series of connected nodes.
# Here, each node stores the data and the address of the next node. For example,


# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, new_item):
        node = Node(new_item)
        node.next = self.head
        self.head = node
        return self.head

    def __str__(self):
        output = []
        curr = self.head
        while (curr):
            output.append(curr.data)
            curr = curr.next
        return str(output)

    def delete(self, item):
        # for case #1 : if need to delete head then
        if self.head.data == item:
            self.head = self.head.next
            return self.head

        # for case #2 : if item have in the list then delete this
        prev = None
        curr = self.head
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        # for case #3 if no data found in list then check
        if curr:
            prev.next = curr.next
        return self.head
    # remove nth item form the end of linked list

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


llist = LinkedList()
llist.add(10)
llist.add(4)
llist.add(16)
llist.add(19)
llist.removeNthFromEnd(llist.head, 2)
print(llist)
