#include <stdio.h>

int FactorialRecursive(int n)
{
    if (n==1)
        return 1;
    return FactorialRecursive(n-1)*n;
}

int FactorialLoop(int n)
{
    int i, mult =1;
    for (i=1;i<=n;i++)
        mult *= i;
    return mult;
}

int main(void) {
    printf("4! = %d \n", FactorialRecursive(4));
    printf("4! = %d \n", FactorialLoop(4));
    return 0;
}