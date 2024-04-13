예제는 맞았지만 테스트 케이스는 하나도 맞지 못한 충격적인 결과~

def solution(genres, plays):
    answer = []
    playlist = {}
    genre = set(genres)
    
    for i,j in zip(genres, plays):
        if i not in playlist:
            playlist[i] = j
        else:
            playlist[i] += j
    
    a = sorted(playlist.items(), key = lambda x: x[1], reverse = True)
    top_genre = [a[0][0], a[1][0]]
    
    for i in top_genre:
        score_list = []
        for j in range(len(genres)):
            if i == genres[j]:
                score_list.append(plays[j])
        answer.append(plays.index(max(score_list)))
        score_list.pop(score_list.index(max(score_list)))
        answer.append(plays.index(max(score_list)))
    
    return answer
