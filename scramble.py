from twophase import solver
from twophase.cubie import CubieCube, basicMoveCube


def apply_moves(cube: CubieCube, moves: str):
    d2i = {'U': 0, 'R': 1, 'F': 2, 'D': 3, 'L': 4, 'B': 5}
    for m in [_m.strip() for _m in moves.split(' ')]:
        direction = m[0]
        mag = 1
        if len(m) == 2:
            if m[1] == '2':
                mag = 2
            elif m[1] == '3' or m[1] == "'":
                mag = 3
        for i in range(mag):
            cube.multiply(basicMoveCube[d2i[direction]])


def get_random_state_cube() -> CubieCube:
    cube = CubieCube()
    apply_moves(cube, "U R2 B2 L2 D' B2 R2 F2 U' R' F D' R2 U' B' D' L F D2 U2 U")
    #cube.randomize()
    #cube.set_twist(451)
    #cube.multiply(basicMoveCube[0]) #URFDLB
    print(cube.get_twist())
    print(cube.get_flip())
    print(cube.get_corners())
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

    cube_solution_str = solver.solve(
        random_cube.to_facelet_cube().to_string()
    )

    scramble = inverse_solution(cube_solution_str)

    print(f"\nSC: {scramble}\n")
    print(random_cube.to_facelet_cube().to_2dstring())
    # print(cube_solution_str)


if __name__ == '__main__':
    gen_scramble()
