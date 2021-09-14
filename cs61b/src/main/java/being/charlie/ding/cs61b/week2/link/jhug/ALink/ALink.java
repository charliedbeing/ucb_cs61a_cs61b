package being.charlie.ding.cs61b.week2.link.jhug.ALink;

import java.util.ArrayList;
import java.util.Arrays;


public class ALink {

    public final static ArrayList list= new ArrayList<String>();


    public IntNode[] container = {};
    public int currentCapacity;
    public int currentIndex ;

    public ALink(){
        this.container = new IntNode[100];
        currentCapacity =100;
        currentIndex =0;
    }

    public ALink(int capacity){
      this.container = new IntNode[capacity];
      currentCapacity =capacity;
      currentIndex =0;
    }

    public ALink append(int x){
        checkCapacity();
        this.container[currentIndex] = new IntNode(x);
        currentIndex = currentIndex+1;
        return this;
    }

    public int size(){
        return currentIndex;
    }

    public IntNode get(int key){
        return this.container[key-1];
    }

    public ALink update(int index, int y){
        this.container[index-1] = new IntNode(y);
        return this;
    }

    private void checkCapacity(){
        if(currentIndex+1 == currentCapacity){
            container = changeNewCapacity();
        }
    }

    private IntNode[] changeNewCapacity(){
        IntNode[] arrBigger = new IntNode[this.currentCapacity *2];

        for(int i=0;i<currentIndex;i++){
            arrBigger[i]= container[i];
        }
        return arrBigger;
    }

    private String allItems(){
        String rs ="";
        for(int i=0;i<currentIndex;i++){
            rs = rs + " - " + container[i].item;
        }
        return rs;
    }

    @Override
    public String toString() {
        return "ALink{" +
                "container=" + Arrays.toString(container) +
                ", currentCapacity=" + currentCapacity +
                ", currentIndex=" + currentIndex +
                '}' + "allItems:" + allItems();
    }
}
