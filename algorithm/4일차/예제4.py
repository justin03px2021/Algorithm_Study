# 최단 거리 찾기 [ 그래프 구현 ]
# 조건 : 춘천 , 서울 , 속초 , 대전 , 광주 , 부산
# 조건 : 지역 이동간 걸리는 시간 [ 임의 ]
# 문제 : 춘천 --> 부산 최단거리

# 1. 그래프 클래스 선언 [2차원 리스트를 이용한 그래프 구현 ]
from pip._internal.cli.cmdoptions import editable


class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.Graph = [[0 for _ in range(size)] for _ in range(size)]


# 그래프 출력 함수
def Graph_print(g):
    print("   ", end=" ")  # 1. 가로제목 출력부분

    for v in range(g.SIZE):  # 지역개수만큼 반복문
        print(Locationlist[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(Locationlist[row], end=" ")  # 2.세로제목 출력부분
        for col in range(g.SIZE):
            print("%3d" % g.Graph[row][col], end=" ")
            # %3d   : 정수 세자리 자리차지
            # 정수가 세자리가 아닐경우 공백으로 채움
            # %03d  : 정수 세자리 자리차지
            # 정수가 세자리가 아닐경우 0으로 채움

        print()
    print()


# 2. 전역변수
G1 = None
Locationlist = ["춘천", "서울", "속초", "대전", "광주", "부산"]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5
# 3. 실행
Locationsize = len(Locationlist)
G1 = Graph(Locationsize)
# 지역 이동간 걸리는 시간 [ 임의 설정 ]
G1.Graph[춘천][서울] = 10;
G1.Graph[춘천][속초] = 15
G1.Graph[서울][춘천] = 10;
G1.Graph[서울][속초] = 40;
G1.Graph[서울][대전] = 11;
G1.Graph[서울][광주] = 50
G1.Graph[속초][춘천] = 15;
G1.Graph[속초][서울] = 40;
G1.Graph[속초][대전] = 12
G1.Graph[대전][서울] = 11;
G1.Graph[대전][속초] = 12;
G1.Graph[대전][광주] = 20;
G1.Graph[대전][부산] = 30
G1.Graph[광주][서울] = 50;
G1.Graph[광주][대전] = 20;
G1.Graph[광주][부산] = 25
G1.Graph[부산][대전] = 30;
G1.Graph[부산][광주] = 25
# 지역별 고속도로간 걸리는 시간 출력
Graph_print(G1)

# 가중치 간선
edgelist = []  # 고속도로 가 존재하는 거리만 리스트 선언
for i in range(Locationsize):
    for k in range(Locationsize):
        if G1.Graph[i][k] != 0:  # 거리가 존재하면
            edgelist.append([G1.Graph[i][k], i, k])
            #   이동시간 , 출발지 , 도착지
print("정렬 전 : ", edgelist)

# 정렬[ 정렬 클래스를 이용한 정렬 ]  reverse= True : 내림차순  / 생략시 오름차순
from operator import itemgetter

edgelist = sorted(edgelist, key=itemgetter(0), reverse=True)
# sorted ( 리스트 , ket = itemgetter(인덱스)  ,
print("정렬 후(이동시간) : ", edgelist)

# 무방향은 대칭 관계 -> 단방향
newary = []
for i in range(0, len(edgelist), 2):  # 0인덱스부터 마지막인덱스까지 2씩 증가
    newary.append(edgelist[i])

print(newary)  # 단방향 리스트 생성


def find(g, location):
    stack = []  # 지점를 지나는 스택
    visitedary = []  # 방문한 지역
    current = 0  # 시작 지점
    stack.append(current)
    visitedary.append(current)
    while (len(stack) != 0):
        next = None  # 다음 지점 선언
        for var in range(Locationsize):
            if g.Graph[current][var] != 0:
                if var in visitedary:  # 방문한 적이 있는 지점이면 X
                    pass
                else:  # 방문한 적이 없으면
                    next = var  # 다음에 방문
                    break
        if next != None:  # 다음에 방문할 지점이 있을경우
            current = next  # 현재 지점를 다음 지점으로 변경
            stack.append(current)  # 스택 추가
            visitedary.append(current)  # 방문목록 추가
        else:  # 다음에 방문할 지점이 없을경우
            current = stack.pop()

    if location in visitedary:
        return True
    else:
        return False


# 거리 계산
index = 0  # 거리 순서
while (len(newary) > Locationsize - 1):  # 간선의 개수가 마지막 지역 까지 반복
    start = newary[index][1]  # 출발지
    end = newary[index][2]  # 도착지
    saveCost = newary[index][0]  # 걸리는 시간

    G1.Graph[start][end] = 0  # 초기값 설정
    G1.Graph[end][start] = 0

    startYN = find(G1, start)
    endYN = find(G1, end)

    if startYN and endYN:
        del (newary[index])
    else:
        G1.Graph[start][end] = saveCost
        G1.Graph[end][start] = saveCost
        index += 1
print(" 춘천 ---> 부산까지의 최단 거리 ")
Graph_print(G1)
"""
            춘천
        10       15
    서울     40     속초
         11      12 
    50      대전 
        20      30 
    광주     25    부산 

"""

