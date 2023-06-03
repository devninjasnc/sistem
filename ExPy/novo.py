import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import threading
import subprocess
rec = sr.Recognizer()




def falar():
    engine = pyttsx3.init()
    engine.say('''Olá, me chamo Júlia e sou atendente virtual do SESC IPARANA. Digite: 
        [1] Se você deseja fazer uma reserva
        [2] Se você deseja fazer um check-in
        [3] Serviços de comorbidade
        [4] Informações Locais e atrações turísticas''')
    engine.runAndWait()

# Criação da janela principal
janela = tk.Tk()

# Define as dimensões da janela
largura = 1366
altura = 768
janela.geometry(f"{largura}x{altura}")
janela.title('SESC IPARANA')

# Carregamento e exibição da imagem em tela cheia
imagem_principal = Image.open("magens\iparan.png")
imagem_principal = imagem_principal.resize((largura, altura))
imagem_principal_tk = ImageTk.PhotoImage(imagem_principal)

label_imagem_principal = tk.Label(janela, image=imagem_principal_tk)
label_imagem_principal.pack()

# Carregamento e redimensionamento da imagem do botão
imagem_botao = Image.open("magens\saibamais.png")
imagem_botao = imagem_botao.resize((200, 100))
imagem_botao_tk = ImageTk.PhotoImage(imagem_botao)

def vocêfalou():
    falar=pyttsx3.init()
    falar.say('Você apertou em saiba mais')
    falar.runAndWait()
    
def criar_janela_secundaria():
    # Criação da janela secundária (Toplevel)
    janela_secundaria = tk.Toplevel
    janela_secundaria.title('Janela Secundária')
    largura = 1366
    altura = 768
    janela_secundaria.geometry(f"{largura}x{altura}")
    janela_secundaria.title('SESC IPARANA2')
def saiba_mais():
    print("Botão 'Saiba Mais' pressionado")
def doiscomando():
    saiba_mais()
    vocêfalou()
def escutar_comando():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        while True:
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            if 'reserva' in texto.lower():
                falaa = pyttsx3.init()
                falaa.say('Que bom tê-lo conosco,vamos fazer a sua reserva!')
                falaa.runAndWait()
                comando = ["python", "novo.py"]
                subprocess.Popen(comando)
                criar_janela_secundaria()
            elif 'repetir' in texto.lower():
                falaa = pyttsx3.init()
                falaa.say('''[1] Se você deseja fazer uma reserva
                [2] Se você deseja fazer um check-in
                [3] Serviços de comorbidade
                [4] Informações Locais e atrações turísticas''')
                falaa.runAndWait()
                continue

            



# Criação do botão com a imagem
botao_saiba_mais = tk.Button(janela, image=imagem_botao_tk,command=criar_janela_secundaria,borderwidth=0)
botao_saiba_mais.place(x=100, y=100)

imagem = Image.open("magens\saibamais.png")
imagem = imagem.resize((100, 100))  # Ajustar o tamanho da imagem, se necessário
imagem_tk = ImageTk.PhotoImage(imagem)


# Inicialização do mecanismo de fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Iniciar a fala após a janela estar aberta
janela.after(1000, falar)
janela.after(1000,escutar_comando)

# Iniciar a escuta contínua em um thread separado
thread = threading.Thread(target=escutar_comando)
thread.daemon = True
thread.start()

# Execução da janela principal
janela.mainloop()