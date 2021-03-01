def solution(board, moves):
    new_list = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                new_list.append(board[j][i-1])
                board[j][i-1] = 0

                if len(new_list) > 1:
                    if new_list[-1] == new_list[-2]:
                        new_list.pop(-1)
                        new_list.pop(-1)
                        answer += 2     
                break

    return answer
