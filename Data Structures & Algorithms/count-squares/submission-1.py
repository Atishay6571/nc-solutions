class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)      # (x, y) → count
        self.x_map = defaultdict(list)      # x → list of y values

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.x_map[point[0]].append(point[1])

    def count(self, point: List[int]) -> int:
        qx, qy = point
        result = 0
        for py in self.x_map[qx]:
            side = py - qy
            if side == 0:
                continue
            result += self.points[(qx + side, qy)] * self.points[(qx + side, py)]
            result += self.points[(qx - side, qy)] * self.points[(qx - side, py)]
        return result