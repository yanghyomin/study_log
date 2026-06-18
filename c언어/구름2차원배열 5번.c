// 2026-06-18

/* 문제 : 
정수 n을 입력 받아 1~n*n까지 2차원 배열을 지정한 후 사각 테두리에 있는 배열 값들만 합하여 결과를 출력하는 프로그램을 작성하시오.

단, 사각 테두리를 합하는 과정은 함수로 작성하시오.

예를 들어, n = 3이라면

1 2 3
4 5 6
7 8 9

이 중 테두리인 1+2+3+4+6+7+8+9 = 40을 출력한다.

입력

정수 값 n이 입력 된다. (1 <= n <= 100)

출력

테두리의 합이 출력 된다. */





#include <stdio.h>
#include <stdlib.h>

int side_sum(int **arr, int n) {
    int sum = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
                sum += arr[i][j];
            }
        }
    }
    
    return sum;
}
int main() {
    int n;
    
    if (scanf("%d", &n) != 1) return 0;
    
    int **arr = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; i++) {
        arr[i] = (int *)malloc(sizeof(int) * n);
    }
    
    int num = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            arr[i][j] = num++;
        }
    }
    printf("%d", side_sum(arr, n));
}