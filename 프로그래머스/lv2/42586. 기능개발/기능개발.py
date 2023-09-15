import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days=deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    count=1
    k = days.popleft()
    while(days):
        j=days.popleft()
        if(j<=k):
            count+=1
        else:
            answer.append(count)
            count=1
            k=j
    if(sum(answer)!=len(progresses)):
        answer.append(count)
        return answer
    return answer