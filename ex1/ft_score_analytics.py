import sys

args =sys.argv

scores = []

print("=== Player Score Analytics ===")

for arg in args[1:]:
    try:
        arg = int(arg)
        scores.append(arg)
    except ValueError:
        pass
if len(scores) > 0:
    print(f"Scores processed:{scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
else:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
