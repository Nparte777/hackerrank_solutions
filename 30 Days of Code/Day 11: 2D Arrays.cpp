#include <bits/stdc++.h>

using namespace std;

int main()
{   int n=6;
    int a[n][n];
    for (int i = 0;i<n ;i++)
    {
        for(int j =0 ; j<n;j++)
            {cin>>a[i][j];}
    }
    int max=-1111,sum=0;    //Check Reasom for max= -1111 to pass test cases
    for (int i=0;i<n-2;i++)
    {
        for(int j =0;j<n-2;j++)
        {
        sum = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2];
        if(sum>max)
        {
            max=sum;
        }
        }
    }
    //cout<<sum<<endl;    //This will output 14 for testcase 1
    cout<<max;
    return 0;
}
