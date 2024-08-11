#include<cmath>
#include <iostream>
#include <iomanip>

using namespace std;

int factorial(int n)
{
    unsigned long long factorial = 1;
    for (int i = 1; i <= n; ++i)
    {
        factorial *= i;
    }
    return factorial;
}
int main()
{
    int n;
    cin>>n;
    double sum;
    for (int i = 2; i <= n; i++)
    {
        sum=sum + pow(-1,i)/factorial(i);
    }
    int fac=factorial(n);
    double result=fac * sum;
    double prob=result/fac;
    cout<<prob<<endl;
}