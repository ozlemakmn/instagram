from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 


class İnstagramLogin:
    def __init__(self):
        self.browser=webdriver.Chrome()
        
    def login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.instagram.com/accounts/login")
        sleep(1)
        emailInput = driver.find_element(By.NAME,"username")
        passwordInput = driver.find_element(By.NAME,"password")
        emailInput.send_keys("22222222")
        sleep(2)
        passwordInput.send_keys("555555s")
        sleep(2)
        loginButton = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
        loginButton.click()
    
        
        errorMessage= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/span")))
        testResult = errorMessage.text == "Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et."
        print(f"TEST SONUCU: {testResult}")
        
  

testclass = İnstagramLogin()
testclass.login()


