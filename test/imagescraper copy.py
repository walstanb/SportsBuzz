from selenium import webdriver
import urllib.request
from urllib.request import Request
import pymongo
import time
import _thread

conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/sportsbuzzdb?retryWrites=true&w=majority")
db = conn["sportsbuzzdb"]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()

player_stats=[]
[player_stats.append(x) for x in db.Epl_player_img.find()]

#img = driver.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
#src = img.get_attribute('src')

site= "https://cdn.sofifa.com/players/203/376/20_240.png"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib.request.Request(site, headers=hdr)
page = urllib.request.urlopen(req)
#webpage = urlopen(req).read()
output = open("file01.jpg","wb")
output.write(page.read())
output.close()