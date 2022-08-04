names = []
def add_data(name):
    names.append(None)
    count = len(names)
    names[count-1] = name

def insert_data(position, name):
    if position < 0 or position > len(names):
        print(['인덱스가 없다'])
        return

    names.append(None) #1.배열에 메모리 할당
    count = len(names)  #2. 배열의 길이 체크

    for i in range(count - 1,position, -1):
        name[i] = names[i-1]
        names[i-1] = None
    names[position] = name

def remove_data(position):
    if position < 0 or position > len(names):
        print(['인덱스가 없다'])
        return
    count = len(names)
    names[position] = None

    for i in range(position + 1,count):
        name[i-1] = name[i]
        names[i] = None
    del(names[count-1])



add_data('유재석')
add_data('강호동')
add_data('신동엽')
add_data('서장훈')
add_data('김희철')
insert_data(2,'하하')
print(names)

