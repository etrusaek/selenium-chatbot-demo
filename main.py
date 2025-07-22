from plataformas import betaki #importo todas as casas da pasta que tem módulo configurado
import time


INTERVALO = 180 #3 minutos

#Mensagem promocional principal
MENSAGEM = "🚀 Venha para nosso grupo de sinais no Telegram: t.me/seuGrupo 🔥"

#Inicializa as plataformas
plataformas = [betaki] #menciono as casas importadas

if __name__ == "__main__":
    driver = betaki.iniciar_navegador()
    betaki.login(driver)
    betaki.abrir_chat(driver)

    while True:
        betaki.enviar_mensagem(driver, MENSAGEM)
        time.sleep(INTERVALO)