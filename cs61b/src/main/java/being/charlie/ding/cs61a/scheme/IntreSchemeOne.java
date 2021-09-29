package being.charlie.ding.cs61a.scheme;


public class IntreSchemeOne {

    //(+(+ 2 3)(-(+ 123 390) 9))
    //(+ 2 3)

    /** very simple */
    class LeftItem{
        private boolean isValue;
        private String[] rs;
        //this index will be the base for find rightItem.
        private int left_RightEdge;

        public LeftItem(){}

        public int getValue(){
            return Integer.parseInt(rs[0]);
        }
        public String[] getStringArray(){
            return rs;
        }
        public void setIsValue(boolean b){isValue =b;}
        public void setRs(String[] s){rs=s;}
        public void setLeft_RightEdge(int i){left_RightEdge =i;}
    }

    class RightItem{
        private boolean isValue;
        private String[] rs;
        public RightItem(){}

        public int getValue(){
            return Integer.parseInt(rs[0]);
        }
        public String[] getStringArray(){
            return rs;
        }
        public void setIsValue(boolean b){isValue =b;}
        public void setRs(String[] s){rs=s;}

    }

    public  int parseFormulaHelp(String[] s){

        SStack ss = new SStack();
        String operator = get_operator(s,ss);
        LeftItem leftItem = get_leftItem(s,ss);
        RightItem rightItem = get_rightItem(s,ss);

        return op_formula(operator,leftItem,rightItem);
    }

    /** Three basic steps*/
    private static String get_operator(String[]s, SStack ss ){
        ss.push(s[0]);
        return s[1];
    }

    //(+(+ 2 3)(-(+ 123 390) 9))
    //(+ 2 3)
    //(- 2(+ 2 3))
    //(- 2(+ 2 3))
    /**
     * two types: () or number
     *
     */
    private  LeftItem get_leftItem(String[]s, SStack ss  ){

        LeftItem leftItem = new LeftItem();

        if(s[2].equals(" ")){
            leftItem.setLeft_RightEdge(3);
            String [] t = {s[3]};
            leftItem.setRs(t);
            leftItem.setIsValue(true);

        }else if(s[2].equals("(")){
            leftItem.setIsValue(false);
            // update another two fields values.
            getOneCompleteBracketContentLeft(s,ss,2,leftItem);
        }
        return leftItem;
    }

    //(+(+ 2 3)(-(+ 123 390) 9))
    //(+(+ 2 3) 8)
    //(+ 2 3)
    //(- 2(+ 2 3))

    private  RightItem get_rightItem(String[]s, SStack ss  ){

        LeftItem  leftItem = get_leftItem(s,ss);
        RightItem rightItem = new RightItem();
        // base on the  s[leftItem.left_RightEdge+1] can be blank or (
        String baseString = s[leftItem.left_RightEdge+1];

        if(baseString.equals(" ")){

            String [] t = {s[leftItem.left_RightEdge+2]};
            rightItem.setRs(t);
            rightItem.setIsValue(true);
        }else if(baseString.equals("(")){
            rightItem.setIsValue(false);
            getOneCompleteBracketContentRight(s,ss,leftItem.left_RightEdge+1 ,rightItem);
        }


        return rightItem;
    }


    private  int op_formula(String operator,LeftItem leftItem,RightItem rightItem){
        int rs =0;
        if(leftItem.isValue && rightItem.isValue){
            rs= simple_op(operator,leftItem.getValue(),rightItem.getValue());
        }else if(leftItem.isValue && !rightItem.isValue){
            rs= simple_op(operator,leftItem.getValue(),parseFormulaHelp(rightItem.getStringArray()));
        }else if(!leftItem.isValue && !rightItem.isValue){
            rs= simple_op(operator,parseFormulaHelp(leftItem.getStringArray()),parseFormulaHelp(rightItem.getStringArray()));
        }else if(!leftItem.isValue && rightItem.isValue){
            rs= simple_op(operator,parseFormulaHelp(leftItem.getStringArray()),rightItem.getValue());
        }
        return rs;
    }
    /**  simple method to support calculate the final value*/

    private static int simple_op(String op, int left,int right){
        int rs =0 ;
        if(op.equals("+")){
            rs= left +right;
        }else if(op.equals("-")){
            rs=  left- right;
        }else if(op.equals("*")){
            rs=  left * right;
        }else if(op.equals("/")){
            rs=  left / right;
        }

        return rs;
    }


    /** support methods for three basic steps */

    // //(+(+ 2 3)(-(+ 123 390) 9))

   //(+(+(+ 2 3)(- 3 2))(+ 2 3))
  //012345678910
   //(+  ( + (+ 2 3) (- 3 2) )    (+ 2 3))

    private static void getOneCompleteBracketContentLeft(String[]s,SStack ss ,  int index,LeftItem leftItem){

      //   leftItem.setRs(); =>((+(- 4 2)(+ 2 3))
     //   leftItem.left_RightEdge() =>  (+ 2 3)'s right bracket index
        int rightIndex = index;
        ss.clear();
        ss.push(s[index]);
       // (+(+(+ 2 3)(- 3 2))(+ 2 3))
        // (+(+(+ 2 3)(- 3 2))(+ 2 3))
        for(int i=index+2;i<s.length;i++){
            if(!StringUtil.is_bracket(s[i])){
                continue;
            }else if("(".equals(s[i])){
                ss.push(s[i]);
            }else if(")".equals(s[i])){
                ss.pop();
                if(ss.getCurr()==0){
                    rightIndex =i;
                    break;
                }
            }
        }

        String [] rs = new String[rightIndex-index+1];
        int indexRs =0;
        for(int i=index;i<=rightIndex;i++){
            rs[indexRs]=s[i];
            indexRs = indexRs+1;
        }
        leftItem.setRs(rs);
        leftItem.setLeft_RightEdge(rightIndex);
    }

//   //(+(+ 2 3)(-(+ 123 390) 9))
    private static void getOneCompleteBracketContentRight(String[]s,SStack ss , int index, RightItem rightItem){


        //   leftItem.setRs(); =>((+(- 4 2)(+ 2 3))
        //   leftItem.left_RightEdge() =>  (+ 2 3)'s right bracket index
        int rightIndex = index;
        ss.clear();
        ss.push(s[index]);

        for(int i=index+1;i<s.length;i++){
            if(!StringUtil.is_bracket(s[i])){
                continue;
            }else if("(".equals(s[i])){
                ss.push(s[i]);
            }else if(")".equals(s[i])){
                ss.pop();
                if(ss.getCurr()==0){
                    rightIndex =i;
                    break;
                }
            }
        }
        String [] rs = new String[rightIndex-index+1];
        int indexRs =0;
        for(int i=index;i<=rightIndex;i++){
            rs[indexRs]=s[i];
            indexRs = indexRs+1;
        }
        rightItem.setRs(rs);
    }





}
