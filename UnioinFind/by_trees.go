package main

import (
	"fmt"
	"sort"
	"applied-algorithms/unionfind"  
)

// Структура ребра
type Edge struct {
	From, To, Weight int
}

// Сортування ребер за вагою
type ByWeight []Edge

func (e ByWeight) Len() int           { return len(e) }
func (e ByWeight) Less(i, j int) bool { return e[i].Weight < e[j].Weight }
func (e ByWeight) Swap(i, j int)      { e[i], e[j] = e[j], e[i] }

func Kruskal(edges []Edge, numVertices int) (int, []Edge) {
	uf := unionfind.NewUnionFind()   // Використовуємо UnionFind для з'єднання компонент
	uf.UnionFind(numVertices)        // Ініціалізація UnionFind на кількість вершин

	sort.Sort(ByWeight(edges))       // Сортуємо ребра за вагою

	minCost := 0
	var mst []Edge                   // Масив для мінімального кістякового дерева

	for _, edge := range edges {
		// Якщо ребра не утворюють цикл
		if !uf.IsSameSet(edge.From, edge.To) {
			uf.UnionSet(edge.From, edge.To) // Об'єднуємо компоненти
			minCost += edge.Weight          // Додаємо вагу ребра до загальної вартості
			mst = append(mst, edge)         // Додаємо ребро до MST
		}
	}

	return minCost, mst
}

func main() {
	edges := []Edge{
		{0, 1, 4},
		{0, 2, 4},
		{1, 2, 2},
		{1, 3, 6},
		{2, 3, 8},
		{2, 4, 9},
		{3, 4, 7},
	}

	numVertices := 5

	minCost, mst := Kruskal(edges, numVertices)

	fmt.Printf("Мінімальна вартість: %d\n", minCost)
	fmt.Println("Ребра MST:")
	for _, edge := range mst {
		fmt.Printf("%d - %d (вага: %d)\n", edge.From, edge.To, edge.Weight)
	}
}
