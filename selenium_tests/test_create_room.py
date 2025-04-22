# test_create_room.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_create_room():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    
    try:
        # Login
        driver.get("http://localhost:3003/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        
        # Navegar para criação de quartos
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Criar Quarto"))
        ).click()
        
        # Preencher formulário
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "roomName"))
        ).send_keys("101")
        
        driver.find_element(By.ID, "type").send_keys("Single")
        driver.find_element(By.ID, "price").send_keys("150")
        
        # Submeter
        driver.find_element(By.XPATH, "//button[contains(text(),'Salvar')]").click()
        
        # Verificar listagem
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'101')]"))
        )
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_create_room()
