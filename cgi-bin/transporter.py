#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

print "Content-type: text/html"

form = cgi.FieldStorage()

inventory = (form["inventory"].value).split(",")
mana = int(inventory[0]) - 1
gold = int(inventory[1])
roomUrl = form["URL"].value

resources_file = open("./resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()

#out of mana game over screen
if mana == 0:
	print "\n\n"
	print """
	<!DOCTYPE html>
	<html>
	<body style="text-align: center;">
	<h1>GAME OVER, YOU RAN OUT OF MANA</h1>
	</body>
	</html>
	"""

elif int(resources[2]) == 1:
	#regenerate previous room using roomUrl with current gold and mana
	print "location:{0}\r\n".format(roomUrl)
elif int(resources[2]) == 0:
	#room is empty so generate our html
	resources_file = open("./resources.csv", "w")
	resources_file.write("{0},{1},{2}".format(int(resources[0])+1, resources[1], '1'))
	resources_file.close()
	print "\n\n"
	print """
			
				
		<!DOCTYPE html>
		<html>
		<title>DeuceVille</title>
		<body style="text-align: center;">

		<h1>Welcome to DeuceVille</h1>
		<center><img src="http://i.imgur.com/MwyPH84.jpg" alt="DeuceVille" style="width:800px;height:400px;">
		</center>
		<form action="http://www.cs.mcgill.ca/~mma106/cgi-bin/room.cgi" method="get">
		    <input type="text" name="command" placeholder="What will you do at DeuceVille?" style="width:800px;"/></br>
		    <input title="commands: PLAY, DROP, EXIT, REFRESH" style="width:100px
		      ;height:20px;" type="submit" value="Submit"/>
		    <input type="hidden" name="inventory" value="{0},{1}"/>
		</form>
		<center>
			<table>
				<tr>
					<th></th>
					<th>
						<form action="http://www.cs.mcgill.ca/~mma106/cgi-bin/transportOut.py" method="get">
							<input type="submit" value="North" />
							<input type="hidden" name="URL" value="http://www.cs.mcgill.ca/~mma106/cgi-bin/transporter.py?URL=nothing&inventory={0}%2C{1}"/>
							<input type="hidden" name=inventory value="{0},{1}" />
							<input type="hidden" name="transporter" value="http://www.cs.mcgill.ca/~walhas1/cgi-bin/transporter.py/"/>
						</form>
					</th>
					<th></th>
				</tr>
				<tr>
					<th>
						<form action="http://www.cs.mcgill.ca/~mma106/cgi-bin/transportOut.py">
							<input type="submit" value="West" />
							<input type="hidden" name="URL" value="http://www.cs.mcgill.ca/~mma106/cgi-bin/transporter.py?URL=nothing&inventory={0}%2C{1}"/>
							<input type="hidden" name=inventory value="{0},{1}" />
							<input type="hidden" name="transporter" value="http://www.cs.mcgill.ca/~walhas1/cgi-bin/transporter.py"/>
						</form>
					</th>
					<th></th>
					<th>
						<form action="http://www.cs.mcgill.ca/~mma106/cgi-bin/transportOut.py">
							<input type="submit" value="East" />
							<input type="hidden" name="URL" value="http://www.cs.mcgill.ca/~mma106/cgi-bin/transporter.py?URL=nothing&inventory={0}%2C{1}"/>
							<input type="hidden" name=inventory value="{0},{1}" />
							<input type="hidden" name="transporter" value="http://www.cs.mcgill.ca/~walhas1/cgi-bin/transporter.py"/>
						</form>
					</th>
				</tr>
				<tr>
					<th></th>
					<th>
						<form action="http://www.cs.mcgill.ca/~mma106/cgi-bin/transportOut.py">
							<input type="submit" value="South" />
							<input type="hidden" name="URL" value="http://www.cs.mcgill.ca/~mma106/cgi-bin/transporter.py?URL=nothing&inventory=10%2C10"/>
							<input type="hidden" name=inventory value="10,10" />
							<input type="hidden" name="transporter" value="http://www.cs.mcgill.ca/~walhas1/cgi-bin/transporter.py"/>
						</form>
					</th>
					<th></th>
				</tr>
			</table>
		</center>

		</body>
		</html>


	""".format(mana,gold)

