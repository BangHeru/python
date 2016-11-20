def bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  open=[start]
  closed=[]

  while open:
    X=open.pop(0)
    print 'X : ',X
    print 'Open : ',open
    print 'Children :',open
    closed.append(X)
    print 'Closed : ',closed
    if not X in path:
      path=path+[X]
      open=open+graph[X]
  return path


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
#print 'recursive dfs ', recursive_dfs(graph, 'A')
#print 'iterative dfs ', iterative_dfs(graph, 'A')
#print 'Breadth-first search : ', bfs(graph, 'Arad')

bfs(graph, 'Arad')