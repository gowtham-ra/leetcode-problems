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
        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                vals.append('None')
        
        vals = []
        preorder(root)
        
        return ','.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(','))
        
        def des():
            val = next(vals)
            if val == 'None':            
                return None
            
            root = TreeNode(int(val))            
            root.left = des()
            root.right = des()
            
            return root
        
        return des()
            
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))