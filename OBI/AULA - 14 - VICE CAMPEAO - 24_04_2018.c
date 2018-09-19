#include <stdio.h>
#include <stdlib.h>

int compare(const void * i, const void * j)
{
    int x = *((int *)i);
    int y = *((int *)j);
    return x - y;
}

int main()
{
    int i;
    int vet[3];

    for(i = 0; i < 3; i++)
    {
        scanf("%d", &vet[i]);
    }
    qsort(vet, 3, sizeof(int), compare);
    printf("%d\n", vet[1]);
}
