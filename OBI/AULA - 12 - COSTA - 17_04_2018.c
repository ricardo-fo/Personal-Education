#include <stdio.h>

int main()
{
    int l, c, i, j, cont = 0;

    scanf("%d %d", &l, &c);

    char str[l][c];

    for(i = 0; i < l; i++)
    {
        scanf(" %s", str[i]);
    }
    for(i = 0; i < l; i++)
    {
        for(j = 0; j < c; j++)
        {
            if((str[i][j]) == '#')
            {
                if(i == 0 || i == l-1 || j == 0 || j == c-1 ||
                   str[i-1][j] == '.' || str[i+1][j] == '.' ||
                   str[i][j-1] == '.' || str[i][j+1] == '.')
                {
                    cont++;
                }
            }
        }
    }
    printf("%d\n", cont);

    return 0;
}
