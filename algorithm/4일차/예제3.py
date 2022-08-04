"""
    그래프
        예) 지하철 노선도 , 전기 회로도 , 인맥 관계도
        1. 여러 노드가 서로 연결된 자료구조
        2. 그래프 종류
            1. 무방향 그래프 ( 이동 방향 표기X )
            2. 방향 그래프 ( 이동 방향 표기O )
"""


# 그래프 구현 : 2차원 리스트를 이용한 그래프 구현
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        # 1. [ 0 , 0 , 0 , 0 ]
        # 2. [ [ 0 , 0 , 0 , 0 ]  , [ 0 , 0 , 0 , 0 ] ,  [ 0 , 0 , 0 , 0 ]  , [ 0 , 0 , 0 , 0 ] ]
        #  2차원리스트 :  [  [ 열1,열2,열3,열4 ] , [ 열1,열2,열3,열4 ]  , [ 열1,열2,열3,열4 ]  ]


G1 = None  # 객체 [ 클래스로부터 메모리 할당 전  = 선언만 했을경우 ]
G1 = Graph(4)  # 인스턴스 [ 선언된 객체에 해당 클래스로 메모리할당 ]
G1.graph[0][1] = 1;
G1.graph[0][2] = 1;
G1.graph[0][3] = 1
G1.graph[1][0] = 1;
G1.graph[1][2] = 1
G1.graph[2][0] = 1;
G1.graph[2][1] = 1;
G1.graph[2][3] = 1
G1.graph[3][0] = 1;
G1.graph[3][2] = 1
# 출력 [ 무방향 그래프 ]
print(" ------- 무방향 그래프 ------------ ")
for row in range(4):  # row : 행   row는 0부터 3까지 1씩 증가 반복처리
    for col in range(4):  # col : 열   col는 0부터 3까지 1씩 증가 반복처리
        print(G1.graph[row][col], end=" ")
    print()
"""     # 중첩 반복문 [ 어렵다~~~ -->> 순서도  ]
    row = 0 일때
        col = 0 , col = 1 , col = 2 , col = 3
        [0][0]     [0][1]   [0][2]      [0][3]
    row = 1 일때
        col = 0 , col = 1 , col = 2 , col = 3 
        [1][0]      [1][1]  [1][2]      [1][3]
    row = 2 일때 
        col = 0 , col = 1 , col = 2 , col = 3 
        [2][0]      [2][1]  [2][2]      [2][3]
    row = 3 일때 
        col = 0 , col = 1 , col = 2 , col = 3
        [3][0]      [3][1]  [3][2]      [3][3]
"""
# 출력 [ 방향 그래프 ]
G3 = Graph(4)
G3.graph[0][1] = 1;
G3.graph[0][2] = 1
G3.graph[3][0] = 1;
G3.graph[3][2] = 1

print(" ------- 방향 그래프 ------------ ")

for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end=" ")
    print()
"""
    무방향 vs 방향 그래프 
        0: 연결x  1:연결o

    # 무방향 : 대칭 관계 

    무방향 초기값 
        A B C D                     B       
      A 0 
      B   0                 A               C
      C     0 
      D       0                     D

    # 1. A 와 B 연결 
        A B C D                  B       
      A 0 1                   / 
      B 1 0                 A       C
      C     0                   
      D       0                 D    

    # 2. A 와 C 연결 
        A B C D                  B       
      A 0 1 1                  / 
      B 1 0                 A  ------  C
      C 1   0                   
      D       0                 D    

    # 3. A 와 D 연결 
        A B C D                 B       
      A 0 1 1 1               / 
      B 1 0                 A  --- C
      C 1   0                 \  
      D 1     0                 D    '

    # 3. B 와 C 연결  / C와 D 연결  
        A B C D                 B       
      A 0 1 1 1               /    \
      B 1 0 1 0              A --- C
      C 1 1 0 1               \    /
      D 1 0 1 0                 D   

---------------------------------------------
    방향 
      A B C D              B
    A 0                     
    B   0               A      C
    C     0             
    D       0              D

    # 1. A ---> B 연결 
      A B C D              B
    A 0 1                /   
    B   0               A      C
    C     0             
    D       0              D

    # 2. A ---> C 연결 
      A B C D              B
    A 0 1 1 0             /   
    B   0               A  --> C
    C     0             
    D       0               D

    # 3. D ---> A 연결 
      A B C D              B
    A 0 1 1 0             /   
    B   0               A  --> C
    C     0               \
    D 1     0               D

    # 4. D ---> C 연결 
      A B C D              B
    A 0 1 1 0             /   
    B   0               A  --> C
    C     0               \   /
    D 1   1 0               D  







"""
