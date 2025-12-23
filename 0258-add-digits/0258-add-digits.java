class Solution {
    public int addDigits(int num) {
        int sum = 0;
        int result = 0;
        int digit = 0;
        if (num < 10) {
            return num;
        }
        while (num > 0 && num >= 10) {
            while (num != 0) {
                digit = num % 10;
                sum += digit;
                num = num / 10;
            }
            result = sum;
            num = sum;
            sum = 0;
            if (result < 10) {
                return result;
            }       
        }
        return result;
    }
}