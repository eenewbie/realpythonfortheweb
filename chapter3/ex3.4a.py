from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

print doc.find("CAR[3]/MODEL").text