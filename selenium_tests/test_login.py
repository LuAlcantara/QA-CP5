import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRestfulBookerLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ajuste para o caminho do chromedriver se necessário
        self.driver.get("http://localhost:3003/admin")
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_success(self):
        # Cenário 1: Login com credenciais corretas
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.send_keys("admin")
        password_field.send_keys("password")
        login_button.click()
        
        self.wait.until(EC.url_to_be("http://localhost:3003/admin/rooms"))
        # Verificar a presença do quarto 101 na lista de quartos
        rooms_list = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='roomlisting']")))
        self.assertIn("101", rooms_list.text)
        self.assertEqual(self.driver.current_url, "http://localhost:3003/admin/rooms")

    def test_login_wrong_password(self):
        # Cenário 2: Login com senha incorreta
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.send_keys("admin")
        password_field.send_keys("wrongpassword")
        login_button.click()
        
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))
        self.assertIn("Invalid credentials", error_message.text)

    def test_login_verify_rooms_page(self):
        # Cenário 3: Login e verificar elemento na página de rooms
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.send_keys("admin")
        password_field.send_keys("password")
        login_button.click()
        
        self.wait.until(EC.url_to_be("http://localhost:3003/admin/rooms"))
        # Verificar a lista de quartos e a presença do quarto 101
        rooms_list = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='roomlisting']")))
        self.assertIn("101", rooms_list.text)

    def test_login_empty_credentials(self):
        # Cenário 4: Login com campos vazios
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        login_button.click()
        
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))
        self.assertIn("Invalid credentials", error_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()