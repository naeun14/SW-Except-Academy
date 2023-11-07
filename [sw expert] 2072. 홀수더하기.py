T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input().split()
    sum = 0
    for i in range(len(a)):
        if(int(a[i])%2 != 0):
            sum += int(a[i])
    print("#{} {}".format(test_case,sum))
    
    #arr = list(map(int, input().split()))
    #print(f"#{test_case}", sum([a for a in arr if a%2==1]))
    
    