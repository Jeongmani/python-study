n=int(input())
data=[0]*1001                   #n은 1000개까지 입력될 수 있으므로 n1~n1000까지 저장할 리스트를 만든다
data[1]=1                       #점화식의 1항을 미리 선언한다.
data[2]=2                       #점화식의 2항을 미리 선언한다.
for i in range(3,1001):
    data[i]=data[i-1]+data[i-2] #n3부터 성립되는 점화식을 이용해 n1000까지 계산한다.
print(data[n]%10007)            #이를 10007로 나눈 나머지를 출력한다.