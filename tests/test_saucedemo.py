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


def test_catalogo_productos_visibles():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login (el mismo de antes: cada test es independiente)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperamos a que aparezcan TODOS los productos
    productos = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    # Verificamos que haya al menos uno
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    # Tomamos el primer producto de la lista
    primer_producto = productos[0]

    # Dentro de ese producto, buscamos su nombre y su precio
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    # Validamos que no estén vacíos y mostramos los datos
    assert nombre != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"El precio debería empezar con '$', se obtuvo '{precio}'"
    print(f"Primer producto: {nombre} - {precio}")

    assert driver.title == "Swag Labs", f"Título esperado 'Swag Labs', obtenido '{driver.title}'"

    driver.quit()


def test_elementos_interfaz_presentes():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    
# Login (el mismo de antes: cada test es independiente)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # TODO 1: esperar a que el botón de menú sea visible
    # TODO 2: esperar a que el filtro de orden sea visible

    # TODO 3: verificar con assert que ambos se muestran

    driver.quit()

def test_elementos_interfaz_presentes():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login (cada test es independiente)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperamos a que el botón de menú (las 3 rayitas) sea visible
    menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
    )

    # Esperamos a que el filtro de orden (desplegable) sea visible
    filtro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

    # Verificamos que ambos se estén mostrando
    assert menu.is_displayed(), "El botón de menú no está visible"
    assert filtro.is_displayed(), "El filtro de orden no está visible"
    assert driver.title == "Swag Labs", f"Título esperado 'Swag Labs', obtenido '{driver.title}'"

    driver.quit()