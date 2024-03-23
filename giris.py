from girisUserInfo import username ,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

class İnsGiris:
    def __init__(self,username,password):
     self.browser=webdriver.Chrome()
     self.username=username
     self.password=password
      
      
    def giris(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        emailInput = self.driver.find_element(By.NAME,"username")
        passwordInput = self.driver.find_element(By.NAME,"password")
        emailInput.send_keys(username)
        sleep(5)
        passwordInput.send_keys(password)
        sleep(5)
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
        loginButton.click()
        sleep(5)
        
        kaydedilsinmi=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        kaydedilsinmi.click()
        sleep(5)
        
        bildirimler=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        bildirimler.click()
        sleep(5)
        mesaj=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div")
        mesaj.click()
        sleep(10)
        MesajGonder=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/div[1]")
        MesajGonder.click()
        sleep(10)
        mesajInput=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
        mesajInput.send_keys("Merhaba ,Nasılsınız")
        mesajInput.send_keys(Keys.ENTER)  #enter tuşuna basma
        sleep(5)
        
        
        
    

testclass=İnsGiris(username,password)
testclass.giris() 
