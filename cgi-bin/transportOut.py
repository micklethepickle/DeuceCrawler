#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

#setting room to not occupied

resources_file = open("./resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()

resources_file = open("./resources.csv", "w")
resources_file.write("{0},{1},{2}".format(int(resources[0]), resources[1], '0'))
resources_file.close()

form = cgi.FieldStorage()


#formatting get url
inventory = (form["inventory"].value).split(",")
mana = inventory[0]
gold = inventory[1]
roomUrl = form["URL"].value
transporterUrl = form["transporter"].value

properUrl = transporterUrl + "?URL=" + roomUrl + "&inventory=" + mana + "%2C" + gold

#going to other transporter
print "Content-type: text/html"
print "location:{0}\r\n".format(properUrl)


