# Serialize or deserialize binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        h = []
        def setHeap(r):
            if r == None:
                h.append(None)
                return
            h.append(r.val)
            setHeap(r.left)
            setHeap(r.right)
            return
        setHeap(root)
        return str(h)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        ml = len(data)
        if ml==0:
            return None
        i = 0
        def newRec(i):
            if i >= ml or data[i]==None:
                return None, i
            x = TreeNode(data[i])
            x.left, i = newRec(i+1) 
            x.right, i = newRec(i+1)
            return x, i
        x,y = newRec(0)
        return x
        

# Your Codec object will be instantiated and called as such:
#codec = Codec()
#codec.deserialize(codec.serialize(root))