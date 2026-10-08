# Pre-entrega: Automatización de pruebas en saucedemo.com

## Propósito del proyecto

Automatizar con Selenium WebDriver y Python los flujos básicos de navegación de
[saucedemo.com](https://www.saucedemo.com), un sitio demo para practicar testing:

1. **Login** con credenciales válidas y validación de la redirección a `/inventory.html`
   (título "Swag Labs" y encabezado "Products").
2. **Catálogo**: título de la página, presencia de productos (se muestra nombre y precio
   del primero) y elementos de interfaz (menú y filtro de orden).
3. **Carrito**: agregar el primer producto, verificar el contador y que aparezca en el carrito.

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- pytest-html (reporte HTML)
- Git y GitHub

## Estructura del proyecto

```
├── tests/
│   └── test_saucedemo.py   # Casos de prueba
├── utils/
│   └── helpers.py          # Funciones auxiliares (login y captura de pantalla)
├── reports/                # Reporte HTML, capturas de fallos y log de ejecución
├── pytest.ini              # Configuración de Pytest (incluye el log)
├── requirements.txt        # Dependencias
└── README.md
```

## Instalación de dependencias

Necesitás Python 3 y Google Chrome instalados.

```bash
python3 -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Opcionalmente, se puede usar un entorno virtual para aislar las dependencias del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
```

## Cómo ejecutar las pruebas

```bash
pytest -v --html=reports/reporte.html
```

Para ver también los `print()` en la consola, agregá `-s`.

## Evidencias generadas

- `reports/reporte.html`: reporte de resultados de la ejecución.
- `reports/ejecucion.log`: registro de la ejecución.
- `reports/fallo_<test>_<fecha>.png`: captura de pantalla automática cuando un test falla.

## Decisiones de diseño

- **Tests independientes:** cada test abre su propio navegador y hace su propio login,
  por lo que la falla de uno no afecta a los demás.
- **Esperas explícitas** (`WebDriverWait`) en lugar de pausas fijas.
- **Capturas automáticas:** cada test captura la excepción, saca una captura de pantalla con
  `tomar_captura` y vuelve a lanzar el error; el navegador siempre se cierra en el `finally`.
- **Funciones auxiliares** en `utils/helpers.py` para no repetir código.