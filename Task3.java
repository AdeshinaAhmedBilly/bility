public class Task3 {
    public static void main(String[] args) {
        System.out.println("Task 3: Print odd numbers between 1-10");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}