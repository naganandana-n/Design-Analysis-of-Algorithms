public class SelectionSort {
    public static void main(String[] args) {
        
        int array[] = {5, 4, 3, 2, 1};
        selectionSort(array);

        for(int i : array)
            System.out.print(i + " ");
    }

    public static void selectionSort(int[] array){

        for(int i = 0; i < array.length - 1; i++){
            int min = i;
            for(int j = i + 1; j < array.length; j++){
                if (array[min] > array[j]) // swapping less than greater than here will change 
                    min = j;                // sorting order from ascending to descending and viceversa
            }

            // swapping
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }
}
