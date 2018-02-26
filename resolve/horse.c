#include <stdlib.h>
#include <stdio.h>

int main()
{
    int N,i=0,inf=10000000,tmp;
    scanf("%d", &N);
    int power[N];
    while (i< N) {
        scanf("%d", &tmp);
        power[i] = tmp;
        i++;
    }
    
    inline int more (void const *a, void const *b){return ( *(int*)a - *(int*)b );}
    qsort(power, N, sizeof(int), more);

    for (i = 0; i < N-1; i++) {
        tmp = ( power[i+1] - power[i] );
        if (tmp < inf) {
             inf = tmp;
         }
    }
    printf("%d\n",inf);
    return 0;
}