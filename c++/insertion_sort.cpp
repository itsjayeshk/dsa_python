#include <iostream>
using namespace std;
void insertionsort(int arr[], int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
void printarray(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main() {
    int n =5;
    int arr[] = {5, 4, 3, 2, 1};
    insertionsort(arr, n);
    printarray(arr, n);  
    return 0;

}
