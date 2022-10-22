#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pi;
    pi = (int *)malloc(sizeof(int));
    if(pi == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.\n");
        exit(1);
    }
    *pi = 100;
    printf("%d\n", *pi);
    free(pi);
    return 0;
}