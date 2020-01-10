import java.util.ArrayList;
import java.util.Scanner;
import java.util.Set;
import java.util.HashMap;

public class ProgrammingExercises {
    public static void printDups(String str){
        HashMap<Character, Integer> dups = new HashMap();
        // poulate the hash map - O(n)
        for(int i = 0; i < str.length(); i++){           
            char curKey = str.charAt(i); 
            if(dups.containsKey(curKey)){
                int curVal = dups.get(curKey);
                //if(dups.containsKey(curKey)){
                    curVal++;
                    dups.put(curKey, curVal);
                //}
            }else{
                dups.put(curKey, 1);
            }
        }
        for(char c: dups.keySet()){
             if(dups.get(c) > 1){
                System.out.print(c);
            }
        }
        // Time Complexity: size of string(n) + number of keys in hash map(m)
        // bounded by whichever of m, n is greatest
    }

    public static boolean anagram(String a, String b){
        // must be same length
        if(a.length() != b.length()) return false;
        
        ArrayList<Character> firstString = new ArrayList();
        // populate the char array with each 
        for(int i = 0; i < a.length(); i++){
            firstString.add(a.charAt(i));
        }
        for(int i = 0; i < b.length(); i++){
            for(int j = 0; j < firstString.size(); j++){
                if(!firstString.isEmpty()){
                    if(firstString.indexOf(b.charAt(i)) != -1){
                        firstString.remove(firstString.indexOf(b.charAt(i)));
                        break;
                    }
                }
            }
        }
        //done comapring every character
        if(!firstString.isEmpty()){
            return false;
        }
        return true;

    }
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String input;
        String input2;
        System.out.println("First String: printDups and anagram string a\nSecond String: anagram string b ");
        input = scan.nextLine();
        input2 = scan.nextLine();
        printDups(input);
        System.out.println(input + " and " + input2 + " are anagrams: " + anagram(input, input2));
    }
}
