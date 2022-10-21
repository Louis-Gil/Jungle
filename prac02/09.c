#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
    int num1, num2;

    printf("정수를 입력하세요: ");
    scanf("%d %d", &num1, &num2);    // 표준 입력을 받아서 변수에 저장

    printf("%d %d\n", num1, num2);    // 변수의 내용을 출력


    float num3;

    printf("실수를 입력하세요: ");
    scanf("%f", &num3);    // 실수를 입력받아서 변수에 저장

    printf("%f\n", num3);    // 변수의 내용을 출력


    char c1;

    printf("문자를 입력하세요: ");
    scanf("%c", &c1);    // 문자를 1글자만 입력받아서 변수에 저장

    printf("%c\n", c1);    // 변수의 내용을 출력


    char c2 = getchar();    // 문자 하나를 입력받음

    printf("%c\n", c2);


    char c3 = 'a';

    putchar(c3);
    
    return 0;
}