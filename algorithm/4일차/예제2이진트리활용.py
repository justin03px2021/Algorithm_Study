
import random   # import : 현재 py파일 외 다른 미리 만들어진 파일[클래스] 불러오기
    # 1. 난수 관련 메소드 제공
# 제품 판매 중복체크 [ 이진트리 구현 ]
# 1. 이진트리 노드 선언
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 2. 전역변수
memory = [ ]
root = None
datalist = ["바나나맛우유" , "레스비커피" , "츄파춥스","도시락","삼다수","코카콜라","삼각김밥"]
selllist = [ random.choice( datalist) for _ in range(50) ]
# 랜덤으로 DATALIST에서 제품명를 SELLLIST에 50개 저장
print(" 오늘 판매된 물건(중복o) ---> : " , selllist )

# 3.메인 실행
node = TreeNode()  # 노드 생성
node.data = selllist[0]     # 판매된 첫번째 제품
root = node # root node 선정
memory.append( node )

for name in selllist[1:] : # 판매리스트에서 1인덱스부터 마지막 인덱스 까지 반복처리
    node = TreeNode()
    node.data = name

    current = root      # current : 현재 위치
    while True :
        if name == current.data :   # 만약에 해당 인덱스의 data  현재위치의 data 와 동일하면
            break
        if name < current.data :      # 만약에 해당 인덱스의 data 가  현재위치의 data 더 작으면
            if current.left == None :   # 만약에 왼쪽 자식노드가 없으면
                current.left = node     # 왼쪽 자식노드에 추가
                memory.append(node)
                break
            current = current.left      # 부모노드보다 데이터가 작으면 왼쪽 배치
        else:                           #만약에 해당 인덱스의 data가 현재위치의 data 더 크면
            if current.right == None :     # 만약에 오른쪽 자식노드가 없으면
                current.right = node       # 오른쪽 자식노드에 추가
                memory.append(node)
                break
            current = current.right     # 부모노드보다 데이터가 크면 오른쪽 배치

# 전위 순회
def preorder( node ) :
    if node ==None :
        return
    print(node.data , end=" ")
    preorder( node.left )
    preorder( node.right )

print()
print(" 오늘 판매된 물건(중복x) ---> : " , end = " " )
preorder( root )







