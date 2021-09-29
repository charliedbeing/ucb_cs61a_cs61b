package being.charlie.ding.cs61a.scheme;

public class TestSchemeOne {
    public static void main(String[] args) {
        IntreSchemeOne intreSchemeOne = new IntreSchemeOne();

        String formula="(+(+(+ 2 3)(- 3 2))(+ 2 3))";
        formula="(+ (+ (+ 11 1) 2) (+ (+ 3 4) (+ 2 3))))";

        String [] s= StringUtil.toRegularFormular(formula.toCharArray());
       int rs = intreSchemeOne.parseFormulaHelp(s);

        System.out.println(rs);
        System.out.println(rs == 26 );
    }
}
