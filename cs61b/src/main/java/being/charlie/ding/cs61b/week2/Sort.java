package being.charlie.ding.cs61b.week2;

public class Sort {

    public final static int minInt =Integer.MIN_VALUE;
    public final static int maxInt =Integer.MAX_VALUE;

    public static void main(String[] args) {
//        System.out.println(-1>Integer.MIN_VALUE);
        testIntSort();
    }

    public static void testIntSort(){
        int[] arr1 = {9999,7,5,1,3,4,2,6,10,100,1000};
        int[] arr2 = {1,2,3,4,5,6,7,10,100,1000,9999};

//        arr1 = sort(arr1);
        arr1 = sort_2(arr1);
        if(SortTest.compareTwoArrayForInt(arr1,arr2)){
            System.out.println("int sort success!");
        }
    }


    public static int[] sort(int[]arr){
        int[] newarr= new int[arr.length];
        int[] workArr = cloneIntArray(arr);

        int indexValue = 0;

        for(int i=0;i<arr.length;i++){
            indexValue = findTheMinValueAndReplaceToMAX_VALUE(workArr);
            newarr[i]= indexValue;

        }
        return newarr;
    }
    // {7,5,1,3,4,2,6};
    /** Method 2: swap
     * {7,5,1,3,4,2,6};
     * 1: use arr.length times to finish the process of sorting
     * 2: each time, beginItem(0 - arr.length-1), and currentItem(try to find the minValue in a range),
     * 3: after iterator, decide to swap or not
     * */

    public static int[] sort_2(int[]arr){

        int[] workArr = cloneIntArray(arr);

        int beginItem =0;
        int curItem =0;
        for(int k=0; k < workArr.length; k++){

                beginItem = workArr[k];
                int curr=k;

                for(int m=k+1;m<workArr.length;m++){
                    if(workArr[m]<beginItem){
                        beginItem = workArr[m];
                        curr =m;
                    }
                }
                if(curr > k){
                  // swap happened
                  // the minValue = beginItem, minValueIndex =curr, beginIndex =k
                  int temp = workArr[k];
                  workArr[k] =beginItem;
                  workArr[curr]= temp;
                }

        }

        return workArr;
    }

    // {7,5,1,3,4,2,6};
    /** Method 1: use Integer.MAX_VALUE  */
    public static int findTheMinValueAndReplaceToMAX_VALUE(int[]arr){
        int min= arr[0];
        int curr=0;
        for(int i=1;i<arr.length;i++){
            if(arr[i] < min){
                min = arr[i];
                curr =i;
            }
        }
        arr[curr]=maxInt;
        return min;
    }

    // {7,5,1,3,4,2,6};
    /** Method 2: swap
     * 1:
     * 2:
     * 3:
     * */
    public static int findTheMinValueAndSWAP(int[]arr){
        int min= arr[0];
        int curr=0;
        for(int i=1;i<arr.length;i++){
            if(arr[i] < min){
                min = arr[i];
                curr =i;
            }
        }
        int temp =
        arr[curr]=maxInt;
        return min;
    }





    private static int[] cloneIntArray(int[]arr){

        int[] rs = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            rs[i]= arr[i];
        }
        return rs;
    }

}
