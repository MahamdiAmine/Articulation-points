#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################

# This class represents an undirected graph  using adjacency list representation
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, nodes):
        self.No_nodes = nodes  # Number of of nodes
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.time = 0
        self.No_AP=0

    # function to convert a matrix into adjacency list.
    def convert_matrix_to_Adj_list(self,matrix):
        for i in range(0, self.No_nodes):
            for j in range(0, self.No_nodes):
                if matrix[i][j]:
                    self.graph[i].append(j)# add an edge to the graph
                    self.graph[j].append(i)# add an edge to the graph

    # The function to do DFS traversal to find all the articulation points .
    def find_Articulation_Points(self):
        self.No_AP=0
        visited = [False] * self.No_nodes# Mark all the nodes as not visited
        discovery_time = [float("Inf")] * self.No_nodes#Initialize the discovery time.
        low = [float("Inf")] * self.No_nodes
        parent = [-1] * self.No_nodes #Initialize parent
        self.articulation_points = [False] * self.No_nodes  # To store articulation points
        for current_node in range(self.No_nodes):
            if not visited[current_node]:
                self.DFS(current_node, visited, self.articulation_points, parent, low, discovery_time)
        for index, value in enumerate(self.articulation_points):
            if value:
                self.No_AP+=1

    def DFS(self, node, visited, articulation_points, parent, low, discovery_time):
        # a vertex u is articulation point if one of the following two conditions :
        # (1): u is root of DFS tree and it has at least two children.
        # (2): u is not root of DFS tree and it has a child v such that no
        #      vertex in subtree rooted with v has a back edge
        #      to one of the ancestors (in DFS tree) of u.
        children = 0 # Count of children in current node
        visited[node] = True # Mark the current node as visited and print it
        # Initialize discovery time and low value
        discovery_time[node] = self.time
        low[node] = self.time
        self.time += 1
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[node]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if not visited[v]:
                parent[v] = node
                children += 1
                self.DFS(v, visited, articulation_points, parent, low, discovery_time)
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[node] = min(low[node], low[v])
                # Condition (1) is verified
                if parent[node] == -1 and children > 1:
                    articulation_points[node] = True
                # Condition (2) is verified.
                if parent[node] != -1 and low[v] >= discovery_time[node]:
                    articulation_points[node] = True
                    # Update low value of u for parent function calls
            elif v != parent[node]:
                low[node] = min(low[node], discovery_time[v])

    def drawGraph(self):
    # draw the graph and represent the vertex with a red color.
        G = nx.from_dict_of_lists(self.graph)
        fig = plt.figure()
        fig.canvas.set_window_title('View the articulation points in the graph ')
        color_map = []
        for node in G:
            if  self.articulation_points[node]:
                color_map.append('red')
            else:
                color_map.append('orange')

        nx.draw(G, with_labels=True, node_color=color_map, node_size=1500, edge_color='white',linewidths=3, font_size=15)
        fig.set_facecolor("#00000F")
        plt.show()