def solution(arr):
    my_dict = {}
    count = []
    j=1
    for i in range(len(arr)):
        type = arr[i][1]
        if(type in my_dict):
            my_dict[type]+=1
        else:
            my_dict[type]=1
    for key in my_dict:
        count.append(my_dict[key])

    for i in range(len(count)):
        j *= (count[i]+1)
    return j-1