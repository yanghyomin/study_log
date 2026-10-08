#include <stdio.h>

// 버블정렬 향상버전
void bubbleSort(int arr[], int n){
    int count_compare = 0;
    int count_swap = 0;
    for (int i = 0;i<n-1;i++){
        int change = 0;
        for (int j = 0;j<n-1-i;j++){
            count_compare++;
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                count_swap++;
                change = 1;
            }
        }
        if (change == 0){
            break;
        }
    }
    printf("버블정렬 : count_compare = %d, count_swap = %d\n", count_compare,count_swap);
}

// 선택정렬 향상버전
void selectionSort(int arr[], int n) {
    int count_compare = 0;
    int count_swap = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            count_compare++;
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // 최소값 위치 교환 (Swap)
        if (minIndex != i){ // 젤 작은게 자리자리라면 굳이 교환안함
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
            count_swap++;
        }
    }
    printf("선택정렬 : count_compare = %d, count_swap = %d\n", count_compare,count_swap);
}

int main() {
    int arr1[] = {4,1,7,3,8,2,6,5};
    int arr2[] = {4,1,7,3,8,2,6,5};
    int n = sizeof(arr1) / sizeof(arr1[0]);


    selectionSort(arr1, n);
    bubbleSort(arr2, n);

    printf("---\n");


    printf("선택정렬 : ");
    for (int i =0; i < n-1;i++){
        printf("%d", arr1[i]);
    }
    printf("\n");
    printf("버블정렬 : ");
    for (int i =0; i < n-1;i++){
        printf("%d", arr2[i]);
    }
    return 0;
}