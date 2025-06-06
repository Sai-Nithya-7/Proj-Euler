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
    cout << largest;
}

int main() {
    check_pal();
    return 0;
}