from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def download_files_web_scraping(url, file_path):
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": file_path,  # Caminho onde os PDFs serão salvos
        "download.prompt_for_download": False,  # Não perguntar onde salvar
        "plugins.always_open_pdf_externally": True  # Baixar PDF ao invés de abrir no Chrome
    })

    # Inicializar o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Abrir a página onde está o PDF
    driver.get(url)

    # Aguardar carregar (caso necessário)
    time.sleep(3)
    driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Aceitar cookies"]').click() #clicar em aceitar cookies
    # Clicar no link para baixar o PDF
    botao_download_anexo_i = driver.find_element(By.CSS_SELECTOR, "a[href*='Anexo_I_'][href*='.pdf']")
    botao_download_anexo_ii = driver.find_element(By.CSS_SELECTOR, "a[href*='Anexo_II_'][href*='.pdf']")
    botao_download_anexo_i.click() #comando para quando o downlaod abre outra página
    botao_download_anexo_ii.click() #comando para quando o downlaod abre outra página

    # Aguardar o download finalizar
    time.sleep(5)

    # Fechar o navegador
    driver.quit()
