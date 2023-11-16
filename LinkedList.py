class Node:
    def __init__(self, data=None, next=None):
        '''
        Node class represents a node in the linked list.
        '''
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        '''
        LinkedList class represents a singly linked list.
        '''
        self.head = None

    def insert_at_beginning(self, data):
        '''
        insert_at_beginning method inserts the data at the beginning of the linked list.

        Time Complexity: O(1) - Constant time, as it involves a fixed number of operations regardless of the size of the linked list.
        Space Complexity: O(1) - Constant space, as a new node is created, but it doesn't depend on the size of the linked list.
        '''
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        '''
        insert_at_end method inserts the data at the end of the linked list.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it iterates through the list to find the end.
        Space Complexity: O(1) - Constant space, as a new node is created.
        '''
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def insert_values(self, data_list):
        '''
        insert_values method inserts the values in the data list while clearing any previous data.

        Time Complexity: O(n) - Linear time, where n is the length of the data list, as it iterates through the list.
        Space Complexity: O(1) - Constant space, as it only creates nodes for each element in the data list.
        '''
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        '''
        get_length method returns the length of the linked list.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it iterates through the list to count nodes.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for the count variable.
        '''
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1

        return count

    def remove_at(self, ind: int):
        '''
        remove_at method removes the element at index ind.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it may need to traverse the list to the specified index.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        l = self.get_length()
        if ind < 0 or ind >= l:
            print(f'Linked List of Length: {l}. Kindly choose the index appropriately.')
            return

        indx = ind
        if ind == 0:
            print(f'{self.head.data} removed from index {indx}')
            self.head = self.head.next
            return

        itr = self.head
        prev = itr
        while ind > 0:
            prev = itr
            itr = itr.next
            ind -= 1

        nxt = itr.next
        prev.next = nxt

        print(f'{itr.data} removed from index {indx}')

    def insert_at(self, index: int, data):
        '''
        insert_at method inserts the data at the specified index.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it may need to traverse the list to the specified index.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        '''
        insert_after_value method inserts data_to_insert after the first occurrence of data_after.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it may need to traverse the list to find the data_after.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        if self.get_length() == 0:
            print('Empty List.')
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                break
            itr = itr.next

        nxt = itr.next
        itr.next = Node(data_to_insert, nxt)

    def remove_by_value(self, data):
        '''
        Removes the first node that contains the specified data.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it may need to traverse the list to find the data.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        if self.get_length() == 0:
            return

        if self.get_length() == 1:
            if self.head.data == data:
                self.head = None
                return

        itr = self.head
        prev = itr
        while itr:
            if itr.data == data:
                break
            prev = itr
            itr = itr.next

        prev.next = itr.next

    def print(self):
        '''
        print method prints the linked list.

        Time Complexity: O(n) - Linear time, where n is the length of the linked list, as it iterates through the list to print nodes.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        if self.head is None:
            print('List is Empty!')
            return

        itr = self.head
        ll_str = ''

        while itr:
            ll_str += str(itr.data) + ' --> '
            itr = itr.next

        print(ll_str + " //")


if __name__ == '__main__':
    ll = LinkedList()
    ll.print()

    ll.insert_at_beginning(1)
    ll.print()

    ll.insert_at_beginning(19)
    ll.print()

    ll.insert_at_end(1001)
    ll.insert_at_end(1101)
    ll.insert_at_end(1201)
    ll.insert_at_end(1301)
    ll.insert_at_end(1501)
    ll.insert_at_end(1701)
    ll.insert_at_end(1801)
    ll.print()

    print('Length= ', ll.get_length())

    ll.remove_at(90)

    ll.remove_at(4)
    ll.remove_at(0)
    ll.remove_at(6)
    ll.print()

    print('Length= ', ll.get_length())

    ll.insert_at(2, 92)
    ll.insert_at(0, 0)
    ll.print()

    # ll.insert_at(100, 9)

    print('Length= ', ll.get_length())

    ll.insert_after_value(1701, 'After 1701')
    ll.print()

    ll.remove_by_value(1701)
    ll.print()
