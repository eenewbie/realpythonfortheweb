from xml.etree import ElementTree as et
import requests

xml = requests.get("http://maps.googleapis.com/maps/api/directions/xml?origin=San+Francisco&destination=Los+Angeles&sensor=false&mode=driving")

with open("directions.xml", "wb") as code:
	code.write(xml.content)

doc = et.parse("directions.xml")

#for route in doc.findall("route"):
#	for leg in route.findall("leg"):
#		for step in leg.findall("step"):
#			print step.find("html_instructions").text, "\n"

for leg in doc.findall("route/leg"):
	print "Start: " + leg.find("start_address").text
	print "End: " + leg.find("end_address").text

print "Directions: "

for step in doc.findall("route/leg/step"):
	print step.find("html_instructions").text