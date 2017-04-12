#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

resources_file = open("./resources.csv", "r")
resources = resources_file.read().split(",")
resources_file.close()

resources_file2 = open("./resources.csv", "w")
resources_file2.write("{0},{1},{2}".format(int(resources[0]), resources[1], '0'))
resources_file2.close()

form = cgi.FieldStorage()


roomUrl = form["URL"].value
transporterUrl = form["transporter"].value

properUrl = transporterUrl + "?URL=" + roomUrl + "&inventory="

print "Content-type: text/html\n\n"
print properUrl
#print "location:{0}\r\n".format(properUrl)


