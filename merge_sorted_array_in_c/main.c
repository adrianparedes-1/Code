#include <stdio.h>
#include <stdlib.h>

/*

Adrian Paredes
2/17/24

Leetcode problem 88: Merge Sorted Array

I completed this problem with Java yesterday but had a lot of difficulty with the sorting method. I ended up using Arrays.sort(); but was not ideal.
Came back today and practiced this problem using bubble sort even though it is not good for efficiency or timing. Need to learn quick sort and try a different sorting problem.
Overall, I am happy with the progress so far and I'm motivated to keep learning

*/

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {

    int j = 0;
    for (int i = m; i < nums1Size; i++, j++) { //populated nums1 with nums2 -- will not get out of bounds since nums1Size = m + n and nums2Size = n.
        nums1[i] = nums2[j];
    }

    bool swapped = true; //flag to check if array was sorted at all to avoid unnecessary looping
    for (int i = 0; i < (nums1Size - 1); i++) {
         swapped = false; //setting flag to false every iteration
        for (int j = 0; j < (nums1Size - 1 - i); j++) {
            if (nums1[j] > nums1[j + 1]) { //swapping values if needed
                int temp = nums1[j];
                nums1[j] = nums1[j + 1];
                nums1[j + 1] = temp;
                swapped = true; //array was sorted in this iteration
            }
        }
        if (!swapped) { //if flag is false, it means the array was not sorted in past iteration meaning it is already in correct order so we can exit loop
            break;
        }
    }

    for (int i = 0; i < nums1Size; i++) { //just printing each value
        printf("%d ", nums1[i]);
    }

}
