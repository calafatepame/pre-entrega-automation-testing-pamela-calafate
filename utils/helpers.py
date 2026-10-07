from selenium.webdriver.common.by import By


def hacer_login(driver, usuario="standard_user", password="secret_sauce"):
    """Abre saucedemo.com e inicia sesión con las credenciales indicadas."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()