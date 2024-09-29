using System.Collections.Generic;


namespace Graph
{
    public class GraphConverter
    {
        public static List<Dictionary<int, int>> ConvertMatrixToAdjacencyList(int[,] matrix)
        {
            int vertices = matrix.GetLength(0);
            List<Dictionary<int, int>> adjacencyList = new List<Dictionary<int, int>>(vertices);

            for (int i = 0; i < vertices; i++)
            {
                adjacencyList.Add(new Dictionary<int, int>());
                for (int j = 0; j < vertices; j++)
                {
                    if (matrix[i, j] != 0)
                    {
                        adjacencyList[i].Add(j, matrix[i, j]);
                    }
                }
            }

            return adjacencyList;
        }

        public static int[,] ConvertAdjacencyListToMatrix(List<Dictionary<int, int>> adjacencyList)
        {
            int vertices = adjacencyList.Count;
            int[,] matrix = new int[vertices, vertices];

            for (int i = 0; i < vertices; i++)
            {
                foreach (var neighbor in adjacencyList[i])
                {
                    matrix[i, neighbor.Key] = neighbor.Value;
                }
            }

            return matrix;
        }

        public static int[,] ConvertAdjacencyListToMatrix(List<List<int>> adjacencyList)
        {
            int vertices = adjacencyList.Count;
            int[,] matrix = new int[vertices, vertices];

            for (int i = 0; i < vertices; i++)
            {
                foreach (var neighbor in adjacencyList[i])
                {
                    matrix[i, neighbor] = 1; 
                }
            }

            return matrix;
        }
    }
}
