#PY script to get emails from linkedin specific URLs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time


regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))




driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/")
time.sleep(2)
assert "LinkedIn" in driver.title
elem = driver.find_element_by_id("login-email")
elem.send_keys("ADD_YOUR_USERNAME")

elem = driver.find_element_by_id("login-password")
elem.send_keys("ADD_YOUR_PASSWORD")

elem.send_keys(Keys.RETURN)
time.sleep(5)
all_urls = ['https://www.linkedin.com/in/PROFILE_TO_SCRAPE','https://www.linkedin.com/in/PROFILE_TO_SCRAPE2']
for url in all_urls:
	try:
		driver.get(url)
		time.sleep(2)
		div1 = driver.find_element(By.XPATH, '//div[@class="summary"]/p')
		div1 = div1.text
		div2 = driver.find_element(By.XPATH, '//div[@id="contact-comments-view"]/p')
		div2 = div2.text
		  
		divuri = div1 + div2
		print divuri
		time.sleep(2)
		x = re.findall(regex,divuri)
		for i in x:
			if not i[0].startswith('//'):
				print i[0]
	except:
		pass


driver.close()
