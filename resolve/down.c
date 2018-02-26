#include <stdlib.h>
#include <stdio.h>
#include "../engine.c"

int main()
{
    int max,p,mountainH;
    while (1) {
        max=0;
        for (int i = 0; i < 8; i++) {      
            scanf("%d", &mountainH);
            if (mountainH > max) {
                max = mountainH;
                fprintf(stderr,"target my mountain" );
                p = i;
            }
            
        }
        printf("%d\n",p); 
    }
    return 0;
}