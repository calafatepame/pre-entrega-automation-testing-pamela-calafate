import logging
import os
from datetime import datetime

from selenium.webdriver.common.by import By


def hacer_login(driver, usuario="standard_user", password="secret_sauce"):
    """Abre saucedemo.com e inicia sesión con las credenciales indicadas."""
    logging.info("Iniciando login con el usuario %s", usuario)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def tomar_captura(driver, nombre_test):
    """Guarda una captura de pantalla en reports/ con el nombre del test que falló."""
    os.makedirs("reports", exist_ok=True)  # si la carpeta ya existe, no hace nada
    marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = f"reports/fallo_{nombre_test}_{marca_tiempo}.png"
    driver.save_screenshot(ruta)
    logging.error("El test %s falló. Captura guardada en %s", nombre_test, ruta)
    