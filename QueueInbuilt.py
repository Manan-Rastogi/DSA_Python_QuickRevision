# Queue using List

qu= []
qu.insert(0, 1)
qu.insert(0, 2)
qu.insert(0, 3)
qu.insert(0, 4)

print(qu)

qu.pop()

print(qu)

'''
Problem with list as queue -        It's a dynamic array so Inserting a new element will be done by allocation of new memory, 
coping all elements and so on..
'''

print('######################################################')

# Queue using deque
from collections import deque

q= deque()

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)

print(q)

q.pop()

print(q)

