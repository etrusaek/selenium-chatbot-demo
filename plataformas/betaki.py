from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def iniciar_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver):
    driver.get("https://www.betaki.com/")
    print("🔐 Faça login manualmente na Betaki.")
    input("✅ Pressione Enter após o login estar concluído...")

def abrir_chat(driver):
    print("🎯 Navegue até o jogo desejado e abra o chat maior manualmente.")
    input("✅ Pressione Enter quando o chat estiver visível na tela...")

def enviar_mensagem(driver, mensagem):
    try:
        # Localiza o formulário
        form = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[10]/div/div[1]/div/div/div/div/div[3]/div/div/form')
        
        # Localiza o campo de input dentro do formulário
        campo = form.find_element(By.TAG_NAME, 'input')
        
        campo.clear()
        campo.click()
        campo.send_keys(mensagem)
        time.sleep(0.3)
        campo.send_keys(Keys.ENTER)

        print("✅ Mensagem enviada com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem: {e}")


