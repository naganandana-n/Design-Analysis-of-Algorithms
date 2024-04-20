public class BinarySearchRecursive {
    public static void main(String[] args) {

     int[] array = {0, 1, 2, 3, 4, 5};
     System.out.println(binarySearchRecursive(array, 4, 0, array.length - 1));

    }

    public static int binarySearchRecursive(int[] array, int numberToFind,int low, int high){
        if (low > high)
            return -1;
        int middle = (low + high) / 2;
        int middleNumber = array[middle];
        
        if (middleNumber == numberToFind)
            return middle;
        if (middleNumber > numberToFind)
            return binarySearchRecursive(array, numberToFind, low, middle - 1);
        else    
            return binarySearchRecursive(array, numberToFind, middle + 1, high);
        
    }
}
