def solution(cards1, cards2, goal):
    for word in goal:
        if word == cards1[0]:
            cards1.pop(0)
        elif word == cards2[0]:
            cards2.pop(0)
        else:
            answer = 'No'; return answer
            
        if not cards1:
            cards1.append('temp')
        if not cards2:
            cards2.append('temp')
            
    answer = 'Yes'
    return answer