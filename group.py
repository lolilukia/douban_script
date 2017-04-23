#coding=utf-8
import subprocess
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import smtplib  
from email.mime.text import MIMEText  
from email.MIMEMultipart import MIMEMultipart  
from email.Header import Header
from collections import deque
import codecs
import time
import re
mailto_list=['124724272@qq.com']
mail_host="smtp.163.com"
mail_user="lolilukia"
mail_pass="lj940905"    
mail_postfix="163.com" 
def send_mail(to_list,sub,content):  
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.douban.com/group/explore")
search = driver.find_element_by_id("inp-query")
search.click()
search.send_keys(u'青旅客栈求职招聘')
time.sleep(0.5)
submit = driver.find_element_by_class_name("inp-btn")
submit.click()
time.sleep(1)
result = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/h3/a")
result.click()
time.sleep(1)
var = 1
upTitle = []
normalTitle = []
while var==1 :
	for i in range(3, 61):
		OPath = '//*[@id="group-topics"]/div[2]/table/tbody/tr['+'%d'%i+']'+'/td/span'
		XPath = '//*[@id="group-topics"]/div[2]/table/tbody/tr['+'%d'%i+']'+'/td/a'
		latest = driver.find_element_by_xpath(XPath).text
		try:
			up = driver.find_element_by_xpath(OPath)
			if latest not in upTitle:
				if latest.find(u'上海')!= -1:
					upTitle.append(latest)
					send_mail(mailto_list,latest,'https://www.douban.com/group/515813/')
		except Exception, e:
			if latest not in normalTitle:
				if latest.find(u'上海')!= -1:
					normalTitle.append(latest)
					send_mail(mailto_list,latest,'https://www.douban.com/group/515813/')
	time.sleep(60)
	driver.refresh()
driver.close()