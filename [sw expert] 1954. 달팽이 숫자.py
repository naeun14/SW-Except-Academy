T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0]*N for _ in range(N)] #0으로 초기화
    count = 1  #배열 입력값 
    dir = 0 #0:우 1:하 2:좌 3:상 
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    row,col = 0,0
    while count <= N*N: #n*n 배열 모두 채우기 
        if (0 <= row < N and 0 <= col < N) and snail[row][col] == 0: #정상 범위 내라면 
            snail[row][col] = count
            count += 1
        else:
            row -= dr[dir]
            col -= dc[dir]
            dir = (dir+1)%4
            
        row += dr[dir]
        col += dc[dir]
        
    print("#{}".format(T))
    for r in snail:
        print(*r)  #*를 붙이면 [] 떼고 출력 가능
    
