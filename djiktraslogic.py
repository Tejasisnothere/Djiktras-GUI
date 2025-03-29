import heapq
from time import sleep
class DjikAlgo:

    def __init__(self, matrix, start, end, win):
        self.matrix = matrix
        self.found = False
        self.N = len(matrix)
        self.s_cords = start
        self.e_cords = end
        self.pq = []
        self.window = win

    def get_available(self, point):
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1, -1), (-1, 1)]

        poss_directions = [
            (point.pos_x + dx, point.pos_y + dy)
            for dx, dy in directions
            if 0 <= point.pos_x + dx < self.N and 0 <= point.pos_y + dy < self.N
        ]

        rem_directions = [
            (x, y) for x, y in poss_directions
            if self.matrix[x][y]['bg'] != 'blue'
        ]

        return rem_directions



    def visit_points(self, point):
        print(f"Visiting {point.pos_x},{point.pos_y} | Distance: {point.distance}")


        point.visited = True
        p = self.get_available(point)

        if len(p) == 0:
            return
        points = [self.matrix[i[0]][i[1]] for i in p]
        for inst_point in points:
            if inst_point.distance > point.distance + 1:
                inst_point.distance = point.distance + 1
                if not inst_point.visited:
                    inst_point.config(bg='green')
                    self.window.update()
                    sleep(0.1)

                inst_point.parent = point


        for i in points:
            if not i.visited:
                heapq.heappush(self.pq, (i.distance, i))

        while len(self.pq)!=0:

            _, popped = heapq.heappop(self.pq)
            if popped.visited:
                continue
            popped.visited=True
            if(popped.pos_x == self.e_cords[0] and popped.pos_y == self.e_cords[1]):
                self.trace_path(popped)
                return

            self.visit_points(popped)


    def trace_path(self, point):
        while point:
            point.config(bg="yellow")
            point = point.parent





