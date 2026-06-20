class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder nStr = new StringBuilder("");
        for (int i = 0; i < s.length(); i++) {
            if (!(Character.isAlphabetic(s.charAt(i))) && !(Character.isDigit(s.charAt(i)))) {
                nStr.append("");
            } else {
                nStr.append(s.charAt(i));
            }
        }
        int j = nStr.length() - 1;
        for (int i = 0; i < nStr.length(); i++) {
            if (((int) nStr.charAt(i) == (int) nStr.charAt(j))) {
                j--;
            } else {
                return false;
            }
        }
        return true;
    }
}
