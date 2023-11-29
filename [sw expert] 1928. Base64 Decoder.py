decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]

T = int(input())
for test_case in range(1,T+1):
    en_string = list(map(str,input()))
    de_string = ""
    result = ""
    for i in range(len(en_string)):
        buffer = decode.index(en_string[i])
        buffer = bin(buffer)[2:]
        buffer = str(0)*(6-len(buffer))+buffer
        de_string += buffer
    for i in range(0,len(de_string),8):
        slicing = de_string[i:i+8]
        result += chr(int(slicing,2))
    print("#{} {}".format(test_case,result))