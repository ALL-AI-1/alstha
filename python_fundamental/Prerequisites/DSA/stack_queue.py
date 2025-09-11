from collections import deque
# from ctypes import sizeof
dq=deque()

#stack

dq.append(1)
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)

print(dq)
dq.pop()
print(dq)

print(dq[-1])

print(dq.count(1))

dq.clear()
print(dq)


#queue
dq=deque()

dq.insert(0,1)
dq.insert(0,1)
dq.insert(0,2)
dq.insert(0,3)
dq.insert(0,4)

print(dq)
dq.pop()
print(dq)

print(dq[-1])

print(dq.count(1))

dq.clear()
print(dq)