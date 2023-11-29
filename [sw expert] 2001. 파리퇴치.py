T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    n_list = [list(map(int,input().split())) for _ in range(N)]    
    result = []
    for row in range(N-M+1):
        for col in range(N-M+1):
            num = 0
            for i in range(row,M+row):
                for j in range(col,M+col):
                    num += n_list[i][j]
            result.append(num)
    print("#{} {}".format(test_case,max(result)))