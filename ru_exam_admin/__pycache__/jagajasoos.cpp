#include <stdio.h>
#include <stdlib.h>
int n;
void mergeSort(int arr[], int lb, int ub);
void merge(int arr[], int lb, int mid, int ub);
int main() {
    int i;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    mergeSort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; ++i)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}

void mergeSort(int arr[], int lb, int ub) {
    if (lb < ub) {
        int mid = (lb + ub) / 2;

        mergeSort(arr, lb, mid);
        mergeSort(arr, mid + 1, ub);

        merge(arr, lb, mid, ub);
    }
}

void merge(int arr[], int lb, int mid, int ub) {
    int temp[n], i, j, k;
    i=lb;
    j=mid+1;
    k=lb;
    while(i<=mid && j<=ub){
        if(arr[i]<arr[j]){
            temp[k]=arr[i];
            i++;
        }else{
            temp[k]=arr[j];
            j++;
        }
        k++;
    }
    if(i>mid){
        while(j<=ub){
            temp[k]=arr[j];
            j++;
            k++;
        }
    }else{
        while(i<=mid){
            temp[k]=arr[i];
            i++;
            k++;
        }
    }
    for(i=lb; i<=ub; i++){
        arr[i]=temp[i];
    }
}
