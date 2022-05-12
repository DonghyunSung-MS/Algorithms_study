class Node:
    def __init__(self, name) -> None:
        self.remove = False
        self.prev = None
        self.next = None
        self.name = name

    def __repr__(self) -> str:
        return str(self.name)
       
def solution(n, k, cmd):
    linklist = [Node(i) for i in range(n)]

    for i in range(n-1):
        linklist[i].next = linklist[i+1]
        linklist[i+1].prev = linklist[i]


    deleted = []
    current = linklist[k]

    for c in cmd:
        if c[0]=="D":
            move =  int(c.split(" ")[-1])
            for _ in range(move):
                current = current.next
                
        elif c[0]=="U":
            move = int(c.split(" ")[-1])
            for _ in range(move):
                current = current.prev
                
        elif c[0]=="C":# 삭제
            deleted.append(current)
            current.remove = True
            
            cprev = current.prev
            cnext = current.next

            if cnext:
                cnext.prev = cprev  # None 도 커버가능
                current = cnext
            else:
                current = cprev

            if cprev:
                cprev.next = cnext        
        elif c[0]=="Z": #복구   
            node = deleted.pop()
            node.remove = False
            
            if node.prev:
                node.prev.next = node
            
            if node.next:
                node.next.prev = node

    answer = ""
    for i in range(n):
        if linklist[i].remove:
            answer+="X"
        else:
            answer+="O"

    return answer

if __name__ == "__main__":
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	))