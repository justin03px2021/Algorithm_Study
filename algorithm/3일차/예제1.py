"""
    자료구조 : 1. 스택 / 2. 큐
        // 메모리에 데이터(data) 저장 하는데 저장 되는 방법!!!!
        // 1. 스택 ( stack )
            // 예 ) 동전케이스 , ctrl + z ( 뒤로가기 ) 등등
            // First in Last out => FILO
            // PUSH : 데이터 추가
            // POP : 데이터 추출
                    -----------------------
        DATA(PUSH) ------>
                            메모리
        <-------DATA(POP)
                    ---------------------
            VS
        // 2. 큐 (  Queue )
            // 예 ) 지하철 , 대기 프로그램 등등
            // First in First out -> FIFO
            ---------------------------
          Rear      `               Front
DATA(Enqueue)------>    메모리     -----------> DATA(Dequeue)
            ---------------------------
"""

# 리스트를 이용한 스택 구현

# 1. 스택[ = 리스트 구현 ] 선언
stack = [ None , None , None , None , None ] # 리스트 선언
# None = 데이터 없다 표시  # " " vs None vs 0

# 2. 스택 push        # 리스트의 인덱스는 0부터 시작한다 !!!
top = -1       # top : 현재 데이터 위치   [ 비어있는 stack 은 top = -1 ]
SIZE = 5       # SIZE : 스택에 데이터를 저장 할 수 있는 최대 개수
"""                     스택  = 사이즈(5)
                        top = 5         스택 풀
        |       |       top = 4
        |       |       top = 3
        |       |       top = 2         신동엽 
        |       |       top = 1         강호동
        |       |       top = 0         유재석
        ========        top = -1       [ -1 인덱스 존재X ] 
"""
"""
    // 리스트 상태 
    유재석 , 강호동 , 신동엽 , None , None 
"""
# 스택 출력 함수
def stack_print() :
    global top
    print("----------- 스택 상태 확인  ----------")
    print("top 위치 : " , top)
    for i in range( len(stack)-1  , -1 , -1 ) :
        print( stack[i] )

# 스택 비어있는 공간이 있는지 체크 함수
def isStackFull() :
    global SIZE , top
    if( top >= SIZE - 1) :
        print(" 스택 모두 찼습니다. ")
        return True
    else:
        print(" 비어 있는 자리가 존재합니다. " , ( SIZE-top ) - 1 , "개 남았습니다.")
        return False

stack_print()
isStackFull()

top += 1
stack[top] = "유재석"
stack_print()
isStackFull()

top +=1
stack[top] = "강호동"
stack_print()
isStackFull()

top +=1
stack[top] = "신동엽"
stack_print()
isStackFull()

top +=1
stack[top] = "김희철"
stack_print()
isStackFull()

top +=1
stack[top] = "ㄴㄱㅁ"
stack_print()
isStackFull()

# 3. 스택 POP
stack[top] = None
top -= 1
stack_print()
isStackFull()

stack[top] = None
top -= 1
stack_print()
isStackFull()

stack[top] = None
top -= 1
stack_print()
isStackFull()