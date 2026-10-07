from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita: hasta 10 segundos a que la URL contenga /inventory.html
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Validación 1: la URL
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

    # Validación 2: el título de la pestaña
    assert driver.title == "Swag Labs", f"Título esperado 'Swag Labs', obtenido '{driver.title}'"

    # Validación 3: el encabezado "Products" (esperamos a que el elemento aparezca)
    elemento_titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    titulo = elemento_titulo.text
    assert titulo == "Products", f"Se esperaba 'Products', se obtuvo '{titulo}'"

    driver.quit()
    