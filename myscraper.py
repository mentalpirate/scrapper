#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import os
import csv

def csv_writer(data, path):
#Open CSV file whose path we passed.
    with open(path, "w",encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#getting credentials for login
with open("cred.txt","r") as f:
    data = f.readlines()
    user_id = data[0]
    psd_id = data[1]
    
#######################MAIN################################3
driver = webdriver.Chrome("D://Webdriver//chromedriver.exe",options = options)
driver.get("https://linkedin.com/login")
#entering credentials for loginin
user = driver.find_element_by_xpath("//*[@name='session_key']")
user.send_keys(user_id)
psd = driver.find_element_by_xpath("//*[@name='session_password']")
psd.send_keys(psd_id)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)


#finding employee button and clicking
driver.get("https://linkedin.com/company/twitter")
time.sleep(2)
emp = driver.find_element_by_xpath("//a[@class='ember-view']")
emp.click()
time.sleep(2)

#selecting the employee names 
prof = driver.find_elements_by_css_selector(".mb1 a")
names = driver.find_elements_by_css_selector(".mb1 .app-aware-link span[aria-hidden]")
bio = driver.find_elements_by_css_selector(".mb1 div.entity-result__primary-subtitle")
location = driver.find_elements_by_css_selector(".mb1 div.entity-result__secondary-subtitle")
mylist = []
for i in range(0, len(names)):
    mylist.append([prof[i].get_attribute("href"),names[i].text,bio[i].text,location[i].text])


#generating csv


            
csv_writer(mylist,"output.csv")

#making dirs for projects files
import os
os.mkdir("Employee")
for newnames in names:
    os.mkdir("Employee/" + newnames.text)
    folders = ["Education","Experience","Projects"]
    for i in folders:
        os.mkdir("Employee/" + newnames.text+ "/" + i)
        csv_writer(mylist,"Employee/" + newnames.text+ "/" + i + "/" + i +".csv")



##future work below ##


# for prolink in proflink_list:
#     driver.get(prolink)
    
#     #extractor()
#     #scraping education 
   
#     uni_name = driver.find_elements_by_css_selector("#ember291 > div.pvs-list__outer-container > ul > li > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a > div > span > span:nth-child(1)")
#     uni_link = driver.find_elements_by_css_selector("#ember291 > div.pvs-list__outer-container > ul > li > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a")
#     degree = driver.find_elements_by_css_selector("#ember291 > div.pvs-list__outer-container > ul > li > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a > span > span:nth-child(1)")
#     start = driver.find_elements_by_css_selector("#ember170 > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a > span.t-14.t-normal.t-black--light > span:nth-child(1)")
#     details = driver.find_elements_by_css_selector("#ember291 > div.pvs-list__outer-container > ul > li > div > div.display-flex.flex-column.full-width.align-self-center > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div > div > div > div > span:nth-child(1)")
#     loop = [uni_name,uni_link,degree,start,details]
#     print(loop)
    

#     #proj = driver.find_elements_by_css_selector("#ember")
#     #proj_link = driver.find_elements_by_css_selector().get_attribute("href")
#     #details = driver.find_elements_by_css_selector()
#     #start_end = driver.find_elements_by_css_selector()

#     #scraping experience 
#     pos = driver.find_elements_by_css_selector("#ember286 > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div.display-flex.flex-column.full-width.align-self-center > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a > div > span > span:nth-child(1)")
#     company = driver.find_elements_by_css_selector("#ember286 > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a > div > span > span:nth-child(1)")
#     com_link = driver.find_elements_by_css_selector("#ember286 > div.pvs-list__outer-container > ul > li:nth-child(1) > div > div.display-flex.flex-column.full-width.align-self-center > div.display-flex.flex-row.justify-space-between > a")
#     location = ""
#     start_end  = "" 
#     details = ""
    
#     pol = [pos,company,com_link,location,start_end]
#     print(pol)
#     #code for os manupulation

