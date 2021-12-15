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
    int last1, last2, last3;
    fscanf(f, "%d", &last3);
    fscanf(f, "%d", &last2);
    fscanf(f, "%d", &last1);
    while (fscanf(f, "%d", &num) != EOF) {
        int lastSum = last1 + last2 + last3;
        int newSum = num + last1 + last2;
        if (newSum > lastSum) {
            count++;
        }
        last3 = last2;
        last2 = last1;
        last1 = num;
    }

    printf("%d\n", count);

    printf("Done\n");
    fclose(f);
}