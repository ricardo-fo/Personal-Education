#include <stdio.h>
#include <ctype.h>

int main()
{
    char str[31];
    int cont = 0, i;

    scanf("%[^\n]", str);

    for(i = 0; str[i] != '\0'; i++)/*VARRE A STRING*/
    {
        //if(str[i] >= 'A' && str[i]<='Z')/*PROCURA POR MAIUSCULAS*/
        //{
            if(isupper(str[i]))/*PROCURA POR MAIUSCULAS - "is upper ?" - */
            {
                cont++;
            }
        //}
    }
    printf("%d", cont);
    return 0;
}
