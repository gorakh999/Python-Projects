from game_data import TEAM
import replit

def available_team():
    l1 = [item for item in TEAM.keys()]
    return l1

def display_players(team):
    for name, point in team.items():
        print(f"{name} {point}")


def list_player(team1, team2):
    l1 = []
    for name, point in team1.items():
        temp = [name, str(point)]
        temp = " ".join(temp)
        l1.append(temp)

    for name, point in team2.items():
        temp = [name, str(point)]
        temp = " ".join(temp)
        l1.append(temp)
    return l1

total_credit = 200
selected_players = []

if __name__ == '__main__':
    replit.clear()
    print(f"Available Teams are {available_team()}")
    print("\n*******Choose Your Teams******\n")
    team1 = input("Enter Team 1 Name : ")
    team2 = input("Enter Team 2 Name : ")
    
    whole_team = {**TEAM[team1], **TEAM[team2]}
    available_players = list_player(TEAM[team1], TEAM[team2])

    while(True):
        if (len(selected_players) == 11):
            print("\n\nTeam Choosen Successfully\n")
            print("Your Fantasy Team is : \n")
            print(*selected_players, sep="\n")
            break

        elif (total_credit <= 0):
            print("\n\nNo Credit Points Remaining\n")
            print("Your Fantasy Team is : \n")
            print(*selected_players, sep="\n")
            break

        else:
            print("\n*************************************************************************")
            print(f"\nYou have {total_credit} Credits Remaining")
            print(f"Total Player Selected : {len(selected_players)}\n")
            print(*available_players, sep="\n")    
            player_name = input("\nEnter Player Name : ")
            if player_name in whole_team.keys():
                selected_players.append(player_name)
                total_credit -= whole_team[player_name]
                available_players = [x for x in available_players if player_name not in x]

            else:
                print("\n\nChoose Correct Player Name\n")