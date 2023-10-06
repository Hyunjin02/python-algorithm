def solution(answers):
    answer = []
    a=[]
    b=[]
    b_i=1
    c=[]
    c_i=0
    c_j=3

    n_a=0
    n_b=0
    n_c=0
    for i in range(len(answers)):
        #a
        a.append(i%5+1)
        #b
        if(i%2==0):
            b.append(2)
        else:
            b.append(b_i)
            b_i+=1
            if(b_i==2):
                b_i+=1
            if(b_i==6):
                b_i=1
        #c
        if(c_i==0 or c_i==1):
            c.append(c_j)
            c_i+=1
        if(c_i==2):
            c_i=0
            if(c_j==3):
                c_j=1
            elif(c_j==5):
                c_j=3
            else:
                c_j+=1
                if(c_j==3):
                    c_j+=1

    for i in range(len(answers)):
        if(a[i]==answers[i]):
            n_a+=1
        if (b[i] == answers[i]):
            n_b += 1
        if (c[i] == answers[i]):
            n_c += 1

    maxN = max(n_a,n_b,n_c)
    if(maxN==n_a):
        answer.append(1)
    if(maxN==n_b):
        answer.append(2)
    if(maxN==n_c):
        answer.append(3)
    #print(a,b,c)
    return answer