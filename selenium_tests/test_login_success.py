from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login_success():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),  options=options)
    driver.maximize_window()
    
    try:
        # Acessar página de login
        driver.get("http://localhost:3003/")
        
        # Preencher credenciais
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("admin")
        
        driver.find_element(By.ID, "password").send_keys("password")
        
        # Submeter formulário
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        
        # Verificar dashboard
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))
        )
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_success()
