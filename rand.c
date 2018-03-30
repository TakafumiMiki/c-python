#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){
    int i,ran;
    int b = 0;
    srand((unsigned)time(NULL));
    for(i = 0;i<10000;i++){
        if(rand()%101 == 100){
            b++;
        }
    }
    printf("%d",b);
    return 0;
}