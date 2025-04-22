# test_list_rooms.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_list_rooms():
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
        
        # Acessar listagem
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Listar Quartos"))
        ).click()
        
        # Verificar tabela
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='room-table']"))
        )
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_list_rooms()
