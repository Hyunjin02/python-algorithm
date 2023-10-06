def solution(sizes):
    answer = 0
    max_1=0
    max_2=0
    for i in range(len(sizes)):
        sizes[i].sort()
        if(max_1<sizes[i][0]):
            max_1=sizes[i][0]
        if(max_2<sizes[i][1]):
            max_2=sizes[i][1]
    answer=max_1*max_2
    return answer