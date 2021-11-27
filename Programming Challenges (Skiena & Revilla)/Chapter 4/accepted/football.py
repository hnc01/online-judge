from sys import stdin
import functools


# input the tournament name, team names and games played
# output the tournament standings so far.

def compare_teams(a, b):
    a = a[1]
    b = b[1]
    # teams_profiles[team] = {
    #     "total_points": 0,
    #     "total_wins": 0,
    #     "total_goals_scored": 0,
    #     "total_goals_against": 0,
    #     "total_games_played": 0
    # }
    if a['total_points'] > b['total_points']:
        return 1
    elif a['total_points'] < b['total_points']:
        return -1
    else:
        # equal points
        if a['total_wins'] > b['total_wins']:
            return 1
        elif a['total_wins'] < b['total_wins']:
            return -1
        else:
            # equal wins
            if (a['total_goals_scored'] - a['total_goals_against']) > (b['total_goals_scored'] - b['total_goals_against']):
                return 1
            elif (a['total_goals_scored'] - a['total_goals_against']) < (b['total_goals_scored'] - b['total_goals_against']):
                return -1
            else:
                # equal goal difference
                if a['total_goals_scored'] > b['total_goals_scored']:
                    return 1
                elif a['total_goals_scored'] < b['total_goals_scored']:
                    return -1
                else:
                    # equal goals scored
                    if a['total_games_played'] < b['total_games_played']:
                        return 1
                    elif a['total_games_played'] > b['total_games_played']:
                        return -1
                    else:
                        # equal games played
                        # finally sort by lexicographic order
                        if a['name'].lower() > b['name'].lower():
                            return -1
                        elif a['name'].lower() < b['name'].lower():
                            return 1
                        else:
                            return 0


def extract_game_info(game_line):
    team_split = game_line.split("@")

    team_a_info = team_split[0].split("#")
    team_b_info = team_split[1].split("#")

    team_a_name = team_a_info[0]
    team_a_goals = int(team_a_info[1])

    team_b_name = team_b_info[1]
    team_b_goals = int(team_b_info[0])

    return ({"name": team_a_name, "goals": team_a_goals}, {"name": team_b_name, "goals": team_b_goals})


def build_teams_profiles(teams, games):
    # for each team we need
    # 1) total points
    # 2) total wins
    # 3) total goals scored
    # 4) total goals against
    # 5) total number of games

    teams_profiles = {}

    for team in teams:
        teams_profiles[team] = {
            "name": team,
            "total_points": 0,
            "total_wins": 0,
            "total_ties": 0,
            "total_losses": 0,
            "total_goals_scored": 0,
            "total_goals_against": 0,
            "total_games_played": 0
        }

    # team A wins if goals(A) > goals(B) // team A loses if goals(A) < goals(B) // tie if goals(A) = goals(B)
    # A wins => + 3 // A ties => + 1 // A loses => +0
    for game in games:
        # ({'name': 'Brazil', 'goals': 2}, {'name': 'Scotland', 'goals': 1})
        team_1 = game[0]
        team_2 = game[1]

        if team_1['goals'] > team_2['goals']:
            # team 1 won
            teams_profiles[team_1['name']]['total_points'] += 3
            teams_profiles[team_1['name']]['total_wins'] += 1
            teams_profiles[team_1['name']]['total_goals_scored'] += team_1['goals']
            teams_profiles[team_1['name']]['total_goals_against'] += team_2['goals']
            teams_profiles[team_1['name']]['total_games_played'] += 1

            teams_profiles[team_2['name']]['total_losses'] += 1
            teams_profiles[team_2['name']]['total_goals_scored'] += team_2['goals']
            teams_profiles[team_2['name']]['total_goals_against'] += team_1['goals']
            teams_profiles[team_2['name']]['total_games_played'] += 1
        elif team_1['goals'] < team_2['goals']:
            # team 2 won
            teams_profiles[team_2['name']]['total_points'] += 3
            teams_profiles[team_2['name']]['total_wins'] += 1
            teams_profiles[team_2['name']]['total_goals_scored'] += team_2['goals']
            teams_profiles[team_2['name']]['total_goals_against'] += team_1['goals']
            teams_profiles[team_2['name']]['total_games_played'] += 1

            teams_profiles[team_1['name']]['total_losses'] += 1
            teams_profiles[team_1['name']]['total_goals_scored'] += team_1['goals']
            teams_profiles[team_1['name']]['total_goals_against'] += team_2['goals']
            teams_profiles[team_1['name']]['total_games_played'] += 1
        else:
            # team 1 and team 2 tie
            teams_profiles[team_2['name']]['total_points'] += 1
            teams_profiles[team_1['name']]['total_points'] += 1

            teams_profiles[team_2['name']]['total_ties'] += 1
            teams_profiles[team_1['name']]['total_ties'] += 1

            teams_profiles[team_1['name']]['total_games_played'] += 1
            teams_profiles[team_2['name']]['total_games_played'] += 1

            teams_profiles[team_1['name']]['total_goals_scored'] += team_1['goals']
            teams_profiles[team_1['name']]['total_goals_against'] += team_2['goals']

            teams_profiles[team_2['name']]['total_goals_scored'] += team_2['goals']
            teams_profiles[team_2['name']]['total_goals_against'] += team_1['goals']

    return teams_profiles


while True:
    try:
        N = int(input())

        for case in range(0, N):
            if case != 0:
                print()

            # we won't just do strip because maybe the name of the tournament includes spaces at the end
            tournament_name = stdin.readline().rstrip("\n")

            # number of teams participating in tournament
            T = int(input())

            # the team names
            teams = []

            for team in range(0, T):
                teams.append(stdin.readline().rstrip("\n"))

            # the number of games played
            G = int(input())

            # the games played
            games = []

            for game in range(0, G):
                games.append(extract_game_info(stdin.readline().rstrip("\n")))

            team_profiles = build_teams_profiles(teams, games)

            team_profiles = sorted(team_profiles.items(), key=functools.cmp_to_key(compare_teams), reverse=True)

            print(tournament_name)

            rank = 1
            for team_profile in team_profiles:
                team_profile = team_profile[1]

                print(str(rank) + ") " + team_profile['name'] + " "
                      + str(team_profile['total_points']) + "p, "
                      + str(team_profile['total_games_played']) + "g "
                      + "(" + str(team_profile['total_wins']) + "-" + str(team_profile['total_ties']) + "-" + str(team_profile['total_losses']) + "), "
                      + str(team_profile['total_goals_scored'] - team_profile['total_goals_against']) + "gd "
                      + "(" + str(team_profile['total_goals_scored']) + "-" + str(team_profile['total_goals_against']) + ")")

                rank += 1
        break
    except EOFError:
        break
