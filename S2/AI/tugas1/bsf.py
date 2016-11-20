def bfs(graph, start):
    closed, open = set(), [start]
    #closed, queue = [], [start]
    anak=[]
    tujuan='Bucharest'
    nomor=1
    #print 'Daftar Adjecency\n',adjecency(0),'\n============='
    while open:
        X = open.pop(0)

        print 'Langkah ke ', nomor
        print 'X : ', X
        print 'Open : ', open

        if X == tujuan:
            print 'Solusi tercapai'
            return 
        else:
            anak = graph[X]
            print 'Children : ', list(anak)
            if X not in closed:
                closed.add(X)
                #closed=closed+[X]
                open.extend(graph[X] - closed)
                
            print 'Closed : ', list(closed)
            print'======================\n'
            nomor=nomor+1
    return #closed

#adj = []
#txt = open('adjecency.txt')
#adj =[txt.read()]

adjecency = {
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


bfs(adjecency, 'Arad') # {'B', 'C', 'A', 'F', 'D', 'E'}

graph2 = {
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


graph3 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path
    
    print 'X = ', start
    #print 'Open = ', start.pop(0)
    print 'Children = ', graph[start]
    print 'Closed = ', path
    
    print '=============\n'
    if not graph.has_key(start):
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    		
    return None

#print find_path(graph2, 'Arad', 'Bucharest')



def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

#print list(find_all_paths(graph2, 'Arad', 'Bucharest'))