#include <stdio.h>
#include <string.h>


int main(void)
{
    char input[5] = "Love";
    printf("문자열의 길이 : %d\n", strlen(input));


    char inputOne[5] = "A";
    char inputTwo[5] = "B";
    printf("문자열 비교 : %d\n", strcmp(inputOne, inputTwo));

    char input1[10] = "I love You";
    char result[5] = "Love";
    strcpy(result, input1);
    printf("문자열 복사 : %s\n", result);
    // 문자열의 포인터 자체를 복사

    return 0;
}