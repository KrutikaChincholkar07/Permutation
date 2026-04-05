#include <stdio.h>

// Function to calculate factorial
int factorial(int num) {
    int fact = 1;
    
    for(int i = 1; i <= num; i++) {
        fact = fact * i; // multiply numbers from 1 to num
    }
    
    return fact;
}

int main() {
    int n, r, result;

    // Taking input from user
    printf("Enter value of n: ");
    scanf("%d", &n);

    printf("Enter value of r: ");
    scanf("%d", &r);

    // Permutation formula: P(n,r) = n! / (n-r)!
    result = factorial(n) / factorial(n - r);

    // Display result
    printf("Permutation P(%d,%d) = %d\n", n, r, result);

    return 0;
}
