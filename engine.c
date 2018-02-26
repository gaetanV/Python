int pointer=-1;
int lock=0;
char *data[100];

int setSeq(char *d)
{
   if(lock == 1){
       exit(2);
   }
   pointer=-1;
   lock=1;
   //TODO
}

int scanf(const char *format, ...){
   //TODO
}

int fprintf(FILE *stream, const char *format, ...)
{
    return 0;
}

int printf(const char *format, ...)
{
    return 0;
}
