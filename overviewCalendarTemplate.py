from string import Template
import json
from userFunctions import *
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

headHtml = head()

#Sidebar top with title of course offering
sidebarButtons = sidebar("unit")

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = mobileSidebar("unit")


# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

# Substitute settings unitData with appropriate variables 
result = templateString.safe_substitute(   
    head = headHtml,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
