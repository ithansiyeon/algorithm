package algorithm.Programmers.LEVEL3;

class Solution {
    public int solution(int sticker[]) {
        int l = sticker.length;

        if(l==1) {
            return sticker[0];
        }

        Integer[] dp1 = new Integer[l];
        dp1[0] = sticker[0];
        dp1[1] = dp1[0];

        for(int i = 2; i<l ;i++) {
            dp1[i] = Math.max(dp1[i-2]+sticker[i], dp1[i-1]);
        }

        Integer[] dp2 = new Integer[l];
        dp2[0] = 0;
        dp2[1] = sticker[1];

        for(int i=2; i<l; i++) {
            dp2[i] = Math.max(dp2[i-2]+sticker[i], dp2[i-1]);
        }

        return Math.max(dp2[l-1], dp1[l-2]);
    }
}