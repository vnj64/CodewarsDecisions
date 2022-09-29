import java.util.Arrays;

public class Anag {
    public static void main(String[] args) {
        String string = "липа"; 
        String string_2 = "пила";
        
        System.out.println(checkFlag(string, string_2));
    }
    public static boolean checkFlag(String text1, String text2) {
        boolean flag = false;

        char[] array1 = text1.toCharArray();
        char[] array2 = text2.toCharArray();

        Arrays.sort(array1);
        Arrays.sort(array2);

        for (int i = 0; i < array1.length; i++) {
            if (array1[i] == array2[i]) {
                flag = true;
            } else {
                flag = false;
            }
        }

        return flag;
    } 
}