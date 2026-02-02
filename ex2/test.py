import math
import sys

try:
    t_points_1 = ()
    i = 1

    while i < len(sys.argv):
        for el2 in sys.argv[i].split(","):
            t_points_1 += (int(el2),)
        i += 1

    if len(t_points_1) != 3:
        print("Error !")
    else:
        print("=== Game Coordinate System ===\n")
        t_points_2 = (0, 0, 0)
        distance = float(
            math.sqrt(
                (t_points_1[0] - t_points_2[0])** 2
                + (t_points_1[1] - t_points_2[1])** 2
                + (t_points_1[2] - t_points_2[2]) ** 2
            )
        )
        if len(sys.argv) == 2:
            print(f'Parsing coordinates: "{sys.argv[1]}"')
            print("Parsed position:", end=" ")
        else:
            print("Position created:", end=" ")
        print(t_points_1)
        print(f"Distance between \
{t_points_2} and {t_points_1}:{distance: .2f}")
        print("Unpacking demonstration:")
        x, y, z = t_points_1
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
except ValueError as v:
    if len(sys.argv) == 2:
        print("Parsing", end=" ")
    print(f'invalid coordinates:"{sys.argv[1]}"')
    print(f"Error parsing coordinates: {v}")
    print(f'Error details - Type: {type(v).name}, Args: ("{v}")')
