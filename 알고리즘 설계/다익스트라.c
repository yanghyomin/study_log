// 현재 코드는 정문 입구(A)에서 놀이공원 내 각 시설(A~F)까지 가는 가장 빠른 길(최단 시간)을 찾아주는 코드이다.

# include <stdio.h>

# define INF 99999
# define N 6


int findMinVertex(int dist[], int visited[]){ // 메인에서 만들면 매개변수 필요, int dist[], int visited[]
    int min = INF;
    int minIndex = -1;
    for (int i=0;i<N;i++){
        if(dist[i] < min && !visited[i]){
            min = dist[i];
            minIndex = i;
        }
    }
    return minIndex;
}

void Dijkstra(int graph[][N],int dist[], int visited[]){ // 메인에서 만들면 매개변수 필요
    for(int count=0;count<N;count++){
        int u = findMinVertex(dist,visited);

        if (u == -1){
            break;
        }

        visited[u] = 1;
        for(int v=0;v<N;v++){
            if(graph[u][v] != INF && !visited[v]){
                if(dist[u] + graph[u][v] < dist[v]){
                    dist[v] = dist[u]+ graph[u][v];
                }
            }
        }
    }
}
void printGraph(int dist[],char *start[]){
    printf("시작 정점 : %s\n\n",start[0]);
    for(int i =0;i<N;i++){
        if(dist[i] == INF){
            printf("%s : INF\n",start[i]);
        }
        else{
            printf("%s : %d\n",start[i],dist[i]);
        }
    }
}


int main(){
    int graph[N][N] = {
    // A,   B,   C,   D,   E,   F
    {  0,   5, INF, INF,   7,   9}, // A (0)
    {  5,   0,   2, INF,   4, INF}, // B (1)
    {INF,   2,   0,   6,   6,   4}, // C (2)
    {INF, INF,   6,   0,   1, INF}, // D (3)
    {  7,   4,   6,   1,   0,   8}, // E (4)
    {  9, INF,   4, INF,   8,   0}  // F (5)
    };

    int dist[N];

    int visited[N];

    char *point[1000] = {"정문입구", "롤러코스터", "회전목마", "범퍼카", "푸드코트", "대관람차"};
    for(int i=0;i<N;i++){
        dist[i] = INF;
    }
    dist[0] = 0;

    for(int i=0;i<N;i++){
        visited[i] = 0;
    }

    Dijkstra(graph, dist, visited);
    printGraph(dist,point);

    //정문입구, 롤러코스터, 화전목마, 범퍼카, 푸드코트, 대관람차
}