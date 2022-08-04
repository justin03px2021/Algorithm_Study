import time
def fact(num):
    if num <= 1:
        print('종료')
        return 1
    print('%d * %d 호출' % (num,num-1))
    val = fact(num - 1)
    print('%d * %d = %d 반환' %(num, num-1,val))
    return num * val
# num = int(input('수 입력 : '))
# print(fact(num))

def countDown(n):
    if n == 0:
        print('시작')
    else:
        print(n)
        time.sleep(1)
        countDown(n-1)
# countDown(10)

def starprint(n):
    if n>0:
        starprint(n-1)
        print("*"*n)

# starprint(5)

def gugu(dan, num):
    print('%d * %d = %2d' % (dan,num, dan * num))
    if dan < 9:
        gugu(dan + 1, num)

for num in range(1,10):
    gugu(2,num)
    print()