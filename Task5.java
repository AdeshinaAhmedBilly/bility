public class Task5 {
    public static void main(String[] args) {
        int[] multiples = {4, 8};

        System.out.println("Task 5: Print each result from Task 4, 5 times each");
        for (int multiple : multiples) {
            for (int j = 0; j < 5; j++) {
                System.out.print(multiple);
            }
            System.out.print(" ");
        }
        System.out.println();
    }
}