class Solution:
    def spiralOrder(self, matrix):
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # → right along top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # ↓ down along right column
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # ← left along bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # ↑ up along left column
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result