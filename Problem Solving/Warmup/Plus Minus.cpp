#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main(void)
{
    int n, a;
    cin >> n;

    int zero = 0, plus = 0, min = 0;
    for(int i = 0; i < n; i++){
        cin >> a;

        if(a == 0)
            zero++;
        else if(a > 0)
            plus++;
        else
            min++;
    }

    cout << setprecision(6) << (plus * 1.0) / n << endl;
    cout << setprecision(6) << (min * 1.0) / n << endl;
    cout << setprecision(6) << (zero * 1.0) / n << endl;

    return 0;
}
