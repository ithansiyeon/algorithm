from collections import deque

def is_convertable(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt+=1
        if cnt > 1:
            return False
    return cnt == 1

def solution(begin, target, words):
    # target 단어가 words에 없으면 0 반환
    if target not in words:
        return 0

    queue = deque()
    visited = set()

    queue.append((begin,0))

    while queue:
        cur_word, cnt = queue.popleft()
        if is_convertable(cur_word,target):
            return cnt+1

        for word in words:
            if word not in visited and is_convertable(cur_word,word):
                queue.append((word,cnt+1))
                visited.add(word)
    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))

