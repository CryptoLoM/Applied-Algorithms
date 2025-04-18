package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

// Структура для зберігання графу
type Graph struct {
	numVertices int
	edges       [][]int
}

// Функція для створення нового графу
func NewGraph(numVertices int) *Graph {
	g := &Graph{numVertices: numVertices}
	g.edges = make([][]int, numVertices)
	for i := range g.edges {
		g.edges[i] = make([]int, numVertices)
		for j := range g.edges[i] {
			if i != j {
				g.edges[i][j] = math.MaxInt32 // Ініціалізація нескінченністю
			}
		}
	}
	return g
}

// Додавання ребра
func (g *Graph) AddEdge(from, to, weight int) {
	g.edges[from][to] = weight
	g.edges[to][from] = weight // Для неорієнтованого графу
}

// Алгоритм Дейкстри для знаходження найкоротших шляхів від заданої вершини
func (g *Graph) Dijkstra(start int) []int {
	dist := make([]int, g.numVertices)
	visited := make([]bool, g.numVertices)

	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[start] = 0

	for i := 0; i < g.numVertices; i++ {
		u := -1
		for j := 0; j < g.numVertices; j++ {
			if !visited[j] && (u == -1 || dist[j] < dist[u]) {
				u = j
			}
		}

		if dist[u] == math.MaxInt32 {
			break
		}

		visited[u] = true
		for v := 0; v < g.numVertices; v++ {
			if g.edges[u][v] != math.MaxInt32 && dist[u]+g.edges[u][v] < dist[v] {
				dist[v] = dist[u] + g.edges[u][v]
			}
		}
	}
	return dist
}

// Алгоритм Флойда-Уоршелла для знаходження найкоротших шляхів між усіма парами вершин
func (g *Graph) FloydWarshall() [][]int {
	dist := make([][]int, g.numVertices)
	for i := range dist {
		dist[i] = make([]int, g.numVertices)
		for j := range dist[i] {
			dist[i][j] = g.edges[i][j]
		}
	}

	for k := 0; k < g.numVertices; k++ {
		for i := 0; i < g.numVertices; i++ {
			for j := 0; j < g.numVertices; j++ {
				if dist[i][k] < math.MaxInt32 && dist[k][j] < math.MaxInt32 && dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	return dist
}

// Генерація графа для тестування
func GenerateGraph(random *rand.Rand, numVertices, density int) *Graph {
	g := NewGraph(numVertices)
	for i := 0; i < numVertices; i++ {
		for j := i + 1; j < numVertices; j++ {
			if random.Intn(100) < density {
				weight := random.Intn(10) + 1
				g.AddEdge(i, j, weight)
			}
		}
	}
	return g
}

// Функція для створення діаграми
func createChart(dijkstraTime, floydTime int64) {
	bar := charts.NewBar()
	bar.SetGlobalOptions(charts.WithTitleOpts(opts.Title{
		Title: "Час виконання алгоритмів",
	}))

	// Додавання даних у графік
	bar.SetXAxis([]string{"Дейкстра", "Флойд-Уоршелл"}).
		AddSeries("Час (мс)", []opts.BarData{
			{Value: dijkstraTime},
			{Value: floydTime},
		})

	// Збереження графіку у файл
	f, err := os.Create("output_chart.html")
	if err != nil {
		fmt.Println("Помилка створення файлу:", err)
		return
	}
	defer f.Close()

	bar.Render(f)
	fmt.Println("Діаграма створена: output_chart.html")
}

// Функція для тестування алгоритмів
func TestAlgorithms(random *rand.Rand) {
	numVertices := 100
	density := 30 // Щільність графу в процентах

	g := GenerateGraph(random, numVertices, density)

	// Тестування алгоритму Дейкстри
	start := time.Now()
	for i := 0; i < numVertices; i++ {
		g.Dijkstra(i)
	}
	elapsedDijkstra := time.Since(start).Milliseconds()

	// Тестування алгоритму Флойда-Уоршелла
	start = time.Now()
	g.FloydWarshall()
	elapsedFloydWarshall := time.Since(start).Milliseconds()

	fmt.Printf("Час виконання Дейкстри: %d мс\n", elapsedDijkstra)
	fmt.Printf("Час виконання Флойда-Уоршелла: %d мс\n", elapsedFloydWarshall)

	// Створення діаграми
	createChart(elapsedDijkstra, elapsedFloydWarshall)
}

func main() {
	// Create a new random source
	source := rand.NewSource(time.Now().UnixNano())
	random := rand.New(source)

	TestAlgorithms(random)
}
