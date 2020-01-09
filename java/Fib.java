import java.util.Scanner;
import java.util.HashMap;

public class Fib{
    static HashMap<Integer, Integer> memo = new HashMap<>();

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int fibval = 0;

        System.out.print("Enter the value for the fib. sequence: ");
        fibval = s.nextInt();
        System.out.println("fibval: " + fibval);
        System.out.printf("Fib value for %d: %d\n", fibval, fib(fibval));
    }

    static int fib(int x){
        if(x < 0) return 0;
        if(x == 0 || x == 1){
            Fib.memo.put(x, x);
            return x;
        }
        if(Fib.memo.containsKey(x)){// && Fib.memo.size() > x){
            return Fib.memo.get(x);
        }
        int ret = fib(x-1) + fib(x-2);
        Fib.memo.put(x, ret);
        return ret;
    }
}
