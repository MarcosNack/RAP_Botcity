
"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
import pyautogui as gui
from time import sleep
import os
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *str


def ConsultaCNPJ():
    bot = DesktopBot()
    
    caminho = os.path.dirname(__file__)
    
    print(f"Caminho file: {caminho}")
    # Opens the BotCity website.
    bot.browse(str("https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"))

    camp = 0
    
    sleep(3)
    gui.hotkey("Win", "up")
    
    # Clicar no campo pesquisa
    t = 0
    while bot.find_text( "cnpj", threshold=230, waiting_time=2000) == None:
        if t == 5:
            camp = 1
            break
        t += 1
    
    if camp == 0:
        bot.find_text( "cnpj", threshold=230, waiting_time=0)
        bot.click()
    
        # Informar o CNPJ para consulta
        sleep(1)
        bot.paste("81905176000194")
        
        # Clicar no checkbox captcha
        t = 0
        while bot.find( "check_cap", matching=0.97, waiting_time=1000) == None:
            if t == 5:
                camp = 1
                break
            t += 1

        if camp == 0:
            bot.find( "check", matching=0.97, waiting_time=0)
            bot.click()
                            
            # Validar o captcha
            t = 0
            while bot.find( "conf_cap", matching=0.97, waiting_time=5000) == None:
                if t == 5:                        
                    break
                t += 1
            
            # Clicar no botão consulta
            t = 0
            while bot.find( "consulta", matching=0.97, waiting_time=1000) == None:            
                bot.scroll_down(200) 
                if t == 5:
                    break
                t += 1           
                
            bot.click()
        
            
            # Cartão CNPJ encontrado
            t = 0
            while bot.find( "cartao_cnpj", matching=0.97, waiting_time=5000) == None:
                if t == 5:
                    camp = 1
                    break
                
            if camp == 0:
                # Salvar o cartão CNPJ
                gui.hotkey("Ctrl", "s")
                sleep(2)
                bot.paste(f"{caminho}\CNPJ.html")
                sleep(2)
                gui.press("Enter")
        

ConsultaCNPJ()
