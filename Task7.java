public class Task7 {
    public static void main(String[] args) {
        int[] multiples = {4, 8, 16, 32, 64, 8, 16, 32, 64, 128}; // Assuming these are the results from Task 6
        System.out.println("Task 7: Sum the pairs from Task 6 together");
        int sum = 0;
        for (int i = 0; i < multiples.length; i += 2) {
            sum += multiples[i] + multiples[i + 1];
        }
        System.out.println("Sum of pairs: " + sum);
    }
}