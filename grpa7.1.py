'''A round-robin tournament is one in which each team competes with every other team. Consider a version of the IPL tournament in which every team plays exactly one game against every other team. All these games have a definite result and no match ends in a tie. The winning team in each match is awarded one point.

Eight teams participate in this round-robin cricket tournament: CSK, DC, KKR, MI, PK, RR, RCB and SH. You are given the details of the outcome of the matches. Your task is to prepare the IPL points table in descending order of wins. If two teams have the same number of points, the team whose name comes first in alphabetical order must figure higher up in the table.

There are eight lines of input. Each line is a sequence of comma-separated team names. The first team across these eight lines will always be in this order: CSK, DC, KKR, MI, PK, RR, RCB and SH. For a given sequence, all the other terms represent the teams that have lost to the first team. For example, the first line of input could be: CSK,MI,DC,PK. This means that CSK has won its matches against the teams MI, DC and PK and lost its matches against all other teams. If a sequence has just one team, it means that it lost all its matches.

Print the IPL points table in the following format — team:wins — one team on each line. There shouldn't be any spaces in any of the lines.'''



def create_points_table():
    teams = ["CSK", "DC", "KKR", "MI", "PK", "RR", "RCB", "SH"]
    wins = {team: 0 for team in teams}
    
    match_results = []
    for _ in range(8):
        line = input().strip()
        match_results.append(line)
    
    for line in match_results:
        match = line.split(',')
        winner = match[0]
        losers = match[1:]
        
        wins[winner] += len(losers)
    
    # Sort teams by wins (descending) and alphabetically if tied
    sorted_teams = sorted(wins.items(), key=lambda x: (-x[1], x[0]))
    
    # Display results
    for team, win_count in sorted_teams:
        print(f"{team}:{win_count}")

# Call the function
create_points_table()
