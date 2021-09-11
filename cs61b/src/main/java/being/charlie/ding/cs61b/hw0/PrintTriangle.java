package being.charlie.ding.cs61b.hw0;

public class PrintTriangle {

    public static void main(String[] args) throws Exception {
        printTriangle(5);
        int [] a1= {1,2,-3,4,5,4};
        int [] a2 ={1,-1,-1,10,5,-1};
        int [] res= windowPosSum(a2,2);
        printArray(res);
    }

    private static void printArray(int[] a){
        for(int i=0;i<a.length;i++){
            System.out.println(a[i]);
        }
    }


    public static void printTriangle(int num){
        String item="";
        for(int i=0;i<num;i++){
            item=item+"*";
            System.out.println(item);
        }
    }

    public static int maxNumber(int[] arr){
        int res =0;
        for(int i=0; i<arr.length; i++){
            if(arr[i]>res){
                res =arr[i];
            }
        }
        return res;
    }

    /**
     *
     Write a function windowPosSum(int[] a, int n)
     that replaces each element a[i] with the sum of a[i] through a[i + n],
     but only if a[i] is positive valued.
     If there are not enough values because we reach the end of the array,
     we sum only as many values as we have.
     For example, suppose we call windowPosSum with the array
     a = {1, 2, -3, 4, 5, 4}, and n = 3. In this case, we’d:

     Replace a[0] with a[0] + a[1] + a[2] + a[3].
     Replace a[1] with a[1] + a[2] + a[3] + a[4].
     Not do anything to a[2] because it’s negative.
     Replace a[3] with a[3] + a[4] + a[5].
     Replace a[4] with a[4] + a[5].
     Not do anything with a[5] because there are no values after a[5].
     */

    public static int[] windowPosSum(int []arr,int n) throws Exception {


        int indexSum=0;

        for(int i=0;i<arr.length;i++){
            indexSum = sumByindexAndArray(arr,i,n);
            arr[i]=indexSum;
        }

        return arr;
    }

    private static int  sumByindexAndArray(int[] arr,int index,int n) throws Exception {
        int res =0;
       if(index > arr.length-1){
           throw new Exception("Error index,please check the index");
       }else if(index == arr.length-1 || arr[index]<0)

       {
            res= arr[index];
        }else{

           for(int i=index;i<=index+n;i++){
               if(i > arr.length-1){
                   break;
               }else if(i<=arr.length-1){

                       res =res +arr[i];
                   }
               }
           }
            return res;
        }

    }

