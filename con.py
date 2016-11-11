import sys
try:
	import requests
except ImportError:
	print "Install requests module first!"
	print "Use 'sudo pip install requests'"
	print "To install pip use 'sudo apt-get install python-pip'"

try:
	from bs4 import BeautifulSoup
except ImportError:
	print "Install BeautifulSoup module first!"
	print "Use 'sudo pip install BeautifulSoup'"
	print "To install pip use 'sudo apt-get install python-pip'"

#----------------------color class-----------------------#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#----------------------/color class-----------------------#


#'''
#-----------------------codechef-------------------------#

def CODECHEF():
	print color.BOLD + color.UNDERLINE + color.RED + "CodeChef" + color.END
	print '\n'
	codechefUrl =  "https://www.codechef.com/contests"
	r = requests.get(codechefUrl)
	soup = BeautifulSoup(r.content, "lxml")
	data = soup.find_all("div", {"class": "content-wrapper"})
	for table in data:
		tables = table.find_all("table", {"class": "dataTable"}, limit=2)  #limit = 2 will stop finding the table 3 which contains past contests as it will stop after finding only first two tables in data 
		futureness=0 # futureness = 0 means the contest is active and running and 1 means it is in future
		itemNamer=0
		for tr in tables:
			td = tr.find_all('td')
			if futureness == 0:
				print color.UNDERLINE + "ACTIVE CONTESTS\n" + color.END
			if futureness == 1:
				print color.UNDERLINE + "FUTURE CONTESTS\n" + color.END
			futureness+=1
			itemNamer=0
			for data in td:
				#not printing contest code as it is not necessyay to print itemcode use itemNamer=0
				if itemNamer == 1:
					print color.BOLD + color.BLUE + "Contest Name         : " + color.END + color.YELLOW + data.text + color.END
				if itemNamer == 2:
					print color.BOLD + color.BLUE + "Start Date and Time  : " + color.END + data.text
				if itemNamer == 3:
					print color.BOLD + color.BLUE + "End Date and Time    : " + color.END + data.text + "\n"
				itemNamer+=1
				if itemNamer == 4:
					itemNamer = 0
#-----------------------/codechef-------------------------#
#'''
#'''
#-----------------------codeforces-------------------------#

#to see earlier contest just change '<' sign with '>'
#0 is the contest-id of the contest
#it will show you the list of all previous contests and it is a long list
#program is written to show active or upcoming contests so the there may be formatting problems associated with it
#also it may show you some wrong values

def CODEFORCES():
	print color.BOLD + color.UNDERLINE + color.RED + "CodeForces" + color.END
	print '\n'
	codeforcesUrl = "http://codeforces.com/contests"
	r = requests.get(codeforcesUrl)
	soup = BeautifulSoup(r.content, "lxml")
	a_data = soup.find_all("div", {"class": "datatable"}, limit=1)
	codeforces = []
	for table in a_data:
		contests = table.find_all("tr")
		for tr in contests:
			td = tr.find_all("td")
			itemNamer=0
			for data in td:
				if tr["data-contestid"] > "0":
					if itemNamer == 0:
						print color.BOLD + color.BLUE + "Contest Name        : " + color.END + color.YELLOW + data.text.strip(' ').strip('\r').strip('\n') + color.END
					elif itemNamer == 2:
						print color.BOLD + color.BLUE + "Start Date and Time : " + color.END + data.text.strip(' ').strip('\r').strip('\n')
					elif itemNamer == 3:
						print color.BOLD + color.BLUE + "Length of Contest   : " + color.END + data.text.strip(' ').strip('\r').strip('\n').strip('\r').strip(' ') + " hrs"
					elif itemNamer == 5:
						temp = data.text.strip(' ').strip('\r').strip('\n').strip(' ')
						time1 = temp[-8:]
						#print [temp]
						if time1[6] == 'y' or time1[-2] == 'k':
							time2 = temp[-7:]
							print color.BOLD + color.BLUE + "Before registration : " + color.END + time2 + '\n' 
						else:
							if temp[-1]=='n':
								time3 = temp[-32:-24]	
								print color.BOLD + color.BLUE + "Register before     : " + color.END + time3 + " hrs to participate" + '\n'
							else:
								print color.BOLD + color.BLUE + "Before registeration : " + color.END + time1 + " hrs remaining" + '\n'
					if itemNamer > 5:
						itemNamer=0
					itemNamer+=1
#-----------------------/codeforces-------------------------#
#'''
#'''
#--------------------------spoj----------------------------#
def SPOJ():
	print color.BOLD + color.UNDERLINE + color.RED + "Spoj" + color.END
	print '\n'
	spojUrl =  "http://www.spoj.com/contests/"
	r = requests.get(spojUrl)
	soup = BeautifulSoup(r.content, "lxml")

	data = soup.find_all('div', {'class': 'row'})
	for table in data:
		tables = table.find_all("table", {"class": "table table-condensed"})
		futureness=0
		for tr in tables:
			td = tr.find_all('td')
			if futureness == 0:
				print color.UNDERLINE + "ACTIVE CONTESTS\n" + color.END
			if futureness == 1:
				print color.UNDERLINE + "FUTURE CONTESTS\n" + color.END
			futureness+=1
			itemNamer=0
			for data in td:
				if itemNamer == 0:
					print color.BOLD + color.BLUE + "Contest Name  : " + color.END + color.YELLOW + data.text + color.END
				elif itemNamer == 1:
					print color.BOLD + color.BLUE + "Start Date    : " + color.END + data.text
				elif itemNamer == 2:
					print color.BOLD + color.BLUE + "End Date      : " + color.END + data.text + "\n"
				itemNamer+=1
				if itemNamer > 2:
					itemNamer = 0 
#--------------------------/spoj----------------------------#
#'''
''' 	
#-----------------------hackerearth-------------------------#


#-----------------------/hackerearth-------------------------#
#-----------------------hackerrank--------------------------#


#-----------------------/hackerrank--------------------------#

'''
if len(sys.argv) == 1:
	CODEFORCES()
	CODECHEF()
	SPOJ()
elif sys.argv[1] == 'cf':
	CODEFORCES()
elif sys.argv[1] == 'cc':
	CODECHEF()
elif sys.argv[1] == 'sp':
	SPOJ()
else:
	print "Enter a valid argument:"
	print "cf for Codeforces\ncc for Codechef\nsp for Spoj"