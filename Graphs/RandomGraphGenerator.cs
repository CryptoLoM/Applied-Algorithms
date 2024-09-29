using System;


namespace Graph
{
    public class RandomGraphGenerator
    {
        public static UndirectedGraph GenerateRandomUndirectedGraph(int vertices, double probability)
        {
            Random rand = new Random();
            UndirectedGraph graph = new UndirectedGraph(vertices);

            for (int i = 0; i < vertices; i++)
            {
                for (int j = i + 1; j < vertices; j++)
                {
                    if (rand.NextDouble() < probability)
                    {
                        graph.AddEdge(i, j);
                    }
                }
            }

            return graph;
        }

        public static DirectedGraph GenerateRandomDirectedGraph(int vertices, double probability)
        {
            Random rand = new Random();
            DirectedGraph graph = new DirectedGraph(vertices);

            for (int i = 0; i < vertices; i++)
            {
                for (int j = 0; j < vertices; j++)
                {
                    if (i != j && rand.NextDouble() < probability)
                    {
                        graph.AddEdge(i, j);
                    }
                }
            }

            return graph;
        }
    }
}
