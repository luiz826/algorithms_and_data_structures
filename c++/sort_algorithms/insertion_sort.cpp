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
