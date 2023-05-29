'''
파이썬에서 Class 개념을 이용한 LinkedList 구현은 두 클래스의 객체가 
서로를 참조함으로써 각 기능들을 구현할 수 있다. LinkedList의 맴버변수
들이 LinkedList 기능으로부터 생성된 Node 객체들을 참조하고 유기적으로
연결하고 정의하여, 논리적 연결성을 지닌 Node 구조체를 형성할 수 있다.
'''

# Node 만들기
class Node:
    def __init__(self, value = 0 , next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

# LinkedList 만들기
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # LinkedList에 값 추가
    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    # LikedList에서 특정 인덱스 위치한 값 리턴
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    # LikedList에서 특정 위치에 값 삽입
    def insert_at(self, idx, value):
        current = self.head
        new_node = Node(value)
        
        for _ in range(idx-1):
            current = current.next
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    # LinkedList에서 인덱스 값 삭제
    def remove_at(self, idx):
        current = self.head
        if idx == 0:
            self.head = current.next
            current.next = None
            self.head.prev = None
            
        else:
            for _ in range(idx):
                current = current.next
            current.next.prev = current.prev
            current.prev.next = current.next

    # LinkedList를 파이썬 리스트 형태로 출력
    def output(self):
        pylist =[]
        current = self.head
        while current is not None:
            pylist.append(current.value)
            current = current.next
        return pylist


ll = LinkedList()

ll.append(1)

ll.append(2)

ll.append(3)

ll.append(4)

print('index 2 위치에 5 삽입')
ll.insert_at(2, 5)

print(ll.get(2))
print(ll.output())
print()

print('index 3에 위치한 값 삭제')
ll.remove_at(0)

print(ll.output())
print()
