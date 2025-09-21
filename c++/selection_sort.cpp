#include <iostream>
using namespace std;
void selectionsort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int smallestidx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[smallestidx]) {
                smallestidx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[smallestidx];
        arr[smallestidx] = temp;
    }
}
void printarray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main() {
    int arr[] = {5, 4, 3, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionsort(arr, n);
    printarray(arr, n);
    return 0;
}
