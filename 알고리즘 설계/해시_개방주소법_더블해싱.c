// 개방주소법

#include <stdio.h>

#define TABLE_SIZE 11 // 테이블 사이즈 11
#define EMPTY -1
#define DELETED -2

int table[TABLE_SIZE];

int hash1(int key){        // hash1
    return key % TABLE_SIZE;
}

int hash2(int key){       // hash2
    return 1 + (key % 7);
}

int hash3(int key, int i){ // hash3 = hash1 + i * hash2 % TABLE_SIZE
    return (hash1(key) + i * hash2(key) % TABLE_SIZE);
}


void Init(){
    for (int i=0;i<TABLE_SIZE;i++){
        table[i] = EMPTY;
    }
}


void Insert(int key){
    int i = 0;
    int index = hash1(key);

    while (i < TABLE_SIZE){
        if (table[index] == EMPTY || table[index] == DELETED){
            table[index] = key;
            return;
        } // 넘어가면 충돌 발생
        i ++; // i(충돌 횟수)값 추가
        index = hash3(key, i);
    }
    printf("테이블 꽉 참");
}


int Search(int key){
    int i = 0;
    int index = hash1(key);
    while (i < TABLE_SIZE){
        if (table[index] == key){
            return index;
        }
        if (table[index] == EMPTY){
            return -1;
        }
        i++; // 충돌 횟수 증가
        index = hash3(key, i);
    }
    return -1;
}

void DELETE(int key){
    int index = Search(key);
    if (index == -1){
        return;
    }
    else {
        table[index] = DELETED;
    }
}


void PrintTable(){
    int count = 0;
    while (count < TABLE_SIZE){
        printf("[%d] -> ",count);
        if (table[count] == -1){
            printf("EMPTY\n");
        }
        else if (table[count] == -2){
            printf("DELETED\n");
        }

        else {
            printf("%d\n", table[count]);
        }
        count++;
    }
}


int main() { // 테스트 코드
    Init();
    PrintTable();

    printf("=== 1. 충돌 및 이중 해싱 테스트 ===\n");
    Insert(12);
    Insert(23);
    Insert(34);
    PrintTable();
    printf("\n");

    printf("=== 2. 검색 테스트 ===\n");
    printf("키 23 위치 검색: %d (예상: 4)\n\n", Search(23));

    printf("=== 3. 삭제 후 탐색 버그 테스트 ===\n");
    printf("키 12 삭제 수행...\n");
    DELETE(12);
    PrintTable();
    printf("키 23 위치 재검색: %d (DELETED 버그 수정 전에는 -1 반환됨)\n\n", Search(23));

    printf("=== 4. 테이블 가득 채우기 테스트 ===\n");
    Init(); // 테이블 초기화
    int test_keys[] = {1, 12, 23, 34, 45, 56, 67, 78, 89, 90, 101, 112};
    for (int k = 0; k < 12; k++) {
        printf("Insert(%d) -> ", test_keys[k]);
        Insert(test_keys[k]);
        if (k == 11) printf("\n");
    }
    PrintTable();

    return 0;
}