# Automação simples com Selenium para pesquisar "Engenharia de software" na Wikipédia
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver do Chrome (certifique-se de que o chromedriver esteja instalado e configurado no PATH)
driver = webdriver.Chrome()

# Acessa a página principal da Wikipédia em português
driver.get("https://www.wikipedia.org")
time.sleep(2)  # Aguarda o carregamento da página

# Localiza o campo de busca usando o ID "searchInput" e realiza a busca
try:
    campo_busca = driver.find_element(By.ID, "searchInput")
    campo_busca.send_keys("Engenharia de software")
    campo_busca.send_keys(Keys.ENTER)  # Pressiona ENTER para buscar
    time.sleep(2)  # Aguarda a página de resultados carregar
except Exception as e:
    print("Erro ao realizar a busca:", e)

# Opcional: Salva um screenshot da página resultante como 'screenshot.png'
driver.save_screenshot("screenshot.png")
print("Screenshot salvo como 'screenshot.png'")

# Fecha o navegador
driver.quit()
