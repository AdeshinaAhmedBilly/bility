public class Task6 {
    public static void main(String[] args) {
        int[] multiples = {4, 8}; 
        System.out.println("Task 6: Print the 5 multiples of each of the result from Task 4");
        int[] results = new int[multiples.length * 5];
        int index = 0;
        for (int multiple : multiples) {
            for (int j = 1; j <= 5; j++) {
                results[index++] = multiple * j;
                System.out.print(multiple * j + " ");
            }
        }
        System.out.println();
    }
}