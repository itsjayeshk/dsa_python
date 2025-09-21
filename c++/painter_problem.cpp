#include <bits/stdc++.h>
using namespace std;
bool canPaintWithMax(const vector<long long>& boards, long long painters, long long maxAllowed) {
    long long usedPainters = 1;
    long long currSum = 0;
    for (long long len : boards) {
        if (len > maxAllowed) return false; 
        if (currSum + len <= maxAllowed) {
            currSum += len;
        } else {
            usedPainters++;
            currSum = len;
            if (usedPainters > painters) return false;
        }
    }
    return true;
}
long long minTimePartition(const vector<long long>& boards, long long painters) {
    long long lo = *max_element(boards.begin(), boards.end()); 
    long long hi = accumulate(boards.begin(), boards.end(), 0LL); 
    long long ans = hi;
    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (canPaintWithMax(boards, painters, mid)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> boards(n);
    for (int i = 0; i < n; ++i) cin >> boards[i];

    long long result = minTimePartition(boards, k);
    cout << result << "\n";
    return 0;
}
