import sys

args = sys.argv
print("=== Command Quest ===")

if len(args) == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print("Total arguments: 1")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(args) - 1}")
    j = 1
    for i in range(len(args) - 1):
        print(f"Argument {j}: {sys.argv[i + 1]}")
        j += 1
    print(f"Total arguments: {len(args)}")
