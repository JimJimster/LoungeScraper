from bs4 import BeautifulSoup # To get everything
import requests





class Match:
	def __init__(self,matchid = 0, team1odds = 0, team2odds = 0, team1 = 0, team2 = 0, win = 0)
	self.MatchID = MatchID
	self.team1odds = team1odds
	self.team2odds = team2odds
	self.team1 = team1
	self.team2 = team2
	self.win = win


currenturl = "http://csgolounge.com/match?m=6075"
r = requests.get(currenturl)

soup = BeautifulSoup(r.content, "html.parser")
#print(soup.encode('UTF-8'))
#print(soup.prettify().encode('UTF-8'))
#soup.find_all("a")

#links = soup.find_all("main")

text = soup.get_text('|', strip=True)

#print(text)


array = text.split("|")

index = 0
count = -1
subcount = 0

print("\n")

for segment in array:
	print(segment)
	count += 1
	if "Match" in segment:
		subsegment = segment.split(" ")
		MatchID = subsegment[-1]
	elif "hours ago" in segment:
		subsegment = segment.split(" ")
		Day = 0
	elif "days ago" in segment:
		subsegment = segment.split(" ")
		Day = subsegment[0]
	elif "Best of" in segment:
		subsegment = segment.split(" ")
		BestOf = subsegment[-1]
	elif "vs" in segment:
		team1 = array[count - 2]
		team1odds = array[count - 1]
		team2 = array[count + 1]
		team2odds = array[count + 2]
	elif "people placed" in segment:
		break

print("--- Output ---\n")
print("Match ID: ", MatchID)
print("Days ago: ", Day)
print("Best of: ", BestOf)
print(team1, ":", team1odds)
print(team2, ":", team2odds)




#for segment in array:
#	print(segment)