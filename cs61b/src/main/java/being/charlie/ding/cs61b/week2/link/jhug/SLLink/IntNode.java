package being.charlie.ding.cs61b.week2.link.jhug.SLLink;

public class IntNode {
    public int item;
    public IntNode next;
    public IntNode pre;

    public IntNode(int i, IntNode n, IntNode p){
        this.item =i;
        this.next =n;
        this.pre =p;
    }
}
