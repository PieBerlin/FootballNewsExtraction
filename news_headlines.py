from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import pandas as pd


website="https://www.thesun.co.uk/sport/football/"
path="C:\\Users\\USER\\Documents\\ChromeDriver\\chromedriver-win64.exe"

service=Service(executable_path=path)
# chrome_options=Options()
chrome_options=uc.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

#headless mode
chrome_options.headless=True

driver=webdriver.Chrome(service=Service(),options=chrome_options)
driver.get(website)

containers=driver.find_elements(by="xpath",value='//div[@class="layout__item"]')

titles=[]
subtitles=[]
links=[]

# //div[@class="layout__item"]/div[1]/div[1]/div[2]/a/h3
for container in containers:
    title=container.find_element(by="xpath",value='./div[1]/div[1]/div[2]/a/p').text
    subtitle=container.find_element(by="xpath",value='./div[1]/div[1]/div[2]/a/h3').text
    link=container.find_element(by="xpath",value='./div[1]/div[1]/div[2]/a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict={'title':titles,'subtitle':subtitles,'link':links}

df_headlines=pd.DataFrame(my_dict)
df_headlines.to_csv("headline.csv")

driver.quit()





