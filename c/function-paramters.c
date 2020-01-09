#include <stdio.h>
#include <stdlib.h>

#define SUM(x,y) (x + y)

void printSumWithMacro(int a, int b);

int main(){
    int a = 9;
    int b = 5;
    printf("Sum of %d + %d = ", a, b);
    printSumWithMacro(a, b)
        printSumWithMacro(a, b);
    return 0;
}

void printSumWithMacro(int a, int b){
    printf("%d",SUM(a, b));
}
