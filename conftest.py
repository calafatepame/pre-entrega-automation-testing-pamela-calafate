import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver

# Carpeta donde se guardan el log y las capturas
CARPETA_REPORTS = "reports"
os.makedirs(CARPETA_REPORTS, exist_ok=True)

# Configuración del log: se guarda en reports/ejecucion.log
logging.basicConfig(
    filename=os.path.join(CARPETA_REPORTS, "ejecucion.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8",
)


@pytest.fixture
def driver():
    """Abre Chrome antes de cada test y lo cierra siempre al terminar."""
    logging.info("Abriendo navegador")
    navegador = webdriver.Chrome()
    yield navegador
    logging.info("Cerrando navegador")
    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Registra el resultado de cada test y saca una captura si falla."""
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call":
        logging.info("Test %s -> %s", item.name, reporte.outcome.upper())

        if reporte.failed and "driver" in item.funcargs:
            marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta = os.path.join(CARPETA_REPORTS, f"fallo_{item.name}_{marca_tiempo}.png")
            item.funcargs["driver"].save_screenshot(ruta)
            logging.error("Captura guardada en %s", ruta)