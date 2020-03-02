from collections import deque
import queue

#List as queue
x = [1,2,3,5,6,7]
x.pop(0) #----1
x.pop()  #----7
x.append(8)

#deque
deq = deque([1,2,3,4,5])
deq.append(9) #extend
print(deq)
print(max(deq))
deq.appendleft(10) #extendleft
print(deq)
print(deq.popleft())
print(deq)
print(deq.pop())
print(deq)

#Queue FIFO
q = queue.Queue(maxsize=3)
print(q.qsize)
q.put('a')
q.put('b')
q.put('c')
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

#Stack LIFO
S = queue.LifoQueue(maxsize=6)
S.put('a')
S.put('b')
S.put('c')
print(S.get())
print(S.get())
print(S.get())
print(S.empty())
