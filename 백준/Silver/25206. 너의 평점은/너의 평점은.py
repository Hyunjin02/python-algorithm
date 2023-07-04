x=[]
score=[]
for i in range(0,20):
    k=input()
    p=list(map(str,k.split()))
    x.append(float(p[1]))
    score.append((p[2]))
for i in range(0,20):
    grade=0.0
    if(score[i][0]=='A'):
        grade=4
    elif(score[i][0]=='B'):
        grade=3
    elif (score[i][0] == 'C'):
        grade = 2
    elif (score[i][0] == 'D'):
        grade = 1
    elif (score[i][0] == 'E'):
        grade = 0
    elif(score[i][0]=='P'):
        x[i]=0
    if (len(score[i])>1):
        if(score[i][1] == '+'):
            grade = grade+0.5
    score[i]=grade

sumOfScore=0.0
for i in range(0,20):
    sumOfScore=sumOfScore+float(score[i])*float(x[i])
print(sumOfScore/sum(x))