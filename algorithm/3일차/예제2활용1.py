# 식당 대기 프로그램  [  큐 구현 ]
#1. enQueue
def enQueue( data ) :
    global SIZE , front , rear
    if isQueueFull() :
        print(" 대기 인원 모두 찼습니다. ")
        return
    rear += 1           # 입구 인덱스 증가
    queue[rear] = data  # 입구에 데이터 추가
    print("고객님의 대기 번호 : ", rear + 1, " 입니다.")
#2. deQueue
def deQueue( ) :
    global  SIZE , front , rear
    if isQueueEmpty() :
        print(" 대기 인원이 없습니다. ")
        return None
    front += 1          # 출구 인덱스 증가
    data = queue[front]
    queue[front] = None    # 출구에 데이터 추출
    # 데이터 추출시 한칸씩 당기기
    for i in range( front+1 , rear+1 ) : # 모든 대기를 한칸씩 앞으로 당긴다.
        queue[i-1] = queue[i]
        queue[i] = None
    # 출구는 항상 -1 이여야 한다.
    front = -1
    # 입구는 한칸 앞으로 당긴다
    rear -= 1
    return data

# 5. isQueueEmpty
def isQueueEmpty():
    global SIZE, front, rear
    if front == rear:  # 입구와 출구가 -1 이면 큐 안에 데이터 존재X
        return True
    else:
        return False
#3. peek
def peek() :
    global SIZE , front , rear
    if isQueueEmpty() :
        print(" 다음 대기 인원이 없습니다. ")
        return None
    print(" 다음 입장할 고객 : " , queue[front+1] )
    return None

#4. isQueueFull
def isQueueFull( ) :
    global SIZE , front , rear
    if rear == SIZE-1 : # 만약에 입구번호가 최대 길이보다 크면 [
        return True
    else:
        return False

#6.전역변수
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1
# 프로그램 실행
while True :
    select = int( input( "1.대기등록 2.입장 3.종료  선택 : " ) )
    if select == 1 :
        print(" 대기 등록 ")
        phone = input("전화번호 : ")
        count = input("인원수 : ")
        enQueue(  ( phone , count )  )
        print( "현재 대기 상태 : " , queue )
    elif select == 2 :
        print(" 입장 ")
        deQueue()
        print("현재 대기 상태 : ", queue)
        peek()
    elif select == 3 :
        print(" 종료 ")
        break
    else:
        print(" 알수 없는 번호 입니다. ")
