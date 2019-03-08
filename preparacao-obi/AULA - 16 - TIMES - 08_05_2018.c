#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[51];
    int hab;
    int time;
} talunos;

int compara_hab (const void *, const void *);
int compara_time (const void *, const void *);

int main()
{
    int tim, num, i;

    scanf("%d %d", &num, &tim);

    talunos aluno[num];

    for(i = 0; i < num; i++)
    {
        scanf(" %s %d", aluno[i].nome, &aluno[i].hab);
    }
    qsort(aluno, num, sizeof(talunos), compara_hab);

    for(i = 0; i < num; i++)
    {
        aluno[i].time = i % tim + 1;
    }
    qsort(aluno, num, sizeof(talunos), compara_time);
    for(i = 0; i < num; i++)
    {
        printf("%d %s\n", aluno[i].time, aluno[i].nome);
    }
}

int compara_hab(const void * a, const void * b)
{
    talunos * x = (talunos *) a;
    talunos * y = (talunos *) b;
    return y->hab - x->hab;
}

int compara_time(const void * a, const void *b)
{
    talunos * x = (talunos *) a;
    talunos * y = (talunos *) b;
    if(x->time < y->time) return -1;
    if(x->time > y->time) return 1;
    return strcmp(x->nome , y->nome);
}
