#include <stdio.h>

int main()
{
    int x, y, l1, h1, l2, h2, t1, t2, t3, t4;

    scanf("%d %d", &x, &y);
    scanf("%d %d", &l1, &h1);
    scanf("%d %d", &l2, &h2);

    t1 = h1 + h2;
    t2 = l1 + l2;
    t3 = h1 + l2;
    t4 = l1 + h2;

    if ((((x >= h1) && (y >= t2)) || ((x >= h2) && (y >= t2))) || ((y >= h1) && (x >= t2)) || ((y >= h2) && (x >= t2)))
    {
        printf("S\n");
    }else{
        printf("N\n");
    }
/*
    if (((x >= h1) && (y >= t4)) || ((y >= h1) && (x >= t4)))
    {
        printf("S\n");
    }else{
        printf("N\n");
    }

    if (((x >= h2) && (y >= t3)) || ((y >= h2) && (x >= t3)))
    {
        printf("S\n");
    }else{
        printf("N\n");
    }

    if ((((x >= l1) && (y >= t1)) || ((x>= l2) && (y >= t1))) || (((y >= l1) && (x >= t1)) || ((y >= l2) && (x >= t1))))
    {
        printf("S\n");
    }else{
        printf("N\n");
    }
*/
    return 0;
}
