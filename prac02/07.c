#include <stdio.h>

int main()
{
    char c1 = 97;    // a의 ASCII 코드값 97 저장
    char c2 = 98;    // b의 ASCII 코드값 98 저장

    // char를 %c로 출력하면 문자가 출력되고, %d로 출력하면 정숫값이 출력됨
    printf("%c, %d\n", c1, c1); // a, 97
    printf("%c, %d\n", c2, c2); // b, 98


    char c3 = '0';    // 문자 0을 저장
    char c4 = 0;      // 숫자 0을 저장

    printf("%c %d\n", c3, c3);    // 0 48: 문자 상태로 0이 출력됨
                                  // 문자 0의 ASCII 코드 48이 출력됨

    printf("%c %d\n", c4, c4);    // 0: ASCII 코드 0은 널문자이므로 아무것도 출력되지 않음
                                  // 정수 0이 출력됨


    printf("%c %d\n", 'a' + 1, 'a' + 1);    // b 98: a는 ASCII 코드값 97이고, 
                                            // 97에 1을 더하여 98이 되었으므로 b가 출력됨

    printf("%c %d\n", 97 + 1, 97 + 1);      // b 98: ASCII 코드값 97에 1을 더하여 98이 되었으므로 
                                            // b가 출력됨


    char c5 = 'a';           // 문자 a 할당
    char c6 = 'b';           // 문자 b 할당 
    char lineFeed = '\n';    // 제어 문자 \n 할당

    printf("%c%c%c%c", c5, lineFeed, c6, lineFeed);    // 제어 문자도 %c로 출력할 수 있음



    printf("%d\n", 10);                 // 10: 정수 리터럴
    printf("%f\n", 0.1f);               // 0.100000: 실수 리터럴
    printf("%c\n", 'a');                // a: 문자 리터럴
    printf("%s\n", "Hello, world!");    // Hello, world!: 문자열 리터럴

    printf("%d\n", 19);        // 19: 10진 정수 리터럴
    printf("0%o\n", 017);      // 017: 8진 정수 리터럴
    printf("0x%X\n", 0x1F);    // 0x1F: 16진 정수 리터럴

    printf("%f\n", 0.1f);       // 0.100000: 실수 리터럴 소수점 표기
    printf("%f\n", 0.1F);       // 0.100000: 실수 리터럴 소수점 표기
    printf("%f\n", 1.0e-5f);    // 0.000010: 실수 리터럴 지수 표기법
    printf("%f\n", 1.0E-5F);    // 0.000010: 실수 리터럴 지수 표기법

    const int con1 = 1;         // 상수. 선언과 동시에 초기화
    const float con2 = 0.1f;    // 상수. 선언과 동시에 초기화
    const char con3 = 'a';      // 상수. 선언과 동시에 초기화

    printf("%d %f %c\n", con1, con2, con3);    // 1 0.100000 a



    return 0;
}