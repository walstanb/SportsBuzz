from selenium import webdriver
import urllib.request
import pymongo
import time
import _thread

'''
conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/sportsbuzzdb?retryWrites=true&w=majority")
db = conn["sportsbuzzdb"]
player_stats=[]
[player_stats.append(x) for x in db.Epl_player_img.find()]
'''

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.headless = True 
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()

'''driver.header_overrides = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}'''

#img = driver.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
#src = img.get_attribute('src')


def beginthread(pg,file2):
    #print(str(player['Image'])+"\t"+str(player['Id']))
    driver.get("https://sofifa.com/teams?type=all&col=ti&sort=asc&showCol%5B0%5D=ti&showCol%5B1%5D=oa&showCol%5B2%5D=at&showCol%5B3%5D=md&showCol%5B4%5D=df&showCol%5B5%5D=tb&showCol%5B6%5D=ps&showCol%5B7%5D=dw&offset="+str(pg))
    page_state = driver.execute_script('return document.readyState;')
    print(page_state)
    for i in range(1,61):
        team_name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[2]/a[1]/div")
        country_info = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[2]/a[2]/div/img")
        league_name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[2]/a[2]/div")
        team_id = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[3]")
        ovr = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[4]/span")
        att = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[5]/span")
        mid = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[6]/span")
        deff = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[7]/span")
        transfer_budget = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[8]")
        width = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[9]")
        no_of_players = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[10]")
        hits = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/table/tbody/tr["+str(i)+"]/td[11]")
        print("Writing row : offset "+str(pg)+" line "+str(i))
        #file2.write(team_name.text+", "+country_info.get_attribute("title")+", "+country_info.get_attribute("data-src")[29:]+", "+league_name.text+", "+team_id.text+", "+ovr.text+", "+att.text+", "+mid.text+", "+deff.text+", "+transfer_budget.text+", "+width.text+", "+no_of_players.text+", "+hits.text+"\n")

#file2 = open("test/teamsdatfwefwea.csv","w",encoding="utf-8")
file2=None
#beginthread(0,file2)

for pg in range(0,721,60):
    beginthread(pg,file2)

#file2.close()
driver.close()
