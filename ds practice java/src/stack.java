import java.util.Scanner;
import java.util.Stack;

public class stack {
    public static void main(String[] args){
        Stack<Integer> stack = new Stack<Integer>();
        Scanner input = new Scanner(System.in);
        int i,n,value, tem = 0;
        System.out.println("Enter the number of element you want to enter to stack:");
        n = input.nextInt();
        System.out.println("Enter the integer "+n+" times:");
        for (i=0; i< n; i++) {
            value = input.nextInt();
            tem = stack.push(value);
        }

        System.out.println("Stack " + stack);
        for (Integer ele:stack)
            System.out.println(ele);

        stack.pop();

        System.out.println("After pop() one element:" + stack);
        for (Integer ele:stack)
            System.out.println(ele);


    }
}
