#include <stdio.h>
#include <stdbool.h>

bool afundou(int l, int c, int n, int m, char tab[][m])
{
    int main()
    {
        int k;
        scanf("%d %d", &n, &m);
        char tab[n][m];
        for(l = 0; l < n; l++)
        {
            for(c = 0; c < m; c++)
            {
                scanf(" %s", tab[l][c]);
            }
        }

        /*scanf("%d", &k);
        char tiro[k][2];
        for(l = 0; l < k; l++)
        {
            for(c = 0; c < 2; c++)
            {
                scanf(" %s", tiro[l][c]);
                if(tiro[l][c] == '#')
                {
                    tab[l][c] = '*';
                }
            }
        }*/
    }
}
