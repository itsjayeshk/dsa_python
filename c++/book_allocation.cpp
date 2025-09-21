#include <iostream>
#include <vector>
using namespace std;
bool isPossible(vector<int> &arr, int n, int m, int mid) {
    int studentCount = 1; 
    int pageSum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > mid) {
            return false; 
        }
        if (pageSum + arr[i] <= mid) {
            pageSum += arr[i];
        } else {
            studentCount++;
            if (studentCount > m) {
                return false; 
            }
            pageSum = arr[i];
        }
    }
    return true;
}
int allocateBooks(vector<int> &arr, int n, int m) {
    if (m > n) return -1; 
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    int s = 0, e = sum, ans = -1;
    while (s <= e) {
        int mid = s + (e - s) / 2;
        if (isPossible(arr, n, m, mid)) {
            ans = mid;   
            e = mid - 1; 
        } else {
            s = mid + 1; 
        }
    }
    return ans;
}
int main() {
    vector<int> books = {12, 34, 67, 90};
    int n = books.size();
    int m = 2;  
    cout << "Minimum pages: " << allocateBooks(books, n, m) << endl;
    return 0;
}
