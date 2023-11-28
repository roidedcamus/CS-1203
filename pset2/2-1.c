#include<stdio.h>

void main()
{
    char str[100];
    int i;
    scanf("%s", str);
    for(i=0;str[i]!=NULL;i++)
    {
        if (str[i] != 'x' || str[i] != 'y')
        {
            printf("%c", str[i]);
        }
    }
}