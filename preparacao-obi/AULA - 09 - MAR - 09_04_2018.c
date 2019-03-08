#include <stdio.h>
int main()
{
    int matriz[1][4], n, xi, yi;

    scanf("%d", &n);

    for (xi = 0; xi < n; xi++)
    {
        for (yi = 0; yi < 4; yi++)
        {
            scanf("%d", &matriz[xi][yi]);
        }
    }
    printf("Conteudo da matriz:\n");
    for (xi = 0; xi < n; xi++)
    {
        for (yi = 0; yi < 4; yi++)
        {
            printf("%d\t", matriz[xi][yi]);
        }
        printf("\n");
    }


    return 0;
}
