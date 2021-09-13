package being.charlie.ding.cs61b.week2.link.improve;

public class SLList {

    public IntNode first;

    public SLList(int x){
        first = new IntNode(x,null);
    }

    public SLList addFirst(int x){
        IntNode node = new IntNode(x,null);
        IntNode temp = first;
        first = node;
        node.next =temp;
        return this;
    }

    public IntNode getFirst(){
        return first;
    }


    public SLList addLast(int x){
        IntNode node = new IntNode(x,null);
        IntNode preLast = findTheLastNode();
        preLast.next =node;

        return this;

    }

    private IntNode findTheLastNode(){
        IntNode last =null;
        IntNode p = first;
        while(p.next != null){
            last = p;
            p = p.next;
        }
        return last.next;
    }

    public  String getAllItems (){
        String rs ="";
        IntNode p = first;
        while(p.next != null){
            rs  =rs +p.item;
            p = p.next;
        }
        return rs+p.item;
    }

    public int size(){
        return size_help(first);
    }

    public IntNode get(int key) throws IllegalAccessException {
        if(key > size()-1 || key <0 ){
            throw new IllegalAccessException("out of the range");
        }else {
            int counter =0;
            IntNode p = first;
            IntNode rs =null;
            while(p.next!=null){
                if (counter == key){
                    rs = p;
                    break;
                }else{
                    counter +=1;
                    p = p.next;
                    if(counter ==key){
                        rs =p;
                        break;
                    }
                }
            }
            return rs;
        }
    }

    private int size_help(IntNode s){
        if(s.next == null){
            return 1;
        }else{
            return 1 + size_help(s.next);
        }
    }

    @Override
    public String toString() {
        return "SLList{" +
                "first=" + first +
                '}'+"allItems:" + getAllItems();
    }
}
