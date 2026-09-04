#include <stdio.h>
int linearSearch(int arr[], int size, int target, int *count);

int linearSearch(int arr[], int size, int target, int *count){
    for (int i = 0; i<size;i++){
        *count += 1;
        if (arr[i] == target){
            return i;
            break;
        }
    }
    return -1;
}

int main(){
    int arr[] = {13,8,27,4,19};
    int size = sizeof(arr)/sizeof(arr[0]);
    int target;
    int count =0;

    printf("찾을숫자 입력 : ");

    scanf("%d", &target);

    int result = linearSearch(arr,size,target,&count);
    if (result == -1){
        printf("비교횟수 : %d\n", count);
        printf("%d는 배열에 없습니다.\n",target);
    }
    else {
        printf("비교횟수 : %d\n", count);
        printf("%d는 %d번째 인덱스에서 찾았습니다.\n",target, result);
    }
    return 0;
}


// 자연어 : i = 0, 배열의 인덱스 i번째가 타겟인지 찾는다 아니면 i++;

/* 의사코드 : for 모든 원소
                if 찾았다
                    return 위치
            return -1
*/
                