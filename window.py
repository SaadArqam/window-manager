class Node():
    def __init__(self,id):
        self.id=id
        self.next=None
        self.prev=None

class WindowManager:
    def __init__(self):
        self.state={}
        self.nodes={}

        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def toTopHelper(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def removeHelper(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def open(self,id):
        if id not in self.state or self.state[id]=="CLOSED":
            node=Node(id)
            self.nodes[id]=node
            self.toTopHelper(node)
            self.state[id]="OPEN"

        elif self.state[id]=="MINIMIZED":
            self.restore(id)

        else:
            self.focus(id)

    def focus(self, id):
        if id in self.state and self.state[id]!="CLOSED":
            if self.state[id]=="MINIMIZED":
                self.restore(id)
                return
            node=self.nodes[id]
            self.removeHelper(node)
            self.toTopHelper(node)
        
    def minimize(self,id):
        if id in self.state and self.state[id]=="OPEN":
            node=self.nodes[id]
            self.removeHelper(node)
            self.state[id]="MINIMIZED"
    
    def restore(self,id):
        if id in self.state and self.state[id]=="MINIMIZED":
            node=self.nodes[id]
            self.toTopHelper(node)
            self.state[id]="OPEN"

    def close(self,id):
        if id in self.state and self.state[id]!="CLOSED":
            if self.state[id] == "OPEN":
                node = self.nodes[id]
                self.removeHelper(node)
            self.state[id]="CLOSED"
            if id in self.nodes:
                del self.nodes[id]

    def top(self):
        if self.head.next==self.tail:
            return -1
        return self.head.next.id

    def list(self):
        res=[]
        curr=self.head.next
        while curr!=self.tail:
            res.append(curr.id)
            curr = curr.next
        return res


# test
wm = WindowManager()
wm.open(1)
wm.open(2)
wm.close(2)

print(wm.list())  
print(wm.top())    