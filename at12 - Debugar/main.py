from selenium import webdriver
import time

# o que é selenium
# instalação do selenium
# tenha sempre a documentação aberta
# webdriver - como funciona e caso dê erro o que fazer: video na descrição - dificuldade em editores de código online
navegador = webdriver.Chrome()

# abrindo um navegador em um site
link = "https://www.hashtagtreinamentos.com/curso-python"
navegador.get(link)

# maximizar a tela
navegador.maximize_window()

# encontrar um elemento na tela
botao_verde = navegador.find_element('class name', 'botao-verde')

# clicar no elemento
botao_verde.click()

# encontrar vários elementos na tela
botoes_navbar = navegador.find_elements('class name', 'header__item')
print(len(botoes_navbar))
for botao in botoes_navbar:
    if "Assinatura" in botao.text:
        botao_assinatura = botao
        break

botao_assinatura.click()

# agora eu quero acessar outra página (vou voltar aqui para o botao verde)

# acessar outra página
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# mudar de aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

navegador.get("https://www.hashtagtreinamentos.com/curso-python")


# escrever no elemento
navegador.find_element("id", "firstname").send_keys("Lira")
navegador.find_element("id", "email").send_keys("pythonimpressionador@gmail.com")
navegador.find_element("id", "phone").send_keys("21999999999")

# colocar um elemento na tela - executar códigos javascript
botao_verde = navegador.find_elements("class name", "botao-verde")[0]
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_verde)

# espera automática do selenium x wait manual com time.sleep x wait por algum elemento

#opcao 1:
time.sleep(3)
botao_verde.click()

# opcao 2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)  # Aguarda no máximo 10 segundos
elemento_clicavel = espera.until(EC.element_to_be_clickable(botao_verde))
botao_verde.click()


print("Abriu")
time.sleep(10)