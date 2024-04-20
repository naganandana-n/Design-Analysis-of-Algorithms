
public class BinarySearch{
    public static void main(String[] args) {
        int[] array = {0, 1, 2, 3, 4, 5};
        System.out.println(binarySearch(array, 2));
        
    }

    public static int binarySearch(int[] array, int numberToFind){
        int low = 0;
        int high = array.length - 1;

        while (low <= high){
            int middle = (low + high) / 2;
            int middleNumber = array[middle];
            
            if (middleNumber == numberToFind)
                return middle;
            if (middleNumber > numberToFind)
                high = middle - 1;
            else    
                low = middle + 1;
        }

        return -1; // number not found
    }
}
