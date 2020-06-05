import constants
import copy

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)


def clean_player_data(players):
    cleaned_players_list = []

    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['height'] = int(player['height'][0:2])

        cleaned_player = {}
        cleaned_player['name'] = player['name']
        cleaned_player['height'] = player['height']
        cleaned_player['experience'] = player['experience']

        cleaned_players_list.append(cleaned_player)

    return cleaned_players_list


def balance_teams(cleaned_players_list, teams):
    extracted_players_names = []
    for player in cleaned_players_list:
        extracted_players_names.append(player['name'])

    populate_teams = {}
    for index, team in enumerate(teams):
        populate_teams[team] = []
        for player in extracted_players_names[index::len(teams)]:
            populate_teams[team].append(player)

    return populate_teams


def display_team_stats(filled_teams, selected_team):
    print(f"\nTeam: {list(populate_teams.keys())[selected_team - 1]} Stats")
    print("--------------------")
    print()
    print(f"Total Players: {int(len(players) / len(teams))}")
    print()
    print("Players on Team:")
    print()
    team_names = list(populate_teams.values())[selected_team - 1]
    team_names = ', '.join(team_names)
    print(team_names)
    print()
    input("Press Enter to continue...")
    print()
    display_first_menu(teams)


def display_team_names(teams):
    for team in teams:
        print(f" {teams.index(team) + 1}) {team}")
    print()
    keep_going = False
    while keep_going == False:
        try:
            selected_team = int(input("Enter an option > "))
        except ValueError:
            print("There is an issue with your input, please try again!")
            display_team_names(teams)
        else:
            if selected_team > 0 and selected_team <= len(teams):
                display_team_stats(populate_teams, selected_team)
                keep_going == True
            else:
                print("Please select an option for a team!")
                display_team_names(teams)


def display_first_menu(teams):
    """
    Show first menu to user.
    """
    print("---- MAIN MENU ----\n")
    print("Here are your choices:")
    print("1)  Display Team Stats")
    print("2) Quit")
    print()
    try:
        selection = int(input("Enter an option > "))
        if selection > 2 or selection < 1:
            raise ValueError("You can only enter either 1 or 2 please!")
    except ValueError as err:
        print(("{}".format(err)).upper())
        print()
        display_first_menu(teams)
    else:
        if selection == 1:
            display_team_names(teams)
        elif selection == 2:
            print("Thank you for using my stats tool!")
            quit()


if __name__ == "__main__":
    print("BASKETBALL TEAM STATS TOOL\n")
    cleaned_players_list = clean_player_data(players)
    populate_teams = balance_teams(cleaned_players_list, teams)
    display_first_menu(teams)
