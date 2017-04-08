#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-type: text/html"

form = cgi.FieldStorage()

inventory = (form["inventory"].value).split(",")
mana = int(inventory[0]) - 1
gold = int(inventory[1])
roomUrl = form["url"].value

resources_file = open("resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()
	

print "\n\n"
print resources
print mana
print gold
print roomUrl