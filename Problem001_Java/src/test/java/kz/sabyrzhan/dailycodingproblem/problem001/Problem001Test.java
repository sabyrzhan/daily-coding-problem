package kz.sabyrzhan.dailycodingproblem.problem001;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Problem001Test {
    Problem001 t = new Problem001();

    @Test
    void test_success() {
        int[] a = new int[]{ 10, 15, 3, 7 };
        int k = 17;
        var result = t.containsNumbers(a, k);
        assertTrue(result);
    }

    @Test
    void test_does_not_contain() {
        int[] a = new int[]{ 10, 15, 3, 7 };
        int k = -1;
        var result = t.containsNumbers(a, k);
        assertFalse(result);
    }

    @Test
    void test_success2() {
        int[] a = new int[]{ 1, 1, 1, 1 };
        int k = 2;
        var result = t.containsNumbers(a, k);
        assertTrue(result);
    }

    @Test
    void test_success3() {
        int[] a = new int[]{ 0,0,0,0 };
        int k = 0;
        var result = t.containsNumbers(a, k);
        assertTrue(result);
    }

    @Test
    void test_success4() {
        int[] a = new int[]{ 1,0,1,0 };
        int k = 1;
        var result = t.containsNumbers(a, k);
        assertTrue(result);
    }

    @Test
    void test_success5() {
        int[] a = new int[]{ 1,0,1,0 };
        int k = 2;
        var result = t.containsNumbers(a, k);
        assertTrue(result);
    }

    @Test
    void test_empty_list() {
        int[] a = new int[]{  };
        int k = 1;
        var result = t.containsNumbers(a, k);
        assertFalse(result);
    }
}