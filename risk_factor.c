#include <stdio.h>
#include <stdlib.h>

int main() {
    char state[3];
    char command[256];

    printf("Enter state abbreviation (e.g., CA): ");
    scanf("%2s", state);

    // Build command
    snprintf(
        command,
        sizeof(command),
        "python3 main.py %s",
        state
    );

    // Execute Python script
    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        perror("Failed to run Python script");
        return 1;
    }

    char result[128];
    fgets(result, sizeof(result), fp);
    pclose(fp);

    printf("Cancer risk for %s: %s per 100,000\n", state, result);

    return 0;
}
