/** https://projecteuler.net/problem=5
 * solution in Java
 * 
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 * 
 * if java is installed, then run by:
 * java .\p5_euler.java
 * 
 * Answer:  232792560
 */
class Main {
    public static void main(String args[]) {
        System.out.println("Euler problem #005 solution");
        int num = 1;
        int n = 20;
        while (true){
            int sum = 0;
            for (int i = 1; i <= n; i++) {
                if(num % i != 0){
                    break;
                }
                else{
                    sum++;
                }
        }
        if (sum == n){
                System.out.println("result: " + num);
                break;
            }
        num++;
        }
    }
}