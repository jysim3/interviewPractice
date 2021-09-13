
from time import sleep
from queue import Queue, PriorityQueue
from Map import Map

class Car():

    def __init__(self, m: Map):
        self.map = m

    def find_path(self, start, end):
        return self.bidirectional_a_star(start, end)

    def bidirectional_a_star(self, start, end, heuristic=1.4):
        def get_q_item(point, is_start, distance_travelled):
            destination = end if is_start else start
            displacement = self.map.get_displacement(point[0], point[1], destination[0], destination[1])

            return (displacement*heuristic + distance_travelled, (point, is_start, distance_travelled+1))

        visited = dict()
        back_visited = dict()

        q = PriorityQueue()
        q.put(get_q_item(start, True, 0))

        p = PriorityQueue()
        p.put(get_q_item(end, False, 0))

        while not (q.empty() or p.empty()):
            _, (point, is_start, distance_travelled) = q.get()
            if not self.map.valid(point[0], point[1]):
                continue
            if point in back_visited:
                mid_point = point
                break
            self.map.draw(point[0],point[1])
            print(self.map)
            adj = [
                (point[0]  , point[1]-1),
                (point[0]-1, point[1]  ),
                (point[0]  , point[1]+1),
                (point[0]+1, point[1]  )
            ]
            for a in adj:
                if a in visited and distance_travelled >= visited[a][0]:
                    continue
                visited[a] = (distance_travelled, point)
                q.put(get_q_item(a, is_start, distance_travelled))

            _, (point, is_start, distance_travelled) = p.get()
            if not self.map.valid(point[0], point[1]):
                continue
            if point in visited:
                mid_point = point
                break
            self.map.draw(point[0],point[1])
            print(self.map)
            adj = [
                (point[0]  , point[1]-1),
                (point[0]-1, point[1]  ),
                (point[0]  , point[1]+1),
                (point[0]+1, point[1]  )
            ]
            for a in adj:
                if a in back_visited and distance_travelled >= back_visited[a][0]:
                    continue
                back_visited[a] = (distance_travelled, point)
                p.put(get_q_item(a, is_start, distance_travelled))
            sleep(0.05)
        front = []
        point = mid_point
        for _ in range(1000000):
            front.append(point)
            d, point = visited[point]
            if point == start:
                break

        back = []
        point = mid_point
        for _ in range(1000000):
            back.append(point)
            d, point = back_visited[point]
            if point == end:
                break

        front = list(reversed(front)) + back
        self.map.draw(start[0], start[1], "@")
        print(self.map)
        for f in front:
            self.map.draw(f[0], f[1], ".")
            print(self.map)
            sleep(0.01)
        self.map.draw(start[0], start[1], "@")
    
    def bidirectional(self, start, end):

        l_visited = {}
        
        r_visited = {}
        q = Queue()
        q.put((start, True))
        q.put((end, False))
        while not q.empty():
            point, is_start = q.get()
            if point in l_visited and point in r_visited:
                break
            if not self.map.valid(point[0], point[1]):
                continue
            if is_start:
                visited = l_visited
            else:
                visited = r_visited
            if point in visited:
                continue
            self.map.draw(point[0],point[1])
            print(self.map)
            a = ((point[0]  , point[1]-1), is_start)
            b = ((point[0]-1, point[1]  ), is_start)
            c = ((point[0]  , point[1]+1), is_start)
            d = ((point[0]+1, point[1]  ), is_start)
            visited[point] = a
            visited[point] = b
            visited[point] = c
            visited[point] = d
            q.put(a)
            q.put(b)
            q.put(c)
            q.put(d)
    

    def a_star(self, start, end, heuristic=1.3):
        def get_q_item(p, history):
            return (self.map.get_displacement(p[0], p[1], end[0], end[1])*heuristic + len(history), [x for x in history] + [p])

        visited = set()
        q = PriorityQueue()
        q.put( get_q_item(start, []) )
        while not q.empty():
            v, history = q.get()
            point = history[-1]

            if point in visited:
                continue
            if not self.map.valid(point[0], point[1]):
                continue
            self.map.draw(point[0],point[1])
            print(self.map)
            print(point, end, self.map.get_displacement(point[0], point[1], end[0], end[1]))
            if point == end: break
            if point != end:
                q.put(get_q_item((point[0]  , point[1]-1), history))
                q.put(get_q_item((point[0]-1, point[1]  ), history))
                q.put(get_q_item((point[0]  , point[1]+1), history))
                q.put(get_q_item((point[0]+1, point[1]  ), history))
                #q.put(get_q_item((point[0]+1, point[1]+1), history))
                visited.add(point)
    
    def bfs(self, start, end):

        visited = set()
        q = Queue()
        q.put( [start] )
        while not q.empty():
            history = q.get()
            point = history[-1]

            if point in visited:
                continue
            if not self.map.valid(point[0], point[1]):
                continue

            if point != end:
                q.put([x for x in history] + [(point[0]  , point[1]-1)])
                q.put([x for x in history] + [(point[0]-1, point[1]  )])
                q.put([x for x in history] + [(point[0]  , point[1]+1)])
                q.put([x for x in history] + [(point[0]+1, point[1]  )])
                visited.add(point)
            self.map.draw(point[0],point[1])
            print(self.map)
            sleep(0.01)
