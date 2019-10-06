from bs4 import BeautifulSoup
import re


class Parse:

    def __init__(self):
        self.req = None
        self.linkList = []


    def parse(self):
        returnList = []
        parsedHTML = BeautifulSoup(self.req.content, 'html.parser')
        for links in parsedHTML.findAll("a"):
            link = str(links.get("href"))
            if link[:7] == "http://":
                if ".onion" not in link:
                    continue
                if re.split("^(.*?)\.onion", self.req.url) != re.split("^(.*?)\.onion", link):
                    returnList.append(link)
        return returnList


    def updateReq(self, req):
        self.req = req

    def updatelinkList(self, linkList):
        self.linkList = linkList