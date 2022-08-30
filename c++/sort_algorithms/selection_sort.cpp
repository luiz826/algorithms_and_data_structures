#include <iostream>

using namespace std;

void selectionSort(int l[], int n)
{
    int i_min, j;

    for (int i = 0; i < n; i++)
    {
        i_min = i;

        for (int j = i+1; j < n; j++)
        {
            if (l[j] < l[i_min])
            {
                i_min = j;
            }
        }
        if (l[i_min] != l[i])
        {   
            int aux = l[i];
            l[i] = l[i_min];
            l[i_min] = aux;
        }
    }
}


int main(void)
{
    const int n = 10;
    int l[n] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    selectionSort(l, n);
    
    for (int i=0; i<n; i++)
    {
        cout << l[i] << endl;
    }

    return 0;
}