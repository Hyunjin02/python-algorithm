import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
queue=deque()

for i in range(n):
    order_list=list(input().split())
    order=order_list[0]
    if(len(order_list)>1):
        x = order_list[1]

    if(order=="push"):
        queue.append(x)
    elif (order == "pop"):
        if (queue):
            print(queue[0])
            queue.popleft()
        else:
            print("-1")
    elif (order == "size"):
        print(len(queue))
    elif (order == "empty"):
        if (len(queue) == 0):
            print("1")
        else:
            print("0")
    elif(order=="front"):
        if(queue):
            print(queue[0])
        else:
            print("-1")
    elif(order=="back"):
        if (queue):
            print(queue[-1])
        else:
            print("-1")

