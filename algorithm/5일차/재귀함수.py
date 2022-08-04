# def openBox():
#     global i
#     i += 1
#     print('상자를 열기', i);
#     openBox()
#
# i=0
# openBox()

def openBox2():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('선물 넣기')
        return
    openBox2()
    print('상자 닫기')
count = 3
openBox2()

def plus(num):
    if num<=1:
        return 1
    return num + plus(num - 1)
print(plus(3))

3 + 2
2 + 1

