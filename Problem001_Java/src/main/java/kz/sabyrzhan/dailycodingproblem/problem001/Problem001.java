package kz.sabyrzhan.dailycodingproblem.problem001;

/*
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
 */
public class Problem001 {
    public boolean containsNumbers(int[] numbers, int k) {
        int i = 0;
        int j = numbers.length - 1;
        while (i < j) {
            int a = numbers[i];
            int b = numbers[j];
            if (a + b == k) {
                return true;
            }

            if (a < b) {
                i++;
            } else {
                j--;
            }
        }

        return false;
    }
}