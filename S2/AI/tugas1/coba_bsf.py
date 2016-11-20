def bfs(graph, start, goal, path=[]):

  open=[start]
  closed=[]
  goal = goal
  nomor=1
  while open:
    X=open.pop(0)
    print 'Langkah ke : ',nomor
    print 'X : ',X
    print 'Open : ',open
    if X == goal:
        print 'Solution found'
        return
    else:
        children = graph[X]
        print 'Children : ',children
        
        if not X in path:
            path=path+[X]
            open=open+graph[X]
            #open=graph[X]


        if not X in closed:
            closed=closed+[X]
        print 'Closed : ', closed
        print 'Path : ', path
    nomor=nomor+1
    print '==================\n'

            
  return #path


graph = {
         'Arad':['Zerind','Sibiu','Timisoara'],
         'Zerind':['Oradea','Arad'],
         'Sibiu':['Fagaras','RimnicuVilcea','Oradea','Arad'],
         'Timisoara':['Lugoj','Arad'],
         'Oradea':['Sibiu','Zerind'],
         'Lugoj':['Mehadia','Timisoara'],
         'Fagaras':['Bucharest','Sibiu'],
         'RimnicuVilcea':['Pitesti','Craiova','Sibiu'],
         'Pitesti':['Bucharest','RimnicuVilcea','Craiova'],
         'Craiova':['Pitesti','Drobeta','RimnicuVilcea'],
         'Mehadia':['Drobeta','Lugoj'],
         'Drobeta':['Craiova','Mehadia'],
         'Bucharest':['Giurgiu','Urziceni','Fagaras','Pitesti'],
         'Giurgiu':['Bucharest'],
         'Urziceni':['Hirsova','Vaslui','Bucharest'],
         'Hirsova':['Eforie','Urziceni'],
         'Eforie':['Hirsova'],
         'Vaslui':['Lasi','Urziceni'],
         'Lasi':['Neamt','Vaslui'],
         'Neamt':['Lasi']
         }


#bfs(graph, 'Arad', 'Bucharest')

def BFS(graph, mulai, tujuan, path=[]):
    open=[mulai]
    closed=[]
    children=[]
    while open:
        X = open.pop(0)
        if X == tujuan:
            print 'Solusi tercapai'
            return
        else:
            children = graph[X]
            if not X in closed:
                closed=closed+[X]
            
            if not X in path:
                path=path+[X]
                open=open+(graph[X])
            #open=graph[X]
            #print 'Path : ', path
            print 'X : ', X
            print 'Open : ',open
            print 'Children : ',children
            print 'Closed : ', closed

    return
#BFS(graph, 'Arad', 'Bucharest')



graph2 = {
         'Arad':set(['Zerind','Sibiu','Timisoara']),
         'Zerind':set(['Oradea','Arad']),
         'Sibiu':set(['Fagaras','RimnicuVilcea','Oradea','Arad']),
         'Timisoara':set(['Lugoj','Arad']),
         'Oradea':set(['Sibiu','Zerind']),
         'Lugoj':set(['Mehadia','Timisoara']),
         'Fagaras':set(['Bucharest','Sibiu']),
         'RimnicuVilcea':set(['Pitesti','Craiova','Sibiu']),
         'Pitesti':set(['Bucharest','RimnicuVilcea','Craiova']),
         'Craiova':set(['Pitesti','Drobeta','RimnicuVilcea']),
         'Mehadia':set(['Drobeta','Lugoj']),
         'Drobeta':set(['Craiova','Mehadia']),
         'Bucharest':set(['Giurgiu','Urziceni','Fagaras','Pitesti']),
         'Giurgiu':set(['Bucharest']),
         'Urziceni':set(['Hirsova','Vaslui','Bucharest']),
         'Hirsova':set(['Eforie','Urziceni']),
         'Eforie':set(['Hirsova']),
         'Vaslui':set(['Lasi','Urziceni']),
         'Lasi':set(['Neamt','Vaslui']),
         'Neamt':set(['Lasi'])
         }


def bfs(graph, start):
    visited, queue = set(), [start]
    anak=[]
    tujuan='Giurgiu'
    nomor=1
    while queue:
        X = queue.pop(0)

        print 'Langkah ke ', nomor
        print 'X : ', X
        print 'Open : ', queue

        if X == tujuan:
            print 'Solusi tercapai'
            return
        else:
            anak = graph2[X]
            print 'Children : ', list(anak)
            #closed.add(vertex)
            if X not in visited:
                visited.add(X)
                queue.extend(graph[X] - visited)
            print 'Closed : ', list(visited)
            print'======================\n'
            nomor=nomor+1
    return #visited


bfs(graph2, 'Arad') # {'B', 'C', 'A', 'F', 'D', 'E'}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

#list(bfs_paths(graph2, 'Arad', 'Bucharest')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

