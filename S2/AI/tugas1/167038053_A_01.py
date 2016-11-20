def bfs(graph, start):
    closed, open = set(), [start]
    #closed, queue = [], [start]
    anak=[]
    tujuan='Bucharest'
    nomor=1
   
    while open:
        X = open.pop(0)

        print 'Langkah ke ', nomor
        print'======================\n'
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


bfs(adjecency, 'Arad') 