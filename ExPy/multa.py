import tkinter as tk
import speech_recognition as sr

def ouvir():
    # Inicializa o objeto Recognizer
    r = sr.Recognizer()
    
    # Define o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Diga algo...")
        
        # Realiza a escuta do áudio
        audio = r.listen(source)
    
    try:
        # Utiliza o Google Speech Recognition para converter o áudio em texto
        texto = r.recognize_google(audio, language="pt-BR")
        
        # Adiciona o texto na entrada (entry)
        entry_texto.delete(0, tk.END)  # Limpa o conteúdo atual
        entry_texto.insert(tk.END, texto)  # Insere o novo texto
        
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio")
    except sr.RequestError as e:
        print("Erro na solicitação ao Google Speech Recognition: {0}".format(e))

# Criação da janela
janela = tk.Tk()

# Criação da entrada (entry)
entry_texto = tk.Entry(janela)
entry_texto.pack()

# Criação do botão para iniciar a escuta
botao_ouvir = tk.Button(janela, text="Ouvir", command=ouvir)
botao_ouvir.pack()

# Execução da janela
janela.mainloop()
