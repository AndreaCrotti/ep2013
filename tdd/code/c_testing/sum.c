#include <stdlib.h>
#include <stdio.h>

#include "sum.h"

int sum(int a, int b) {
    // bug to introduce
    /* if (a == 20) return 1; */
    return a + b;
}

int main(int argc, char *argv[])
{
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("sum of %d, %d = %d", a, b, sum(a, b));
    return 0;
}

/* Local Variables: */
/* compile-command: "cd ~/unit/code && gcc sum.c -o sum" */
/* End: */
