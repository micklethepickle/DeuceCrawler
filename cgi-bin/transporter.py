#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-type: text/html"

form = cgi.FieldStorage()

inventory = (form["inventory"].value).split(",")
mana = int(inventory[0])
gold = int(inventory[1])
roomUrl = form["url"].value

resources_file = open("../resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()

if int(resources[2]) == 1:
	#regenerate previous room using roomUrl with current gold and mana
	print "location:{0}\r\n".format(roomUrl)
elif int(resources[2]) == 0:
	#room is empty so generate our html
	resources_file = open("../resources.csv", "w")
	resources_file.write("{0},{1},{2}".format(mana, gold, '1'))
	resources_file.close()
	print "\n\n"
	print """
	<!DOCTYPE html>
			<html>
			<title>DeuceVille</title>
			<body style=\"text-align: center;\">

			<h1>Welcome to DeuceVille</h1>
			<center><img src=\"http://i.imgur.com/MwyPH84.jpg\" alt=\"DeuceVille\" style=\"width:800px;height:400px;\">
			</center>
			<h3>DROP succesful</h3>
			<form action=\"room.c\" method=\"post\">
			    <input type=\"text\" name=\"command\" placeholder=\"What will you do at DeuceVille?\" style=\"width:800px;\"></br>
			    <input title=\"commands: PLAY, DROP, EXIT, REFRESH\" style=\"width:100px; height:20px;\" type=\"submit\" value=\"Submit\">
			    <input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">
			</form>
			<center>
				<table>
					<tr>
						<th></th>
						<th>
							<form action=\"http://google.com\">
								<input type=\"submit\" value=\"North\" />
							</form>
						</th>
						<th></th>
					</tr>
					<tr>
						<th>
							<form action=\"http://google.com\">
								<input type=\"submit\" value=\"West\" />
							</form>
						</th>
						<th></th>
						<th>
							<form action=\"http://google.com\">"
								<input type=\"submit\" value=\"East\" />
							</form>
						</th>
					</tr>
					<tr>
						<th></th>
						<th>
							<form action=\"http://google.com\">
								<input type=\"submit\" value=\"South\" />
							</form>
						</th>
						<th></th>
					</tr>
				</table>
			</center>

			</body>
			</html>
	"""

