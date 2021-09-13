package being.charlie.ding.cs61b.week2.link;

public class LinkTest {

    public static void main(String[] args) {
        Link l1 = new Link(1);
        Link l2 = new Link(2);
        Link l3 = new Link(3);

        l1.next =l2;
        l2.next =l3;

        System.out.println(l1.size());

        // another constructors demos

        Link ll = new Link(1,new Link(2,new Link(3,null)));

        System.out.println(l1.size() == ll.size());

        try {
            //System.out.println(ll.get(1));

            ll.get(10);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
