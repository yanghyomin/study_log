// 개방주소법

#include <stdio.h>

#define TABLE_SIZE 7
#define EMPTY -1

int table[TABLE_SIZE];

int hash(int key){
    return key % TABLE_SIZE;
}

void Init(){
    for (int i=0;i<TABLE_SIZE;i++){
        table[i] = EMPTY;
    }
}


void Insert(int key){
    int index = hash(key);
    int count = 0;

    while (count < TABLE_SIZE){
        if (table[index] == EMPTY){
            table[index] = key;
            return;
        }
        index = (index + 1) % TABLE_SIZE;
        count++;
    }
    printf("테이블 꽉 참");
}


int Search(int key){
    int index = hash(key);
    int count = 0;
    while (count < TABLE_SIZE){
        if (table[index] == key){
            return index;
        }
        if (table[index] == EMPTY){
            return -1;
        }
        index = (index+1)% TABLE_SIZE;
        count++;
    }
    return -1;
}


void PrintTable(){
    int count = 0;
    while (count < TABLE_SIZE){
        printf("[%d] -> ",count);
        if (table[count] == -1){
            printf("EMPTY\n");
        }
        else {
            printf("%d\n", table[count]);
        }
        count++;
    }
}


int main(){
    Init();

    Insert(10);
    Insert(17);
    Insert(24);

    PrintTable();

}
