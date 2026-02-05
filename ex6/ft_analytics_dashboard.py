#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist
Demonstrates list, dictionary, and set comprehensions for
elegant data transformation and analysis.
"""




def get_game_data():
    """Return the game analytics dataset."""
    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
             'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
             'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
             'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
             'mode': 'ranked', 'completed': True},
            {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
             'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
             'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
             'mode': 'casual', 'completed': True},
            {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
             'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
             'mode': 'casual', 'completed': False},
            {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
             'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
             'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
             'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 46, 'score': 329,
             'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
             'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
             'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
             'mode': 'competitive', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
             'mode': 'ranked', 'completed': False},
            {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
             'mode': 'ranked', 'completed': False},
            {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
             'mode': 'ranked', 'completed': False},
            {'player': 'alice', 'duration_minutes': 101, 'score': 292,
             'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
             'mode': 'competitive', 'completed': True},
            {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
             'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 115, 'score': 147,
             'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
             'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
             'mode': 'casual', 'completed': False},
            {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
             'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
             'mode': 'competitive', 'completed': True},
            {'player': 'bob', 'duration_minutes': 52, 'score': 761,
             'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
             'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
             'mode': 'casual', 'completed': True}
        ],
        'game_modes': ['casual', 'competitive', 'ranked'],
        'achievements': [
            'first_blood', 'level_master', 'speed_runner',
            'treasure_seeker', 'boss_hunter', 'pixel_perfect',
            'combo_king', 'explorer'
        ]
    }
    return data


def list_comprehension_examples(data):
    """Demonstrate list comprehensions for filtering and transformation."""
    print("=== List Comprehension Examples ===")

    players = data['players']
    sessions = data['sessions']

    # Filter: High-level players (level > 30)
    high_level_players = [name for name, info in players.items()
                          if info['level'] > 30]
    print(f"High-level players (>30): {high_level_players}")

    # Transform: Double all player scores
    doubled_scores = [info['total_score'] * 2
                      for info in players.values()]
    print(f"Scores doubled: {doubled_scores}")

    # Filter: Active players (sessions > 20)
    active_players = [name for name, info in players.items()
                      if info['sessions_played'] > 20]
    print(f"Active players (>20 sessions): {active_players}")

    # Filter: High-scoring sessions (score > 2000)
    high_score_sessions = [session['player']
                           for session in sessions
                           if session['score'] > 2000]
    print(f"Players with high-score sessions: {high_score_sessions[:5]}")

    # Transform: Extract all session scores
    all_scores = [session['score'] for session in sessions]
    print(f"All session scores (first 10): {all_scores[:10]}")

    print()


def dict_comprehension_examples(data):
    """Demonstrate dictionary comprehensions for mappings and grouping."""
    print("=== Dict Comprehension Examples ===")

    players = data['players']

    # Create mapping: player name -> total score
    player_scores = {name: info['total_score']
                     for name, info in players.items()}
    print(f"Player scores: {player_scores}")

    # Create mapping: player name -> level
    player_levels = {name: info['level']
                     for name, info in players.items()}
    print(f"Player levels: {player_levels}")

    # Filter and map: Only high achievers (>= 5 achievements)
    high_achievers = {name: info['achievements_count']
                      for name, info in players.items()
                      if info['achievements_count'] >= 5}
    print(f"High achievers (>=5): {high_achievers}")

    # Group by category: Count players by favorite mode
    all_favorite_modes = [info['favorite_mode'] for info in players.values()]
    mode_counter = {}
    for mode in all_favorite_modes:
        mode_counter[mode] = mode_counter.get(mode, 0) + 1
    mode_counts = {
        mode: mode_counter[mode]
        for mode in set(all_favorite_modes)
    }
    print(f"Players by mode: {mode_counts}")

    # Transform: player name -> average score per session
    avg_scores = {name: info['total_score'] // info['sessions_played']
                  for name, info in players.items()
                  if info['sessions_played'] > 0}
    print(f"Average score per session: {avg_scores}")

    print()


def set_comprehension_examples(data):
    """Demonstrate set comprehensions for unique data analysis."""
    print("=== Set Comprehension Examples ===")

    players = data['players']
    sessions = data['sessions']

    # Unique players in dataset
    unique_players = {name for name in players.keys()}
    print(f"Unique players: {unique_players}")

    # Unique game modes from sessions
    unique_modes = {session['mode'] for session in sessions}
    print(f"Unique modes played: {unique_modes}")

    # Unique players who completed sessions
    completed_players = {session['player'] for session in sessions
                         if session['completed']}
    print(f"Players with completions: {completed_players}")

    # High-level player names (level >= 40)
    high_level_set = {name for name, info in players.items()
                      if info['level'] >= 40}
    print(f"High-level players (>=40): {high_level_set}")

    # Players who played ranked mode
    ranked_players = {session['player'] for session in sessions
                      if session['mode'] == 'ranked'}
    print(f"Ranked mode players: {ranked_players}")

    print()


def combined_analysis(data):
    """Demonstrate combined comprehensions for complex analytics."""
    print("=== Combined Analysis ===")

    players = data['players']
    sessions = data['sessions']

    # Total unique players
    total_players = len(players)
    print(f"Total players: {total_players}")

    # Total unique achievements possible
    total_achievements = len(data['achievements'])
    print(f"Total achievements available: {total_achievements}")

    # Average level across all players
    avg_level = sum(info['level'] for info in players.values()) / total_players
    print(f"Average player level: {avg_level:.1f}")

    # Find top performer (highest total score)
    top_player = max(players.items(), key=lambda x: x[1]['total_score'])
    print(f"Top performer: {top_player[0]} "
          f"({top_player[1]['total_score']} points, "
          f"{top_player[1]['achievements_count']} achievements)")

    # Most active player (most sessions)
    most_active = max(players.items(),
                      key=lambda x: x[1]['sessions_played'])
    print(f"Most active: {most_active[0]} "
          f"({most_active[1]['sessions_played']} sessions)")

    # Completion rate
    total_sessions = len(sessions)
    completed_sessions = sum(1 for s in sessions if s['completed'])
    completion_rate = (completed_sessions / total_sessions) * 100
    print(f"Session completion rate: {completion_rate:.1f}%")


def main():
    """Main function demonstrating comprehensions."""
    print("=== Game Analytics Dashboard ===\n")

    # Get data
    data = get_game_data()

    # List comprehensions
    list_comprehension_examples(data)

    # Dictionary comprehensions
    dict_comprehension_examples(data)

    # Set comprehensions
    set_comprehension_examples(data)

    # Combined analysis
    combined_analysis(data)


if __name__ == "__main__":
    main()
