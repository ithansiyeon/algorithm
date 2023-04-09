package algorithm.Programmers.LEVEL3;

import java.util.Arrays;

class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int left = 1;
        int right = Arrays.stream(stones).max().getAsInt();
        while(left <= right) {
            int mid = (left+right) / 2;
            int cnt = 0;
            boolean check = true;
            for(int stone:stones) {
                if(stone < mid) {
                    cnt++;
                    if(cnt>=k) {
                        check = false;
                        break;
                    }
                } else {
                    cnt = 0;
                }
            }
            if(check) {
                answer = mid;
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        return answer;
    }
}