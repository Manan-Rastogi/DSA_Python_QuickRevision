# Stack using list

stk_ll= []

stk_ll.append(1)
stk_ll.append(2)
stk_ll.append(3)
stk_ll.append(4)
stk_ll.append(5)


print(stk_ll)

stk_ll.pop()
print(stk_ll)

stk_ll.append(5)

top= stk_ll[-1]

print(top)

'''
Problem with list as stack -        It's a dynamic array so Inserting(pushing) a new element will be done by allocation of new memory, 
coping all elements and so on..
'''

print('**********************************************************************************')

# Stack using Deque
from collections import deque

stack= deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)

stack.pop()

print(stack)






