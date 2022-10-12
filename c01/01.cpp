#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;
int main()
{
    cout << "Hello World!";
    return 0;
}

int majority1(const vector<int> &A)
{
    int N = A.size();
    int majority = -1, majorityCount = 0;
    for (int i = 0; i < N; i++)
    {
        int V = A[i], count = 0;
        for (int j = 0; j < N; ++j)
        {
            if (A[j] == V)
            {
                ++count;
            }
        }
        if (count > majorityCount)
        {
            majorityCount = count;
            majority = V;
        }
    }
    return majority;
}