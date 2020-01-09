#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long int fib(int x);
long long int* memo;

int main(int argc, char** argv){
    int fibval = 0;
    char* arg;
    char newline = '\n';
    if(argc == 1){
        printf("Continuing without terminal entry...\n");
        printf("Enter a fib val: ");
        scanf("%d%c", &fibval, &newline);
    }else if(argc == 2){
        //arg = argv[1];
        fibval = atoi(argv[1]);
        //printf("arg = %s", arg);
        if(argv[1][0] != '0' && fibval == 0){
            printf("Error during atoi() conversion. Exiting...\n");
            return 0;
        }
    }
    
    memo = malloc(sizeof(long long int) * (fibval + 1));
    for(int i = 0; i < fibval + 1; memo[i++] = -1){}
    /*printf("fib\n");
    for(int i = 0; i < fibval; i++){
        printf("%lld", fib(i));
    }*/
    printf("fib(%d): %lld\n", fibval, fib(fibval));
    return 0;
}

long long fib(int x){
    if(x < 0) return 0;
    if(x == 0 || x == 1){
        memo[x] = x;
        return x;
    }
    if(memo[x] != -1) return memo[x];
    long long int ret = fib(x-1) + fib(x-2);
    memo[x] = ret;
    return ret;
}
