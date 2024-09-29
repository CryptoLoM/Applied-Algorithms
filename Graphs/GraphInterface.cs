using System;


namespace Graph
{
    public static class GraphVisualizer
    {
        public static void VisualizeAsMatrix(int[,] matrix)
        {
            Console.WriteLine("A graph in the form of an adjacency matrix:");
            int vertices = matrix.GetLength(0);

            for (int i = 0; i < vertices; i++)
            {
                for (int j = 0; j < vertices; j++)
                {
                    Console.Write(matrix[i, j] + "\t");
                }
                Console.WriteLine();
            }
        }

        public static void VisualizeAsEdgeList(UndirectedGraph graph)
        {
            Console.WriteLine("A graph in the form of a list of edges:");
            for (int i = 0; i < graph.AdjacencyList.Count; i++)
            {
                foreach (int neighbor in graph.AdjacencyList[i])
                {
                    // Для того щоб уникнути повторів, виводимо лише у одному напрямку
                    if (i < neighbor)
                    {
                        Console.WriteLine($"{i} -- {neighbor}");
                    }
                }
            }
        }   
    }

    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Generation of a random undirected graph...");
            var randomGraph = RandomGraphGenerator.GenerateRandomUndirectedGraph(5, 0.4);

            // Граф у вигляді матриці суміжності
            int[,] adjacencyMatrix = GraphConverter.ConvertAdjacencyListToMatrix(randomGraph.AdjacencyList);
            GraphVisualizer.VisualizeAsMatrix(adjacencyMatrix);

            // Граф у вигляді списку ребер
            GraphVisualizer.VisualizeAsEdgeList(randomGraph);

        }
    }
}
