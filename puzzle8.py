import  copy
dirs = [(-1,0),(1,0),(0,1),(0,-1)]


MAX_MOVES = 12
solutions = 0


def find_a_path(curr_loc, path, solutions):
    if len(path) == MAX_MOVES:
        solutions[0]+=1
        path.pop()
        return

    for indx, next_move in enumerate(dirs):
        loc_move_to = (curr_loc[0] + next_move[0],curr_loc[1]+next_move[1])

        if loc_move_to not in path:
            path.append(loc_move_to)
            find_a_path(loc_move_to, path,solutions)
        else:
            # find_a_path(curr_loc, [])
            continue

        if indx == len(dirs)-1:
            path.pop()


if __name__ == '__main__':
    moves = list()
    start_loc = (0, 0)
    solutions=[0]
    find_a_path(start_loc, moves,solutions=solutions)
    print(solutions)