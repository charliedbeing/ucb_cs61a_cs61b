package being.charlie.ding.cs61b.week2.link.jhug.SLLink;

/**
 *
 * */
public class SSLink {

    public IntNode first;
    public IntNode last;
    public int size =0;

    public SSLink(int x){
        firstOne(x);
    }

    private void firstOne(int x){
        first = new IntNode(x,null,null);
        last = first;
        size +=1;
    }

    public SSLink(){
        first = null;
        last = null;
    }

    /**
     *  1: create a new node : Node
     *  2: Node.next=?  Node.pre =? keep
     *  3: first_p.next =? keep  first_p.pre =?
     *  4: first =? last =? keep
     *  5: size =size+1
     * */
    public SSLink addFirst(int x){

        if(first == null){
            firstOne(x);
        }else{
            IntNode node = new IntNode(x,null,null);
            IntNode first_p = first;

            node.next = first_p;
            first_p.pre= node;
            first = node;
            size+=1;

        }


        return this;
    }

    public IntNode getFirst(){

        return first;
    }

    /**
     *  1: create a new node : Node
     *  2: Node.next=? keep  Node.pre =?
     *  3: p_last.next=?  p_last.pre =? keep
     *  4: first =? keep last =?
     *  5: size =size+1
     */
    public SSLink addLast(int x){
        if(last == null){
            firstOne(x);
        }else{
            IntNode node = new IntNode(x,null,null);
            IntNode p_last = last;

            node.pre = p_last;
            p_last.next =node;
            last =node;
            size+=1;
        }

        return this;
    }
    public IntNode getLast(){
        return last;
    }

    public IntNode get(int key){
          return findFromFrontOrRear(first,key);
    }

    private IntNode findFromFrontOrRear(IntNode p,int key){
        int counter =0;
        IntNode rs =null;

        if(key == counter){
            rs =p ;
        }else{
          while(p.next !=null){
              if(key > counter){
                  counter +=1;
                  p = p.next;
              }else{
                  rs= p;
                  break;
              }
          }
        }
        return rs;
    }


    public int size(){
        return size;
    }

    private String allItems(){
        String s ="";
        IntNode p = first;

        while(p.next !=null){
            s = s+ p.item;
            p=p.next;
        }
        return s +p.item;
    }

    @Override
    public String toString() {
        return "SSLink{" +
                "first=" + first +
                ", last=" + last +
                ", size=" + size +
                '}' + "AllItems:" + allItems();
    }
}
