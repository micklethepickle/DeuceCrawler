#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()


print "Content-type: text/html\n\n"


resources_file = open("./resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()

resources_file2 = open("./resources.csv", "w")
resources_file2.write("{0},{1},{2}".format(int(resources[0]), resources[1], '0'))
resources_file2.close()

form = cgi.FieldStorage()

inventory = (form["inventory"].value).split(",")
mana = inventory[0]
gold = inventory[1]
roomUrl = form["URL"].value
transporterUrl = form["transporter"].value

properUrl = transporterUrl + "?URL=" + roomUrl + "&inventory=" + mana + "%2C" + gold

print properUrl
#print "location:{0}\r\n".format(properUrl)


