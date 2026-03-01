#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char state[3];
    char command[256];

    printf("Enter state abbreviation (e.g., CA): ");
    if (scanf("%2s", state) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    for(int i = 0; i < 2; i++) {
        if (state[i] >= 'a' && state[i] <= 'z') state[i] -= 32; // convert to uppercase
    }

    state[2] = '\0'; // ensure null-terminated

    snprintf(command, sizeof(command), "python3 main.py %s", state);

    FILE *fp = popen(command, "r");
    if (!fp) {
        perror("Failed to run Python script");
        return 1;
    }

    char result[128];
    if (fgets(result, sizeof(result), fp) != NULL) {
        result[strcspn(result, "\n")] = 0; // strip newline
        printf("Cancer risk for %s: %s per 100,000\n", state, result);
    }

    pclose(fp);
    return 0;
}
