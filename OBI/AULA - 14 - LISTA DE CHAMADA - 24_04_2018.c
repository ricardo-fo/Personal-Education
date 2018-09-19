#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void * i, const void * j)
{
    int * x = (char *)i;/* '*' é o ponteiro*/
    int * y = (char *)j;
    return strcmp(x,y);/*funcao para comparar*/
}

int main()
{
    int n, i, s;

    scanf("%d", &n);
    scanf("%d", &s);

    char alunos[n][21];

    for(i = 0; i < n; i++)
    {
        scanf(" %s", alunos[i]);
    }
    qsort(alunos, n, sizeof(char [21]), compare);
    printf("\n%s\n", alunos[s-1]);
}
