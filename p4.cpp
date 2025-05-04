#include <iostream>
using namespace std;

bool is_palindrome(int num) {
    int rev = 0;
    int temp = num;
    while (temp > 0) {
        rev *= 10;
        rev += temp % 10;
        temp = temp / 10;
    }
    return rev == num;
}

void check_pal() {
    int largest = 0;
    for (int i = 999; i >= 100; --i) {
        for (int j = i; j >= 100; --j) {
            int prod = i * j;
            if (prod <= largest) {
                break;
            }
            if (is_palindrome(prod)) {
                largest = prod;
            }
        }
    }
    cout << "Largest possible palindrome from the product of two 3 digit numbers: " << largest;
}

int main() {
    check_pal();
    return 0;
}