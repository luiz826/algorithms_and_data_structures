#include <iostream>
using namespace std;

void insertion_sort(int l[], int n)
{
    int pivot = l[0]; 
    int j;

    for (int i=0; i < n; i++)
    {
        pivot = l[i];
        j = i - 1;
        while ( (j >= 0) && (l[j] > pivot) )
        {
            l[j+1] = l[j];
            j--;
        }   
        l[j+1] = pivot;
    } 
}

int main(){
    const int n = 9;
    int l[n] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    insertion_sort(l, n);

    for (int i=0; i < n; i++) { cout << l[i] << endl; }

    return 0;
}

