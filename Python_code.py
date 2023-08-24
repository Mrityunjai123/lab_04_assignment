class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def search_by_location(self, location_name):
        location_matches = [match for match in self.matches if location_name == match.location]
        return location_matches

    def search_by_timing(self, timing_name):
        timing_matches = [match for match in self.matches if timing_name == match.timing]
        return timing_matches

matches = [
    Match("Mumbai", "India", "Sri Lanka", "DAY"),
    Match("Delhi", "England", "Australia", "DAY-NIGHT"),
    Match("Chennai", "India", "South Africa", "DAY"),
    Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
    Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
    Match("Delhi", "India", "Australia", "DAY")
]

flight_table = FlightTable()
for match in matches:
    flight_table.add_match(match)

while True:
    print("Search Options:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        team_name = input("Enter the team name: ")
        team_matches = flight_table.search_by_team(team_name)
        for match in team_matches:
            print(f"{match.team1} vs {match.team2} at {match.location} ({match.timing})")
    elif choice == 2:
        location_name = input("Enter the location name: ")
        location_matches = flight_table.search_by_location(location_name)
        for match in location_matches:
            print(f"{match.team1} vs {match.team2} at {match.location} ({match.timing})")
    elif choice == 3:
        timing_name = input("Enter the timing: ")
        timing_matches = flight_table.search_by_timing(timing_name)
        for match in timing_matches:
            print(f"{match.team1} vs {match.team2} at {match.location} ({match.timing})")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please select a valid option.")