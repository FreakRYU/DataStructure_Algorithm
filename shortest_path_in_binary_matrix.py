from collections import deque

# 이진행렬 grid를 입력받아 미로를 탐색하는 최단거리 반환
def ShortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    # 이중리스트 grid의 요소 개수는 행의 개수이다.
    row = len(grid) 
    # 그리고 요소의 길이는 열의 개수가 된다.
    col = len(grid[0]) 

    # 시작점과 출발점이 막혀있다면 방법이 없으므로 -1을 반환
    # 인덱스는 0부터 시작하므로 row와 col에 1씩 빼준다.
    if grid[0][0] != 0 or grid[row-1][col-1] != 0: 
        return shortest_path_len
    
    # 방문여부를 grid와 크기가 같은 이중리스트로 형성한다.
    visited = [[False] * col for _ in range(row)]

    # 방향이 상하좌우 및 대각선 4방향을 모두 튜플로 포함
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # 시작점을 미리 방문
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True

    # 암시적 그래프를 기반으로 BFS 수행
    while q:
        # q에서 제거하는 동시에, 탐색을 수행할 현재의 row, col을 새로 정의
        cur_row, cur_col, cur_len = q.popleft()
        
        # cur_row와 cur_col이 목적지에 도착하면 cur_len을 반환
        if cur_row == row-1 and cur_col == col-1:
            shortest_path_len = cur_len
            break
        
        # 상하좌우 및 대각선 8가지 방향을 모두 탐색
        for dr, dc in direction:
            next_row = cur_row + dr
            next_col = cur_col + dc
            # 우선 지정한 좌표가 지도에서 벗어나는지 확인
            if 0 <= next_row < row and 0 <= next_col < col:
                # 좌표에 해당하는 영역이 0인지 1인지 판별 및 방문했는지 여부를 판별
                if grid[next_row][next_col] == 0 and not visited[next_row][next_col]:
                    # 다음 좌표를 q에 저장하고, 거리는 +1 해줌
                    q.append((next_row, next_col, cur_len + 1))
                    visited[next_row][next_col] = True

    return shortest_path_len

# 그래프
grid1 = [[0,0,0],[1,1,0],[1,1,0]]

# 출력: 4
print(ShortestPathBinaryMatrix(grid1))
