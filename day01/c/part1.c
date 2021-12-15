#include <unistd.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

#define PATH "/home/ben/advent-of-code-2021/day01/input.txt"

int main(void) {
    FILE* f = fopen(PATH, "r");

    int count = 0;
    int num;
    int last;
    fscanf(f, "%d", &last);
    while (fscanf(f, "%d", &num) != EOF) {
        if (num > last) {
            count++;
        }
        last = num;
    }

    printf("%d\n", count);

    printf("Done\n");
    fclose(f);
}