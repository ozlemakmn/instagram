from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




class Kaydol:
    def __init__(self):
        self.browser=webdriver.Chrome()
     
    
    def kayit_ol(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.instagram.com/") 
        sleep(1)
        kayitolbutton=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[2]/span/p/a")
        kayitolbutton.click()
        sleep(2)
        emailInput=driver.find_element(By.NAME,"emailOrPhone")
        emailInput.send_keys("ozlemakman16")
        sleep(2)
        adInput = driver.find_element(By.NAME,"fullName")
        adInput.send_keys("özlem")
        sleep(2)
        kullaniciad=driver.find_element(By.NAME,"username")
        kullaniciad.send_keys("akman123")
        sleep(2)
        öneri =driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div[1]/div/div")
        öneri.click()
        sleep(2)
        öneri2= driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]")
        öneri2.click()
        passwordInput=driver.find_element(By.NAME,"password")
        passwordInput.send_keys("123456789")
        sleep(2)
        kayitoluşturbutton=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[9]/div/button")
        kayitoluşturbutton.click()
        errorMessage= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ssfErrorAlert")))
        testResult = errorMessage.text == "Bu şifreyi tahmin etmek çok kolay. Lütfen yeni bir şifre oluştur."
        sleep(3)
        print(f"TEST SONUCU: {testResult}")

testclass=Kaydol()
testclass.kayit_ol()       