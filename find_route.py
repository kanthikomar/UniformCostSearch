import sys
from Queue import Queue
from heapq import heappush,heappop

class PriorityQueue(Queue):
    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = []
    def _put(self, item):
        return heappush(self.queue, item)
    def _get(self):
        return heappop(self.queue)

def construct_graph(file_name):
    # print('creating graph')
    graph = {}
    file = open(file_name, 'r')
    for line in file:
        if 'END OF INPUT' in line:
            return graph
        vertexA, vertexB, distance = line.lower().split()
        graph.setdefault(vertexA, []).append((vertexB, distance))
        graph.setdefault(vertexB, []).append((vertexA, distance))


def find_route(graph, source, destination):
    fringe = set()
    queue = PriorityQueue()
    queue.put((0,[source]))
    while queue.empty() is False:
        #print('inside the while')
        distance, route = queue.get()
        vertex = route[len(route) - 1]
        if vertex not in fringe:
            fringe.add(vertex)
            if vertex == destination:
                route.append(distance)
                return route
            neighbours = graph[vertex]
            for neighbour in [neighbour[0] for neighbour in neighbours]:
                if neighbour not in fringe:
                    position = [node[0] for node in graph[vertex]].index(neighbour)
                    total_distance = distance + int(graph[vertex][position][1])
                    currentroute = route[:]
                    currentroute.append(neighbour)
                    queue.put((total_distance, currentroute))

def display(graph,path):
  distance = path[-1]
  print ('distance: %s'%(distance))
  print ('route: ')
  for x in path[:-2]:
    y = path.index(x)
    position = [z[0] for z in graph[x]].index(path[y+1])
    distance = graph[x][position][1]
    print ('%s to %s, %s km' %(x,path[y+1],distance))



if __name__ == "__main__" :
    graph = {}
    file_name = sys.argv[1]
    source = str(sys.argv[2]).lower()
    destination = str(sys.argv[3]).lower()
    graph = construct_graph(file_name)
    route = []
    if (graph.has_key(source)is False):
        print('source not found in the file')
        sys.exit()
    elif (graph.has_key(destination) is False):
        print('destination not found in the file')
        sys.exit()
    else:
        # print('great')
        route = find_route(graph, source, destination)
        if route:
            display(graph,route)
        else:
            print('distance: infinity')
            print ('route:')
            print (route)



