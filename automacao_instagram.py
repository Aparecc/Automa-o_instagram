import pyautogui


#Pressionar a tecla Windows
pyautogui.press("win")

pyautogui.PAUSE = 2
#Digitar Chrome
pyautogui.write("chrome")

#Pressionar Enter para Entrar no Chrome
pyautogui.press("enter")

pyautogui.sleep (1)

#Escrever o link do Instagram
pyautogui.write("https:/www.instagram.com")

#Pressionar o Enter para entrar no Site do Instagram
pyautogui.press("enter")

pyautogui.sleep (2)
#Achar Posição do Mouse em cima do Email e Clicar 
pyautogui.click(x=829, y=314)

pyautogui.PAUSE = 0
#Colocar o Email ou Nome do Usuário
pyautogui.write("Digite seu email Aqui")

#Descer Para a barra de Senha
pyautogui.press("Tab") 

#Inserir a Senha 
pyautogui.write("Digite sua senha Aqui")

#Dar Um Tab Para pressionar o botão iniciar
pyautogui.press("Tab")
pyautogui.press("Tab")
pyautogui.press("Enter")

pyautogui.sleep (5)
#Clicar na Barra Pesquisar Para Achar o Perfil a entrar
pyautogui.click(x=33, y=298)

pyautogui.sleep (3)
#Clicar no Perfil
pyautogui.click(x=264, y=363)

#Clicar nos Seguidores
pyautogui.click(x=848, y=230)

#Ir Clicando e Seguindo um por um até o final
