using System.Collections.Generic;


namespace Graph
{
    //weighted and unweighted directed graph
    public class DirectedGraph : Graph
    {
        protected List<List<int>> adjacencyList;

        public DirectedGraph(int vertices) : base(vertices)
        {
            adjacencyList = new List<List<int>>(vertices);
            for (int i = 0; i < vertices; i++)
            {
                adjacencyList.Add(new List<int>());
            }
        }

        public override void AddVertex()
        {
            adjacencyList.Add(new List<int>());
            verticesCount++;
        }

        public override void RemoveVertex(int vertex)
        {
            foreach (var neighbor in adjacencyList[vertex])
            {
                adjacencyList[neighbor].Remove(vertex);
                edgesCount--;
            }
            adjacencyList.RemoveAt(vertex);
            verticesCount--;
        }

        public override void AddEdge(int vertex1, int vertex2, int weight = 1)
        {
            if (!adjacencyList[vertex1].Contains(vertex2))
            {
                adjacencyList[vertex1].Add(vertex2);
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