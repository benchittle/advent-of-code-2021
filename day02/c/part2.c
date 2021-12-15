#include <unistd.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

#define PATH "/home/ben/advent-of-code-2021/day02/input.txt"

int main(void) {
    FILE* f = fopen(PATH, "r");

    char buf[16];
    int depth = 0;
    int horiz = 0;
    int aim = 0;
    while (fgets(buf, sizeof(buf), f) != NULL) {
        char word[8];
        int amount;
        sscanf(buf, "%s %d", word, &amount);

        switch(word[0]) {       // We only need to consider the first character to distin
            case 'f':
                horiz += amount;
                depth += aim * amount;
                break;
            case 'd':
                aim += amount;
                break;
            case 'u':
                aim -= amount;
                break;
        }
    }

    printf("%d\n", depth * horiz);
    printf("Done\n");
    fclose(f);
}