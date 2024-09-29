using System.Collections.Generic;


namespace Graph
{
    // Weighted and weighted undirected graph
    public class UndirectedGraph : Graph
    {
        
        public List<List<int>> AdjacencyList { get; private set; }

        public UndirectedGraph(int vertices) : base(vertices)
        {
            AdjacencyList = new List<List<int>>(vertices);
            for (int i = 0; i < vertices; i++)
            {
                AdjacencyList.Add(new List<int>());
            }
        }

        public override void AddVertex()
        {
            AdjacencyList.Add(new List<int>());
            verticesCount++;
        }

        public override void RemoveVertex(int vertex)
        {
            foreach (var neighbor in AdjacencyList[vertex])
            {
                AdjacencyList[neighbor].Remove(vertex);
                edgesCount--;
            }
            AdjacencyList.RemoveAt(vertex);
            verticesCount--;
        }

        public override void AddEdge(int vertex1, int vertex2, int weight = 1)
        {
            if (!AdjacencyList[vertex1].Contains(vertex2))
            {
                AdjacencyList[vertex1].Add(vertex2);
                AdjacencyList[vertex2].Add(vertex1);  // в обидві сторони
                edgesCount++;
            }
        }

        public override void RemoveEdge(int vertex1, int vertex2)
        {
            if (AdjacencyList[vertex1].Contains(vertex2) && AdjacencyList[vertex2].Contains(vertex1))
            {
                AdjacencyList[vertex1].Remove(vertex2);
                AdjacencyList[vertex2].Remove(vertex1);
                edgesCount--;
            }
        }
    }
}
