from sample_tree import root
from collections import deque

def LevelOrder(root):
    de=deque()
    de.append(root)
    while len(de)!=0:
        rNode=de.popleft()
        print(rNode.k,end=' ')

        if rNode.left!=None:
            de.append(rNode.left)
        if rNode.right!=None:
            de.append(rNode.right)


LevelOrder(root)
