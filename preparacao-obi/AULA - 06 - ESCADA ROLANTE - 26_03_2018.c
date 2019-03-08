#include <stdio.h>

int main ()
{
    int n, t, i, func = 0, soma = 0;

    scanf("%d", &n);

    for(i = 1; i <= n; i++)
    {
        scanf("%d", &t);
        if (t < func)
        {
            soma -= func - t;
        }
        func = t + 10;
        soma += 10;
    }
    printf("%d", soma);

    return 0;
}
