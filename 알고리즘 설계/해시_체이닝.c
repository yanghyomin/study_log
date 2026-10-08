#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

struct Node{
    int key;
    struct Node* next;
};

struct Node* table[TABLE_SIZE];

int hash(int key){
    return key % 10;
}

void initTable(){
    for (int i=0; i < TABLE_SIZE;i++){
        table[i] = NULL;
    }
}


// 삽입
void insert(int key){
    int index = hash(key);
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode -> key = key;
    newNode -> next = table[index];
    table[index] = newNode;
}


// 탐색
struct Node* Search(int key){
    int index = hash(key);
    struct Node* current  = table[index];
    while (current != NULL){
        if (current -> key == key){
            return current;
        }
        current = current -> next;
    }
    return NULL;
}

// 식제
struct Node* Delete(int key){
    int index = hash(key);
    struct Node* current  = table[index];
    struct Node* prev = NULL;

    while(current != NULL && current -> key != key){
        prev = current;
        current = current -> next;
    }
    // current가 없음 = 값이 없음
    if (current == NULL){
        return;
    }
    // prev가 없음 = current의 table[index]가 우리가 찾던 값임, 즉 prev의 초기값은 NULL 이므로
    if (prev == NULL){
        table[index] = current -> next; // head 앞으로 옮기기
    }
    // 중간에 있음
    else {
        prev -> next = current -> next; // 삭제할 값 뒤랑 삭제할 값 앞이랑 연결
    }
    free (current);
}