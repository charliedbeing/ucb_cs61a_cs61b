package being.charlie.ding.cs61b.week2.link.improve;

public class SLListTest {

    public static void main(String[] args) throws IllegalAccessException {
        SLList slList = new SLList(1);
        slList = slList.addFirst(2).addFirst(3).addFirst(4);



        // System.out.println(slList.getFirst().item);

      //  slList = slList.addLast(5).addLast(6).addFirst(7).addLast(8);

        slList =  slList.addLast(5).addFirst(6).addLast(7);

        System.out.println(slList);
        System.out.println(slList.first.item);

        System.out.println(slList.size() ==7 );
        System.out.println(slList.size());

        //6432157
        System.out.println(slList.get(0).item);

        System.out.println(slList.get(2).item);

        System.out.println(slList.get(6).item);
    }
}
