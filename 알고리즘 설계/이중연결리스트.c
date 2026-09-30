#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

void freeList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
}

// 이중 연결 리스트 이진 탐색
Node* binarySearch(Node* head, int size, int target) {
    int low = 0;
    int high = size - 1;

    Node* current = head;
    int currentIndex = 0;

    while (low <= high) {
        int mid = (low + high) / 2;

        // 현재 위치에서 mid 위치로 이동
        while (currentIndex < mid) {
            current = current->next;
            currentIndex++;
        }
        while (currentIndex > mid) {
            current = current->prev;
            currentIndex--;
        }

        if (current->data == target) {
            return current;
        }
        else if (current->data < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    return NULL;
}

void insertBack(Node** head, int data, int* size) {
    Node* newNode = (Node*)malloc(sizeof(Node));

    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
    }
    else {
        Node* current = *head;

        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
    (*size)++;
}

void printfList(Node* head) {
    Node* current = head;
    printf("NULL <-> ");
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;
    int size = 0;
    int target;

    // 이진 탐색을 위해 정렬된 순서로 삽입
    insertBack(&head, 3, &size);
    insertBack(&head, 7, &size);
    insertBack(&head, 12, &size);
    insertBack(&head, 18, &size);
    insertBack(&head, 25, &size);

    printf("target : ");
    scanf("%d", &target);

    Node* result = binarySearch(head, size, target);

    if (result == NULL) {
        printf("못찾음 ㅠㅠ\n");
        printf("리스트 보실? (y/n) : ");
        char answer;
        
        // %c 앞에 공백을 두어 엔터(줄바꿈) 문자 입력 방지
        scanf(" %c", &answer);

        if (answer == 'y' || answer == 'Y') {
            printfList(head);
        }
        else {
            printf("김도윤 바보\n");
        }
    }
    else {
        printf("오 찾았음 주소 : %p\n", (void*)result);
    }

    freeList(head);
    return 0;
}