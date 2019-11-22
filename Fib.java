import java.util.*;

public class Fib {
	private static int count = 0;

	// 2971215073, 1647462849 recursive calls
	private static long fib(int n) {
		++count;
		if (n <= 1) return 1;
		return fib(n-1) + fib(n-2);
	}

	// 2971215073, 91 recursive calls
	private static long[] fibcache = new long[100];
	private static long fibm(int n) {
	    ++count;
	    if (fibcache[n] == 0) {
            fibcache[n] = (n <= 1) ? 1 : (fibm(n - 1) + fibm(n - 2));
        }
		return fibcache[n];
	}

	public static void main(String[] args) {
		count = 0;
		System.out.println(fibm(46));
		System.out.println(count);
	}
}
