package being.charlie.ding.cs61b.week2.link;

public class Link {
    public int value;
    public Link next;

    public Link(int v){
        this.value =v;
        this.next =null;
    }

    public Link(int v, Link n){
        this.value =v;
        this.next =n;
    }

    public int size(){
        //return size_help_r(this,0);

        return interval_size();
    }


    private int size_help_r(Link l,int size){
        if(l.next == null){
            return size+1;
        }else{
            size+=1;
            l= l.next;
            return size_help_r(l,size);
        }
    }

    /** In Java this can not be assigned , */
    private int interval_size(){
        int size =0;
        Link cur = this;
        while(cur.next != null){
            size+=1;
            cur = cur.next;
        }
        return size+1;
    }

    public Link get(int key) throws Exception {
        int counter =0;
        Link p = this;
        Link rs = null;

        if(key<0){
            throw new Exception("key must positive integer");
        }
        while(p.next != null){
            if(counter == key){
                rs= p;
                break;
            }else{
                counter +=1;
                p = p.next;
            }
        }
        if(key>=counter){
            throw new Exception("key beyond the range of this list");
        }
        return rs;
    }

    public String  getAllItems(){
        if(this.next ==null){
            return "" + this.value;
        }else{
            return "" + this.value +"->" + this.next.getAllItems();
        }
    }

    @Override
    public String toString() {
        return "Link{" +
                "value=" + value +
                ", next=" + next +
                '}' + "allItems:" + getAllItems();
    }
}
