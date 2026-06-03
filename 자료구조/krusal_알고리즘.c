// 2026-06-03

// kruskal_알고리즘.c
#include <stdio.h>

#define MAX 4
#define MAX_EDGE 20

typedef struct GraphType {
    int n;
    int adj_mat[MAX][MAX];
} GraphType;

typedef struct Edge {
    int u;
    int v;
    int weight;
} Edge;

int parent[MAX];

void init(GraphType* g) {
    g->n = MAX;

    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            g->adj_mat[i][j] = 0;
        }
    }
}

void insert_edge(GraphType* g, int u, int v, int weight) {
    g->adj_mat[u][v] = weight;
    g->adj_mat[v][u] = weight;
}

void set_init(int n) {
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
}

int find(int x) {
    if (parent[x] == x) {
        return x;
    }

    return parent[x] = find(parent[x]);
}

void union_set(int a, int b) {
    int rootA = find(a);
    int rootB = find(b);

    if (rootA != rootB) {
        parent[rootB] = rootA;
    }
}

void sort_edges(Edge edges[], int edge_count) {
    for (int i = 0; i < edge_count - 1; i++) {
        for (int j = 0; j < edge_count - i - 1; j++) {
            if (edges[j].weight > edges[j + 1].weight) {
                Edge temp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = temp;
            }
        }
    }
}

void kruskal(GraphType* g) {
    Edge edges[MAX_EDGE];
    int edge_count = 0;

    for (int i = 0; i < g->n; i++) {
        for (int j = i + 1; j < g->n; j++) {
            if (g->adj_mat[i][j] != 0) {
                edges[edge_count].u = i;
                edges[edge_count].v = j;
                edges[edge_count].weight = g->adj_mat[i][j];
                edge_count++;
            }
        }
    }

    sort_edges(edges, edge_count);
    set_init(g->n);

    int total_weight = 0;
    int selected_edges = 0;

    printf("Kruskal MST 간선\n");

    for (int i = 0; i < edge_count; i++) {
        int u = edges[i].u;
        int v = edges[i].v;
        int weight = edges[i].weight;

        if (find(u) != find(v)) {
            union_set(u, v);

            total_weight += weight;
            selected_edges++;

            printf("%d - %d : %d\n", u, v, weight);
        }

        if (selected_edges == g->n - 1) {
            break;
        }
    }

    printf("총 가중치 : %d\n", total_weight);
}

int main() {
    GraphType g;

    init(&g);

    insert_edge(&g, 0, 1, 10);
    insert_edge(&g, 0, 2, 6);
    insert_edge(&g, 0, 3, 5);
    insert_edge(&g, 1, 3, 15);
    insert_edge(&g, 2, 3, 4);

    kruskal(&g);

    return 0;
}