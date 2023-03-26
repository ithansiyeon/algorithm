package algorithm.Programmers.LEVEL3;
import java.util.*;

class Solution {

    public static int solution(int n, int[] stations, int w) {
        int answer = 0;
        int start = 1;
        int idx = 0;
        while(start<=n){
            if(idx<stations.length && start >= stations[idx]-w) {
                start = stations[idx] + w + 1;
                idx+=1;
            } else {
                start += 2*w+1;
                answer+=1;
            }
        }

        return answer;
    }
}
