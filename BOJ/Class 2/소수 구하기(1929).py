M,N = map(int, input().split())             #M과 N을 입력받아 M이상 N이하의 소수를 구한다

for i in range(M, N+1):                     #M~N까지 for문을 이용해 탐색한다.
    if i == 1:                              #1을 소수가 아니므로 지나간다.
        continue
    for j in range(2, int(i** 0.5)+1 ):     #소수는 대칭 형태임을 이용 (ex: 16은 1 2 4 8 16 의 대칭 형태로 약수를 가지고 있다) 따라서 제곱근까지만 확인을 하면 소수 인지 아닌지 확인할 수 있다
        if i%j==0:                          #만약 j로 나누어 떨어진다면 j는 i의 약수임으로 소수가 아니다
            break                           #이 아이디어를 통해 시간복잡도를 줄일 수 있다.
    else:                                   #이를 통해 걸러진 소수만 출력한다.
        print(i)