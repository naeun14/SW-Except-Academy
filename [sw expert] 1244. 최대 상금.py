def dfs(index, count):
    global result 
    if count == int(cnt):
        result = max(int("".join(data)),result) #why use max? 반복횟수까지 진행완료 했을때 지금까지 찾은 값 중 가장 큰 값 구하기
        return
    for now in range(index,len(data)):
        for next in range(now+1,len(data)):
            if data[now] <= data[next]:
                data[now],data[next] = data[next],data[now]
                dfs(now,count+1) #now에 해당되는 index에서 교환했다 가정했을 때 이후의 경우의 수
                data[now],data[next] = data[next],data[now] #다른 경우의 수 파악하기 위해 원상복귀
    
    if result == 0 and count < int(cnt): #현재상태가 가장 큰 값일 때 
        check = (int(cnt)-count) % 2 #짝수 번 반복시 현재상태랑 동일
        if check == 1: #홀수 번 반복시 1의자리 10의자리 숫자 교한(교환 시 최대값)
            data[-1],data[-2] = data[-2],data[-1]
        dfs(index,int(cnt))
                

T = int(input())
for test_case in range(1,T+1):
    data , cnt = input().split() #data와 반복횟수 입력받음
    data = list(data) #리스트로 저장
    result = 0 #출력 결과물 
    dfs(0,0) 
    
    print("#{} {}".format(test_case,result))