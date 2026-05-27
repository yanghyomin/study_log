// 2026-05-27

#include <stdio.h>

// c언어 포인터 코드
int main(void){
    int a[5] = {10,20,30,40,50};
    int *ptr = a;  //*ptr = 10 을 의미.
    int *ptr2 = a + 3;
    printf("%ld\n", ptr2 - ptr);
    if(ptr2 > ptr) {
        printf("ptr2 > ptr\n");
    }
    else {
        printf("ptr2 <= ptr\n");
    }
    return 0;
}