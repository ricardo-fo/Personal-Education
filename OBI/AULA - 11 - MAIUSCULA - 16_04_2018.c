#include <stdio.h>
#include <string.h>

int main ()
{
    int i, j;
    char numero[16];

    scanf("%s", numero);
    for(i = 0; numero[i] != '\0'; i++)
    {
        if(numero[i] >= 'A' && numero[i] <= 'Y')
        {
            switch (numero[i])
            {
            case 'A' || 'B' || 'C':
                numero[i] = 2;
            break;

            case 'D' || 'E' || 'F':
                numero[i] = 3;
            break;

            case 'G' || 'H' || 'I':
                numero[i] = 4;
            break;

            case 'J' || 'K' || 'L':
                numero[i] = 5;
            break;

            case 'M' || 'N' || 'O':
                numero[i] = 6;
            break;

            case 'P' || 'Q' || 'R' || 'S':
                numero[i] = 7;
            break;

            case 'T' || 'U' || 'V':
                numero[i] = 8;
            break;

            case 'W' || 'X' || 'Y':
                numero[i] = 9;
            break;
            }
        }
    }


    return 0;
}
