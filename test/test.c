//main.c                                                                        
/* this
 is a comment */
#include <stdio.h>

void swap();

int buf[2] = {0x137, 0x291};

int main() {
    printf("%d, %d\n", buf[0], buf[1]);
    swap();
    printf("%d, %d\n", buf[0], buf[1]);
    return 0;
}
