import requests as r
import json
from parse import Parse
from lxml.html import fromstring
from lxml.etree import ParserError
from lxml.etree import ParseError

def start():

    URL = "http://hackingwpzhxqe3a.onion/author/admin/index.html"
    s = r.Session()
    s.proxies = {
        'http': 'socks5h://localhost:9150',
        'https': 'socks5h://localhost:9150'
    }

    linkList = [URL]
    validLinks = [URL]
    iter = 0
    parser = Parse()
    while True:
        for linkUntilAppend in range(10):
            print(iter)
            if iter > len(linkList):
                return
            try:
                req = s.get(linkList[iter], allow_redirects=False, verify=False, timeout=10)
            except r.Timeout:
                print("{}  Timed out".format(linkList[iter]))
                iter+=1
                continue
            except r.ConnectionError:
                print("{}  Actively refused".format(linkList[iter]))
                iter+=1
                continue
            if req.status_code == 200:
                try:
                    validLinks.append(req.url + "   title=  {}".format(fromstring(req.content).findtext('.//title')))
                except (ParserError, ParseError):
                    validLinks.append(req.url + "   title=Was Empty")
                # print(fromstring(req.content).findtext('.//title'))
                parser.updateReq(req)
                parser.updatelinkList(linkList)
                gotLinks = parser.parse()
                for gottenLinks in gotLinks:
                    linkList.append(gottenLinks)
                iter+=1
            else:
                iter+=1
        else:
            jsonAppender(validLinks)


def jsonAppender(linkList):
    data = {'links': linkList}

    with open("links.json", 'w') as jsFile:
        json.dump(data, jsFile, sort_keys=True, indent=4)


if __name__ == "__main__":
    start()
    print("Done")
