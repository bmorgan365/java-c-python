#include <stdio.h>
#include <stdlib.h>

int swap(int x, int y, int* a);

int main(){
    const int ARR_SIZE = 10;
    int array[] = {4, 7, 3, 0, 6, 10, 29, 16, 11, 1};

    int min = 0;
    for(int i = 0; i < ARR_SIZE-1; i++){
        min = i;
        for(int j = i+1; j < ARR_SIZE; j++){
            if(array[j] <= array[min]){
                min = j;
            }
        }
        swap(i, min, array);
    }

    for(int i = 0; i < ARR_SIZE; i++){
        printf("%d ", array[i]);
    }
    return 0;
}

int swap(int x, int y, int* a){
    printf("in swap\n");
    int t = a[x];
    a[x] = a[y];
    a[y] = t;
}
