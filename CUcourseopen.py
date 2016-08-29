import requests
from bs4 import BeautifulSoup

"""API for retreiving open status of a course. Made by Sitar."""

# if a proxy is necessary, uncomment the following lines
# these are free ones I found online
proxyDict = { 
#               "http"  : "http://104.238.149.146:8080", 
#               "https" : "https://104.238.149.146:8080"
            }

def getOpen(courseid):
    """Returns a dictionary defining which class within courseid is open. 
       Dictionary is formatted as: classnumber:'open/closed'"""
    page = requests.get(str("https://classes.cornell.edu/browse/roster/FA16/class/" + 
                        courseid[:-4] + "/" + courseid[-4:]), proxies=proxyDict)
    soup = BeautifulSoup(page.text, 'lxml')
    numList = []
    for x in soup.find_all("strong", class_="tooltip-iws"):
        numList += [x.getText().encode("utf-8")]
    openstat = {}
    iter = 0
    for x in soup.findAll('i', {"class":True}):
        openstat[numList[iter]] = x['class'][2].split("-", 2)[2]
        iter += 1
    return(openstat)