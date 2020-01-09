public class SelectionSort{
    public static void main(String[] args){
        int array [] = {4, 7, 3, 0, 6, 10, 29, 16, 11, 1};
        int min = 0;

        for(int i = 0; i < array.length-1; i++){
            min = i;
            for(int j = i+1; j < array.length; j++){
                if(array[j] <= array[min]){
                    min = j;
                }
            }
            swap(i, min, array);
        }

        for(int i = 0; i < array.length; i++){
            System.out.printf("%d ", array[i]);
        }
    }

    static void swap(int x, int y, int[] a){
        int t = a[x];
        a[x] = a[y];
        a[y] = t;
    }
}
