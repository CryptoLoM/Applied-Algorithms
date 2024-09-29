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
                    // Для того щоб уникнути повторів
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
            Console.WriteLine("Enter the number of vertices in the graph:");
            int numberOfVertices = int.Parse(Console.ReadLine() ?? "0");

            var randomGraph = new UndirectedGraph(numberOfVertices);

            randomGraph.AddEdge(0, 1);
            randomGraph.AddEdge(1, 2);
            randomGraph.AddEdge(0, 2);

            // Конвертуємо список суміжності в матрицю
            int[,] adjacencyMatrix = GraphConverter.ConvertAdjacencyListToMatrix(randomGraph.AdjacencyList);
            // Візуалізація графа у вигляді матриці
            GraphVisualizer.VisualizeAsMatrix(adjacencyMatrix);

            // Підрахунок кількості вершин і ребер
            Console.WriteLine($"Vertices Count: {randomGraph.GetVerticesCount()}");
            Console.WriteLine($"Edges Count: {randomGraph.GetEdgesCount()}");
        }
    }
}