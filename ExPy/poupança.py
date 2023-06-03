import speech_recognition as sr

# Crie um objeto de reconhecimento de fala
r = sr.Recognizer()

# Abra o microfone para gravação
with sr.Microphone() as source:
    print("Ajustando para ruído ambiente. Aguarde...")
    # Ajuste para ruído ambiente
    r.adjust_for_ambient_noise(source)
    print("Pronto! Comece a falar.")

    # Aguarde o usuário falar algo
    audio = r.listen(source)

# Use o reconhecimento de fala para converter o áudio em texto
try:
    text = r.recognize_google(audio)
    print("Você disse:", text)
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print("Erro ao solicitar resultados do serviço de reconhecimento de fala:", str(e))
