#include <stdio.h>
#include <math.h>

struct point{
    int x, y;
};

void comparePoint(struct point p1, struct point p2){
    // p1 과 p2의 직접비교는 다르다!

    if((p1.x == p2.x)&&(p1.y == p2.y))
    {
        printf("p1과 p2가 같습니다.\n");
    }
}

int main(void)
{
    struct point p1;
    struct point p2;

    p1.x = 30;
    p1.y = 10;

    p2.x = 30;
    p2.y = 10;

    comparePoint(p1, p2);
    return 0;
}