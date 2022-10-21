#include <stdio.h>
#include <math.h>    // fmod 함수가 선언된 헤더 파일

int main()
{
    // 실수의 나머지 연산은 fmod, fmodf, fmodl 함수를 사용

    double num1 = 10.843;
    double num2 = 3.79;
    printf("%f\n", fmod(num1, num2));    // 3.263000

    float num3 = 10.843f;
    float num4 = 3.79f;
    printf("%f\n", fmodf(num3, num4));    // 3.263000

    long double num5 = 10.843l;
    long double num6 = 3.79l;
    printf("%Lf\n", fmodl(num5, num6));    // 3.263000


 
    if (num1 == 10)    // num1이 10이면
    {
        printf("10입니다.\n");    // "10입니다."를 출력
    }
    else if (num1 == 11)
    {
        printf("메롱.\n")
    }
    else{
        printf("10이 아닙니다.\n");
    }

    printf("%d\n", num1 == 10);    // 1: num1이 10과 같은지
    printf("%d\n", num1 != 5);     // 1: num1이 5와 다른지




    return 0;
}



//gcc 10.c -lm -o app_test