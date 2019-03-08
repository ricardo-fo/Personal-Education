#include <stdio.h>
#include <string.h>

int main()
{
    int i, n, soma = 0;

    scanf("%d", &n);

    char bloco[n + 1];

    scanf(" %s", bloco);

    for(i = 0; bloco[i] != '\0'; i++)
    {
        if((bloco[i] == 'P') || (bloco[i] == 'C'))
        {
            soma += 2;

        }else{
           if(bloco[i] == 'A')
           {
               soma++;
           }
        }
    }
    printf("%d\n", soma);

    return 0;
}
