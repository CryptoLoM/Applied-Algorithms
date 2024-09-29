using System.Collections.Generic;

namespace Graph
{
    //weighthed directed graph
    public class DirectedGraph : Graph
    {
        protected List<Dictionary<int, int>> adjacencyList; // 

        public DirectedGraph(int vertices) : base(vertices)
        {
            adjacencyList = new List<Dictionary<int, int>>(vertices);
            for (int i = 0; i < vertices; i++)
            {
                adjacencyList.Add(new Dictionary<int, int>());
            }
        }

        public override void AddVertex()
        {
            adjacencyList.Add(new Dictionary<int, int>());
            verticesCount++;
        }

        public override void RemoveVertex(int vertex)
        {
            
            foreach (var neighbor in adjacencyList[vertex].Keys)
            {
                adjacencyList[neighbor].Remove(vertex);
                edgesCount--;
            }
            adjacencyList.RemoveAt(vertex);
            verticesCount--;
        }

        public override void AddEdge(int vertex1, int vertex2, int weight = 1)
        {
            if (!adjacencyList[vertex1].ContainsKey(vertex2))
            {
                adjacencyList[vertex1][vertex2] = weight; 
                edgesCount++;
            }
        }

        public override void RemoveEdge(int vertex1, int vertex2)
        {
            if (adjacencyList[vertex1].Remove(vertex2))
            {
                edgesCount--;
            }
        }
    }
}
