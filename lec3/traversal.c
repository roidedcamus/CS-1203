#include <stdio.h>
#include <stdbool.h>

typedef char* string;

//create maze using pointer nodes
//intitialize AM to all false and parents array to all -1
//define stack operations
//traverse function - takes root as input, maintains a stack - pops top, adds adjacent of popped( if p[i] == -1), also updates AM)
// repeats till dead end/exit reached, then returns top of stack
// show path using returned value and AM + array

#define N 10;
bool matrix[N][N];
int parents[N];

void main()
{

}

void start(bool am[][], int p[])
{
    for (int i = 0; i < N; i++)
    {
        p[i] = -1;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            matrix[i][j] = F;
        }
    }
}
