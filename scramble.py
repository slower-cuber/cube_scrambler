from twophase import solver
from twophase.cubie import CubieCube


def get_random_state_cube() -> CubieCube:
    cube = CubieCube()
    cube.randomize()
    return cube


def inverse_solution(solution_str: str) -> str:
    """Takes *special* format from twophase library"""
    move_tokens = [t for t in solution_str.split(' ')
                   if not t.startswith('(')]

    inverse_moves = []
    for move in reversed(move_tokens):
        if move[1] == '1':
            inverse_moves.append(move[0]+"'")
        elif move[1] == '2':
            inverse_moves.append(move)
        elif move[1] == '3':
            inverse_moves.append(move[0])
        else:
            raise ValueError('Parsing error in twophase lib output')

    return ' '.join(inverse_moves)


def gen_scramble():
    # Check the implementation of randomize() in the twophase library
    # Notice how the cube is created by choosing EO, CO, EP, CP in random
    # rather than applying a bunch of random "moves"
    random_cube = get_random_state_cube()

    cube_solution_str = solver.solve(random_cube.to_facelet_cube().to_string())

    scramble = inverse_solution(cube_solution_str)

    print(scramble)
    print(random_cube.to_facelet_cube().to_2dstring())
    # print(cube_solution_str)


if __name__ == '__main__':
    gen_scramble()
