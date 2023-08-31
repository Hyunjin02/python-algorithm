import sys

input = sys.stdin.readline
arr = []
while(True):
    str1 = input().rstrip()
    flag="yes"
    if(str1== '.'):
        break;
    else:
        for i in str1:
            if(i=="(" or i=="["):
                arr.append(i)
            elif(i==")" or i=="]"):
                if(len(arr)==0):
                    flag="no"
                    break;
                else:
                    if(i==")"):
                        if(arr.pop()!="("):
                            flag="no"
                            break;
                    elif(i=="]"):
                        if (arr.pop() != "["):
                            flag = "no"
                            break;

        if(len(arr)!=0):
            flag="no"
        print(flag)
        while(len(arr)!=0):
            arr.pop()
