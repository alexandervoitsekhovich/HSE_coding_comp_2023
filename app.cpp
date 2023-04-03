#include <iostream>

using namespace std;

int main() {
    int arr_size;
    cin >> arr_size;
    int* arr = new int[arr_size];

    for (int i = 0; i < arr_size; i++) {
        cin >> arr[i];
    }

    long int counter = 0;

    for (int i = 0; i < arr_size; i++) {
        int number = arr[i];
        if (number % 4 == 0) {
            counter += number / 4;
        } else {
            counter += number / 4;
            if (number % 4 == 2 || number % 4 == 3) {
                counter += 2;
            } else {
                counter += 1;
            }
        }
    }

    cout << counter;
}
