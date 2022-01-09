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
        def preorder(root, string):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ','
                string = preorder(root.left, string)
                string = preorder(root.right, string)                        
            return string        
        
        return preorder(root, '')


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        
        def des(data):
            if data[0] == "None":
                data.pop(0)
                return None
            
            root = TreeNode(data[0])
            data.pop(0)
            
            root.left = des(data)
            root.right = des(data)
            
            return root
        
        return des(data_list)
            
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))