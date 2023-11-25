class Node:
    def __init__(self, data, prev, nxt):
        '''
            Node class represents a node in the doubly linked list.
        '''
        self.data= data
        self.prev= prev
        self.next= nxt

class DoublyLinkedList:
    def __init__(self, head:Node=None):
        '''
        DoublyLinkedList class represents a doubly linked list.
        '''
        self.head= head

    def insert_at_beginning(self, data):
        newNode= Node(data, None, None)

        if self.head == None:
            self.head= newNode
            return
        
        newNode.next= self.head
        self.head.prev = newNode
        self.head= newNode
        

    def insert_at_end(self, data):
        newNode= Node(data, None, None)

        if self.head == None:
            self.head = newNode
            return
        
        itr= self.head
    
        while itr.next:
            itr= itr.next

        newNode.prev = itr
        itr.next = newNode


    def insert_values(self, data_list):
        '''
        insert_values method inserts the values in the data list while clearing any previous data.

        Time Complexity: O(n) - Linear time, where n is the length of the data list, as it iterates through the list.
        Space Complexity: O(1) - Constant space, as it only uses a constant amount of space for variables.
        '''
        self.head = None
        if len(data_list) == 0:
            return self.head
    
        self.head= Node(data_list[0], None, None)
        if len(data_list) == 1:
            return self.head 

        start= self.head
        for i in range(1, len(data_list)):
            newNode= Node(data_list[i], start, None)
            start.next = newNode
            start = newNode

        


        


    def get_length(self):
        pass

    def remove_at(self, ind: int):
        pass

    def insert_at(self, index: int, data):
        pass
    

    def insert_after_value(self, data_after, data_to_insert):
        pass

    def remove_by_value(self, data):
        pass

    def print_dl(self):
        itr= self.head
        dt= ''
        while itr:
            pprev= itr.prev
            if pprev == None:
                pprev = "None"
            else:
                pprev= itr.prev.data
            
            nnxt= itr.next
            if nnxt == None:
                nnxt = "None"
            else:
                nnxt= itr.next.data

            dt += f'[{str(pprev)} # {str(itr.data)} # {str(nnxt)}]' + " --> "
            itr= itr.next

        dt += '//'

        print(dt)



if __name__ == '__main__':
    dll= DoublyLinkedList(Node(12, None, None))
    dll.print_dl()

    dll.insert_at_beginning(11)
    dll.print_dl()

    dll.insert_at_end(21)
    dll.print_dl()

    dll.insert_values([12, 11, 1111, 11, 21])
    dll.print_dl()

    x= 10
    y=x
    x=x-1
    print(y)