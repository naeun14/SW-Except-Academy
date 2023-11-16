import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int,input().split()))
    count = 0
    coin = 0
    n = 0
    max_price = price[-1]
    for i in range(day-2,-1,-1):
        if max_price <= price[i]:
            max_price = price[i]
        else:
            coin += max_price - price[i]
            
        
    print("#{} {}".format(test_case,coin))
    