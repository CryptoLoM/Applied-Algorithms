package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
	"applied-algorithms/unionfind"
)

type Edge struct {
	From, To, Weight int
}

type ByWeight []Edge

func (e ByWeight) Len() int           { return len(e) }
func (e ByWeight) Less(i, j int) bool { return e[i].Weight < e[j].Weight }
func (e ByWeight) Swap(i, j int)      { e[i], e[j] = e[j], e[i] }

func Kruskal(edges []Edge, numVertices int) (int, []Edge) {
	uf := unionfind.NewUnionFind()
	uf.UnionFind(numVertices)

	sort.Sort(ByWeight(edges))

	minCost := 0
	var mst []Edge

	for _, edge := range edges {
		if !uf.IsSameSet(edge.From, edge.To) {
			uf.UnionSet(edge.From, edge.To)
			minCost += edge.Weight
			mst = append(mst, edge)
		}
	}

	return minCost, mst
}

// Функція для генерації випадкового графа
func generateRandomGraph(numVertices, numEdges int, rng *rand.Rand) []Edge {
	edges := make([]Edge, 0)

	// Спочатку з'єднуємо всі вершини (щоб граф був зв'язним)
	for i := 0; i < numVertices-1; i++ {
		edges = append(edges, Edge{From: i, To: i + 1, Weight: rng.Intn(100)})
	}

	// Додаємо інші випадкові ребра
	for len(edges) < numEdges {
		from := rng.Intn(numVertices)
		to := rng.Intn(numVertices)
		if from != to { // Забороняємо петлі
			weight := rng.Intn(100)
			edges = append(edges, Edge{From: from, To: to, Weight: weight})
		}
	}

	return edges
}

func main() {
	// Створюємо новий генератор випадкових чисел з випадковим seed
	rng := rand.New(rand.NewSource(time.Now().UnixNano()))

	numVertices := 1000 // Приклад з 100 вершинами, але можна змінити

	// Тестування на графах з 10, 100, і 1000 ребрами
	for _, numEdges := range []int{10, 100, 1000} {
		edges := generateRandomGraph(numVertices, numEdges, rng)

		var totalTime int64 = 0
		repeat := 1000 

		for i := 0; i < repeat; i++ {
			start := time.Now()                // Початок вимірювання часу
			Kruskal(edges, numVertices)        
			elapsed := time.Since(start).Microseconds()
			totalTime += elapsed               // Додаємо до загального часу
		}

		avgTime := totalTime / int64(repeat) // Усереднюємо час

		fmt.Printf("Граф з %d вершинами та %d ребрами\n", numVertices, numEdges)
		fmt.Printf("Середній час виконання: %d секунд\n", avgTime)
		fmt.Println()
	}
}
