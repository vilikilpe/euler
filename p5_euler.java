/**
 * https://projecteuler.net/problem=5
 * solution in Java
 * 
 * 2520 is the smallest number that can be divided by each of the numbers from 1
 * to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the
 * numbers from 1 to 20?
 * 
 * if java is installed, then run by:
 * java .\p5_euler.java
 * 
 * Answer: 232792560
 */

class Main {
    public static void main(String args[]) {

        long start1 = System.currentTimeMillis();

        System.out.println("Euler problem #005 solution");
        int num = 20;
        int n = 20;
        // Loop as long as solution is found
        while (true) {
            int sum = 0;
            // Start from 20
            for (int i = 1; i <= n; i++) {
                // If there are remainder then break loop
                if (num % i != 0) {
                    break;
                } else {
                    sum++;
                }
            }
            // If all 20 divisions were without remainder -> sum is equal to n
            if (sum == n) {
                System.out.println("result: " + num);
                break;
            }
            num++;
        }
        long end1 = System.currentTimeMillis();
        System.out.println("Elapsed Time in milliseconds: " + (end1 - start1));
    }
}