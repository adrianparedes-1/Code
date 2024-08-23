/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*) malloc(2 * sizeof(int)); //allocating memory for an array of 2 integers
    for (int i = 0; i < numsSize; i++) {//outside loop will calculate first index
        int val = target - nums[i];
        for (int j = i + 1; j < numsSize; j++) {//inside loop will loop through every other index (not i) and check if any other index == val
            if (val == nums[j]) {
                result[0] = i;//saving first index
                result[1] = j;//saving second index
                *returnSize = 2; //passing the value 2 to int variable pointed to by returnSize
                return result;//returning both indeces
            }
        }
    }
    free(result); //free memory
    return NULL; //return nothing when looping through every value does not equal to target
}