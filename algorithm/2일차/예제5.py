# 원형 연결 리스트 [ Circular Linked list ]
# 싱글 연결 리스트 : 시작 , 끝[o]
    #  역삼역 -> 강남역 -> 교대역 -> 서초역  :  내린다[끝] .
# 원형 연결 리스트 : 시작, 끝[x]
    #  역삼역 -> 강남역 -> 교대역 -> 서초역  :  역삼역 간다

class Node() : # 노드 클래스 선언
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "유재석"
node1.link = node1      # 유재석 -> 유재석 -> 유재석

node2 = Node()
node2.data="강호동"
node1.link = node2
node2.link = node1      # 유재석 -> 강호동 -> 유재석 -> 강호동

node3 = Node()
node3.data = "신동엽"
node2.link = node3
node3.link = node1      # 유재석 -> 강호동 -> 신동엽 -> 유재석 ~~~~~~

# 출력 함수 구현
def node_print()  :
    current  = node1
    print( current.data , end = ' ')
    #while current.link != None :       # 원형 연결리스트 끝이 존재하지 않기 때문에 무한루프
    while current.link !=node1 :        # 첫 지점으로 다시 왔을때 무한루프 종료
        current = current.link
        print( current.data , end = ' ')
node_print()

