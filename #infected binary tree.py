#infected binary tree
from collections import deque
class solution:
    def amountofTime()
        def bfs(root):
            q=deque([root])
            d={}
            while(len(q)>0):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                    d[node.left]=node
            return d
        def preorder(root,start):
            if(root==None):
                return None
            if(root.val==start):
                return root
            path1=preorder(root.left,start)
            if(path1!=None):
                return path1
            path2=preorder(root.left,start)
            return path1 or path2
        parent=bfs(root)
        start_address=preorder(root,start)
        vis=set([start_address])
        q=deque([start_address])
        m=0
        while(len(q)>0):
            for i in range(len(q)):
                none=q.popleft()
                #left
                if(node.left and node.left not in vis):
                    vis.add(node.left)
                    q.append(node.left)
                #right
                 if(node.right and node.right not in vis): 
                    vis.add(node.right)
                    q.append(node.right)  
                #parent
                if(node in parent and parent[node] not in vis):  
                    vis.add(parent[node])
                    q.append(parent[node])
            m+=1
        return m-1                

