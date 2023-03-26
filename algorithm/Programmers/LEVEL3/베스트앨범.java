package algorithm.Programmers.LEVEL3;
import java.util.*;

class Solution {

    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answerList = new ArrayList<>();
        Map<String, List<int[]>> dic = new HashMap<>();
        Map<String, Integer> playSum = new HashMap<>();

        for(int i=0;i<plays.length;i++) {
            String genre = genres[i];
            int play = plays[i];
            
            if(!dic.containsKey(genre)) {
                dic.put(genre, new ArrayList<>());
                playSum.put(genre, 0);
            }

            dic.get(genre).add(new int[] {i,play});
            playSum.put(genre, playSum.get(genre)+play);
        }

        List<String> sortedGenre = new ArrayList<>(playSum.keySet());
        Collections.sort(sortedGenre, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return playSum.get(o2).compareTo(playSum.get(o1));
            }
        });

        for(String genre:sortedGenre) {
            List<int[]> songs = dic.get(genre);
            Collections.sort(songs, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    if(o1[1] == o2[1]) {
                        return Integer.compare(o1[0], o2[0]);
                    }
                    return Integer.compare(o2[1],o1[1]);
                }
            });

            if(songs.size() == 1) {
                answerList.add(songs.get(0)[0]);
            } else {
                answerList.add(songs.get(0)[0]);
                answerList.add(songs.get(1)[0]);
            }
        }
        int[] answer = new int[answerList.size()];
        for(int i=0;i<answerList.size();i++) {
            answer[i]=answerList.get(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] answer = solution(new String[] {"classic", "pop", "classic", "classic", "pop"},new int[] {500, 600, 150, 800, 2500});
        System.out.println(Arrays.toString(answer));
    }
}
