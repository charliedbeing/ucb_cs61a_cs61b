package being.charlie.ding.cs61b.week2.link.jhug.ALink;

public class ALinkTest {

    public static void main(String[] args) {

        ALink  aLink = new ALink(5);

        aLink.append(1).append(2).append(3).append(4).append(5).append(6);


        System.out.println(aLink.size());
        System.out.println(aLink.get(5).item);

        aLink.update(5,100);
        System.out.println(aLink.get(5).item);

        System.out.println(aLink);

    }
}
