# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        node = root
        def debuild(node):
            result.append(str(node.val))
            if node.left:
                debuild(node.left)
            
            else:
                result.append("None")

            if node.right:
                debuild(node.right)

            else:
                result.append("None")
            
        debuild(root) if root else None
        answer = " ".join(result)
        return answer

        
    # Decodes your encoded data to tree. From a preorder traversal encoding
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        tokens = data.split()
        def build():
            nonlocal i
            
            if i >= len(tokens):
                return None

            value = tokens[i]
            i+=1

            if value == "None":
                return None

            node = TreeNode(value)
            node.left = build()
            node.right = build()
            
            return node

        return build()

