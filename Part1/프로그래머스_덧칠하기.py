# n 미터짜리 벽 -> n 개의 구역으로 나눔. (1~n)
# 페인트를 다시 칠해야 할 구역 정함.
# 페인트 롤러의 길이 m 미터

def solution(n, m, section):
    answer = len(section)
    start = section[0]
    
    for i in range(len(section)):
        if m >= section[i+1] - start + 1:
            answer -= 1
        else:
            start = section[i+1]
            
    return answer

# 위 코드는 오답
########정답 풀이##########
def solution(n, m, section):
    answer = 1
    start = section[0]
    for block in section:
        if block - start >= m:  # 두 개의 블럭 색칠
            start = block
            answer += 1         
    return answer