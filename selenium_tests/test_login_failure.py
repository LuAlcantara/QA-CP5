# test_login_failure.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_failure():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    
    try:
        # Acessar página de login
        driver.get("http://localhost:3003/")
        
        # Preencher credenciais inválidas
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("admin")
        
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        
        # Submeter formulário
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        
        # Verificar mensagem de erro
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'error-message')]"))
        )
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_failure()
