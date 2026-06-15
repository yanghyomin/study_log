// 2026-06-15

#include <stdio.h>
int main() {
	int a;
	int temp = 0;
	scanf("%d",&a);
	int arr[a][a];
	for(int i = 0;i < a;i++){
		for(int j = 0;j < a;j++){
			temp += 1;
			arr[i][j] = temp;
		}
	}
	for(int i = 0;i < a;i++){
		for(int j = 0;j < a;j++){
			printf("%d ",arr[i][j]);
		}
		printf("\n");
	}
}

// 입력이 3인 경우 이렇게 출력:
// 1 2 3
// 4 5 6
// 7 8 9