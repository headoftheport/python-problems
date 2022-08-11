"""serialize and deserialize"""

from binary_tree_node import TreeNode

class Codec:
    """codec """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        values = []
        def preorder(root):
            
            if root is None:
                values.append("null")
                return 
            
            values.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root) 
        string = ",".join(values)
        return string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        values = data.split(",")
        def construct():
            
            val = next(values)
            
            if val == 'null':
                return None
            
            node = TreeNode(int(val))
            node.left = construct()
            node.right = construct()
            return node
        
        values = iter(values)
        return construct()