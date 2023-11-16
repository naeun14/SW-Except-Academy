T = int(input())
for test_case in range(1,T+1):
    result = -1
    l = list(map(int,input()))
    year = l[0]*1000 + l[1]*100+l[2]*10 + l[3]*1
    month = l[4]*10 + l[5]*1
    day = l[6]*10 + l[7]*1
    if  13>month>0 and 32>day>0 :
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                result =  str(l[0]) + str(l[1])+ str(l[2]) + str(l[3]) + "/" + str(l[4]) + str(l[5])+  "/" + str(l[6]) + str(l[7])
            elif month == 4 or month == 6 or month == 9 or month == 11 and 31>day>0: 
                result =  str(l[0]) + str(l[1])+ str(l[2]) + str(l[3]) + "/" + str(l[4]) + str(l[5])+  "/" + str(l[6]) + str(l[7])
            elif month == 2 and 29>day>0:
                result =  str(l[0]) + str(l[1])+ str(l[2]) + str(l[3]) + "/" + str(l[4]) + str(l[5])+  "/" + str(l[6]) + str(l[7])
            
    print("#{} {}".format(test_case,result))