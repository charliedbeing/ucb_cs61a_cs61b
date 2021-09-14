package being.charlie.ding.cs61b.week2.link.jhug.SLLink;

public class SSLinkTest {

    public static void main(String[] args) {

        SSLink  l= new SSLink();

       l=  l.addFirst(1).addFirst(2).addFirst(3).addLast(4).addLast(5);

//        l= l.addLast(1);
//        l.addLast(5);


        System.out.println(l);
    }
}
