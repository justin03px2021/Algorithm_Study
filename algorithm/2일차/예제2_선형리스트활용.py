# 구현 프로그램 : 이름 과 나이를 입력받아 나이순 정렬후 출력
# 1. 선형리스트으로 구현
# 2. 메뉴 [ 1.추가 2.삽입 3.삭제 4.종료 ]


# 1. 추가 함수 구현
def add_data(  name , age ) :
    namelist.append( None )
    count = len(namelist)
    namelist[ count -1  ] = ( name , age )  # 마지막 인덱스 튜플 추가
    # 길이는 1부터  // 인덱스는 0부터 // 길이가 인덱스 변환 -1
#2. 삽입 함수 구현
def insert_data( pos , name , age ) :
    if pos < 0 or pos > len(namelist) :
        print(" 해당 인덱스가 존재하지 않습니다.")
        return
    namelist.append(None)   # 1. 메모리 할당 우선
    count = len(namelist)   # 2. 길이 체크
    for i in range( count-1 , pos , -1) :
        namelist[i] = namelist[i-1]
        namelist[i-1] = None
    namelist[pos] = ( name , age )
#3. 삭제 함수 구현
def delete_data( pos ) :
    if pos < 0 or pos > len(namelist) :
        print(" 해당 인덱스가 존재하지 않습니다.")
        return
    count = len(namelist)
    namelist[pos] = None
    for i in range( pos+1 , count ) :
        namelist[i-1] = namelist[i]
        namelist[i] = None
    del( namelist[ count-1 ] )

# 4. 정렬( 나이순으로 )  함수 구현  [ .sort 구현 ]
def sort_data(  ) :     # 정렬 함수 선언
    for i in range( 0 , len(namelist) , 1 ) :       # i : 비교기준
        for j in range( 0 , len(namelist) , 1 ) :   # j : 비교대상
            if namelist[i][1] > namelist[j][1] :    # i의 나이 보다 j의 나이가 더 크면
                # i 인덱스 데이터 와 j의 인덱스 데이터 교환[ swap ]
                temp = namelist[i]                      # temp = 20
                namelist[i] = namelist[j]               # 20 = 30
                namelist[j] = temp                      # 30 = temp
    print(" 나이순 정렬된 출력 : ", namelist )            # 20 과 30 데이터가 스왑 !!!

    #  정렬 시나리오
        #  3  , 4 , 2 , 5
        # 1. 각 인덱스 마다 다른 인덱스 비교
            # 1. 0인덱스 -> 1 , 2 , 3
            # 2. 1인덱스 -> 2 , 3
            # 3. 2인덱스 -> 3
            # 4. 3인덱스 -> x  [ 비교 당했기 때문에 비교 x ]
            # 비교기준 = i  // 비교대상  : j
# 0.
namelist = [ ("유재석" , 20) , ("강호동" , 10 ) , ("신동엽" , 15 ) ]

if __name__== "__main__":       #메인 코드 실행 되는 부분
    while True : # 무한루프
        select = int( input('선택 : 1.추가 2.삽입 3.삭제 4.종료 ') )  # 메뉴 출력 -> 메뉴번호 입력
        if select == 1  :
            name = input("추가 이름 : ")
            age = int( input("추가 나이 : ") )
            add_data( name , age )
            print( namelist )
        elif select == 2 :
            pos = int( input("삽입할 위치 : ") )
            name = input("추가 이름 : ")
            age = int(input("추가 나이 : "))
            insert_data( pos , name , age )
            print( namelist )
        elif select == 3 :
            pos = int( input("삭제할 위치 : ") )
            delete_data( pos )
            print(namelist)
        elif select == 4 :
            sort_data()
            print(" 프로그램 종료 합니다. ")
            break   # 가장 가까운 반복문 탈출
        else:
            print(" 메뉴 1~4 사이만 입력해주세요 : ")
            continue # 가장 가까운 반복문 이동![](../../../Screen Shot 2022-06-16 at 8.21.18 PM.png)