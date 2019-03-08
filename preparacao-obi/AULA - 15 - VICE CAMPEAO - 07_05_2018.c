#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int min;
    int num;
} tcarro;

int compara (const void *, const void *);

int main ()
{
    int n, m, i, j, t;

    scanf("%d %d", n, m);
    tcarro carro[n];

    for (i = 0; i < n; i++)
    {
        carro[i].num = i + 1;
        carro[i].min = 0;
        for(j = 0; j < m; j++)
        {
            scanf("%d", &t);
            carro[i].min += t;
        }
    }
    qsort(carro, n, sizeof(tcarro), compara);
    for(i = 0; i < 3; i++)
    {
        printf("%d\n", carro[i].num);
    }
    return 0;
}

int compara(const void * a, const void * b)
{
    tcarro * x = (tcarro *) a;
    tcarro * y = (tcarro *) b;
    return x->min - y->min;
}
