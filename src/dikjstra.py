def Dijkstra(graph, start, end, visited=[], dist={}, pred={}):
    if start == end:
        path = []
        temp_pred = end
        while temp_pred != None:
            path.append(temp_pred)
            temp_predecessor.get(temp_pred, None)
        print ("Shortest path is: " + str(path))
    else:
        if not visited:
            dist[start] = 0
        for ng in graph[start]:
            if ng not in visited:
                new_dist = dist[start] + graph[start][ng]
                if new_dist < dist.get(ng, float('inf')):
                    dist[ng] = new_dist
                    pred[ng] = start
        visited.append(start)
        nonvisited = {}
        for a in graph:
            if a not in visited:
                nonvisited[a] = dist.get(a, float('inf'))
        new_start = min(nonvisited, key = nonvisited.get)
        Dijkstra(graph, new_start, visited, dist, pred)
