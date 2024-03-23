from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 



class Sifremiunuttum:
    def __init__(self):
        self.browser=webdriver.Chrome()
     
    
    def sifremi_unuttum(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.instagram.com")
        sleep(2)
        unuttumbutton = driver.find_element(By.XPATH,"//*[@id='loginForm']/a/span")
        unuttumbutton.click()    
        sleep(2)
        unuttumInput=driver.find_element(By.NAME,"cppEmailOrUsername")
        unuttumInput.send_keys("mail")
        sleep(2)
        Baglantigonder=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[5]/div")
        Baglantigonder.click()
        
        
testclass=Sifremiunuttum()  
testclass.sifremi_unuttum()      