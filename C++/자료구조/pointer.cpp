#include <iostream>

using namespace std;

int main(void)
{
    // 1번
    // int arr[] = {1, 2, 3, 4, 5};
    // int *ptr = &arr[0];

    // for (int i = 0; i < 5; i++)
    // {
    //     *(ptr + i) += 2;
    // }
    // for (int i = 0; i < 5; i++)
    // {
    //     cout << *(ptr + i) << endl;
    // }

    // 2번
    // int arr[] = {1, 2, 3, 4, 5};
    // int *ptr = &arr[4];
    // int sum = 0;
    // for (int i = 0; i < 5; i++)
    // {
    //     sum += *ptr;
    //     ptr--;
    // }
    // cout << sum << endl;

    int arr[] = {1, 2, 3, 4, 5, 6};
    int *ptr_start = &arr[0];
    int *ptr_end = &arr[5];

    for (int i = 0; i < 3; i++)
    {
        int temp;
        temp = *ptr_start;
        *ptr_start = *ptr_end;
        *ptr_end = temp;

        ptr_start++;
        ptr_end--;
    }
    for (int i = 0; i < 6; i++)
        cout << arr[i] << endl;
    return 0;
}