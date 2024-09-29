namespace Graph
{
    public abstract class Graph
    {
        protected int verticesCount;
        protected int edgesCount;  // Поле для зберігання кількості ребер

        public Graph(int vertices)
        {
            this.verticesCount = vertices;
            this.edgesCount = 0;  // Початкова кількість ребер
        }

        public abstract void AddVertex();
        public abstract void RemoveVertex(int vertex);
        public abstract void AddEdge(int vertex1, int vertex2, int weight = 1);
        public abstract void RemoveEdge(int vertex1, int vertex2);

        // Можна додати методи для отримання кількості вершин та ребер
        public int GetVerticesCount()
        {
            return verticesCount;
        }

        public int GetEdgesCount()
        {
            return edgesCount;
        }
    }
}