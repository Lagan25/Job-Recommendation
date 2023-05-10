from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

options = Options()   
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)


def get_job_data():
    df = pd.DataFrame(columns=["Title","Location","Company","Salary","Job Description"])

    for i in range(0,10,10):
            counter = 0
            driver.get('https://www.indeed.co.in/jobs?q=artificial%20intelligence&l=India&start='+str(i))
            time.sleep(random.randint(1,4))
            results_list = driver.find_elements(By.CLASS_NAME, value = 'resultContent')
            for j in range(0,len(results_list)) :
                    if counter > 0:

                        driver.get('https://www.indeed.co.in/jobs?q=artificial%20intelligence&l=India&start='+str(i))
                        time.sleep(random.randint(1,4))
                        results_list = driver.find_elements(By.CLASS_NAME, value = 'resultContent')
                    counter+=1
                    soup = BeautifulSoup(results_list[j].get_attribute('innerHTML'),'html.parser')

                    try:
                            title = soup.find("h2",class_="jobTitle").text.strip()
                            
                    except:
                            title = 'None'

                    try:
                            link = soup.find("a",href = True)
                            link_string = 'https://www.indeed.com'+link['href']
                            driver.get(link_string)
                            time.sleep(random.randint(1,4))
                            job_description = driver.find_element(By.CLASS_NAME, value = 'jobsearch-jobDescriptionText').get_attribute("innerText")
                           
                            
                    except:
                            job_description = 'None'     

                    
                    try:
                            location = soup.find(class_="companyLocation").text
                    except:
                            location = 'None'

                     
                    try:
                        company = soup.find(class_="companyName").text.replace("\n","").strip()
                    except:
                        company = 'None'
                    
                
                    try:
                        salary = soup.find(class_="salary-snippet-container").text.replace("\n","").strip()
                    except:
                        salary = 'None'
                    
         
                    df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,"Job Description":job_description},ignore_index=True)

    return df 

df_job = get_job_data()
df_job.to_csv("data.csv", index = False)