import sys
import math

def cal_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def parsing_coor(coor):
    parts = coor.split(",")
    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}")
    x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
    return (x, y, z)

def demonstration(p):
    x, y, z = p
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

def main():
    print("=== Game Coordinate System ===")
    init_position = (0, 0, 0)
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                coord_str = sys.argv[i]
                print(f"\nParsing coordinates: \"{coord_str}\"")
                parsed_pos = parsing_coor(coord_str)
                print(f"Parsed position: {parsed_pos}")
                distance = cal_distance(init_position, parsed_pos)
                print(f"Distance between {init_position} and {parsed_pos}: {distance:.2f}")
                print("Unpacking demonstration:")
                demonstration(parsed_pos)
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")

    else:
        new_position = (10, 20, 5)
        print(f"Position created: {new_position}")
        distance = cal_distance(init_position, new_position)
        print(f"Distance between {init_position} and {new_position}: {distance:.2f}")
        print("\nParsing coordinates: \"3,4,0\"")
        try:
            teleport = parsing_coor("3,4,0")
            print(f"Parsed position: {teleport}")
            distance = cal_distance(init_position, teleport)
            print(f"Distance between {init_position} and {teleport}: {distance}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        try:
            parsing_coor("abc,def,ghi")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        print("\nUnpacking demonstration:")
        demonstration(teleport)
main()
