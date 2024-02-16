import java.util.Arrays;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {

        Solution solution = new Solution();
        int[] nums1 = {1, 3, 5, 0, 0, 0};
        int m = 3;
        int[] nums2 = {2, 4, 6};
        int n = 3;
        solution.merge(nums1,m,nums2,n);
    }
}

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        Stack<Integer> stack =  new Stack<>();
        int k = 0;

        for (int i = 0; i < m; i++) {
            stack.push(nums1[i]);
        }
        for (int j = 0; j < n; j++) {
            stack.push(nums2[j]);
        }
        while (!stack.isEmpty()) {
            nums1[((m + n) - 1) - k] = stack.pop();
            k++;
        }

        Arrays.sort(nums1);

        System.out.print(Arrays.toString(nums1));
    }
}