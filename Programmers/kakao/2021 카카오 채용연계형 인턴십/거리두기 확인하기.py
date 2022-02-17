
def check(cordi, visited, matrix):
    # 상하좌우 거리 1
    for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
        nex_x = x + cordi[0]
        nex_y = y + cordi[1]
        if 0 <= nex_x < 5 and 0 <= nex_y < 5:
            if matrix[nex_x][nex_y] == 'P':
                return False

    # 상하좌우 거리 2
    for x,y in [(2,0), (0,2), (-2,0), (0,-2)]:
        nex_x = x + cordi[0]
        nex_y = y + cordi[1]
        if 0 <= nex_x < 5 and 0 <= nex_y < 5:
            if matrix[nex_x][nex_y] == 'P':
                if not visited[nex_x][nex_y]:
                    if cordi[0] == nex_x:
                        to_check_y = min(nex_y, cordi[1])+1
                        if matrix[nex_x][to_check_y] == 'O':
                            return False
                    else:
                        to_check_x = min(nex_x, cordi[0])+1
                        if matrix[to_check_x][nex_y] == 'O':
                            return False
    
    # 대각선
    for x,y in [(1,1), (-1,1), (-1,-1), (1,-1)]:
        nex_x = x + cordi[0]
        nex_y = y + cordi[1]
        if 0 <= nex_x < 5 and 0 <= nex_y < 5:
            if matrix[nex_x][nex_y] == 'P':
                if not visited[nex_x][nex_y]:
                    if matrix[nex_x][cordi[1]] == 'O' or matrix[cordi[0]][nex_y] == 'O':
                        return False
    
    return True


def place(p):
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                visited[i][j] = True
                if check((i,j), visited, p) == False:
                    return 0            
    return 1


def solution(places):
    answer = []
    for p in places:
        answer.append(place(p))
    return answer