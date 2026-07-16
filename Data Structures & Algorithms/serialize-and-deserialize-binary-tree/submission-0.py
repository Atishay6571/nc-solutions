# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def bfs(root):
            result=""
            queue=deque()
            queue.append(root)
            while queue:
                node=queue.popleft()
                
                if node:
                    result+=str(node.val)
                    result+=","
                    queue.append(node.left)
                    queue.append(node.right)
                elif not node:
                    result+="N,"
                    continue
            return result
        return bfs(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result=data.split(',')
        if result[0]=="N":
            return None
        queue=deque()
        root=TreeNode(int(result[0]))
        queue.append(root)
        i=1
        while queue:
            node=queue.popleft()
            if result[i]!="N":
                node.left=TreeNode(result[i])
                queue.append(node.left)
            i+=1
            if result[i]!="N":
                node.right=TreeNode(result[i])
                queue.append(node.right)
            i+=1
        return root
    