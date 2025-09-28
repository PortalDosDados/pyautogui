import pyautogui as py
import time
import subprocess as sp

# Configurações do PyAutoGUI
py.FAILSAFE = True  # permite mover o mouse para o canto para parar o script
py.PAUSE = 0.5      # pausa entre cada comando do PyAutoGUI

# Caminho da imagem que será localizada
tl_inicial = 'assets/tl_ecc.png'

# Caminho do SAP Logon
sap_path = 'C:/Program Files (x86)/SAP/FrontEnd/SapGui/saplogon.exe'

# Abrir o SAP Logon
print("Abrindo o SAP Logon...")
sp.Popen(sap_path)

# Esperar o SAP abrir completamente (ajuste o tempo se necessário)
print("Aguardando o SAP abrir...")
time.sleep(8)

# Loop de tentativa para localizar a imagem
pos = None
tentativas = 20  # tenta localizar por 20 segundos
for i in range(tentativas):
    pos = py.locateCenterOnScreen(tl_inicial, confidence=0.8)
    if pos:
        py.doubleClick(pos)
        print(f"Imagem encontrada na posição {pos} e clicada!")
        break
    time.sleep(1)

# Caso não encontre a imagem
if not pos:
    print("Imagem não encontrada após 20 segundos. Verifique resolução, escala ou caminho da imagem.")

