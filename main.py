import customtkinter as ctk
from tkinter import messagebox


#Funcoes
def clicar_no_botao():
    print("Olá, Mundo Moderno! O botão foi clicado.")
    rotulo.configure(text="Botão clicado!")
    
#Janela Principal
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Youtube Downloader with yt-dlp")
janela.geometry("400x300")

#Botão
botao = ctk.CTkButton(janela, text="Clique aqui", command=clicar_no_botao)
botao.pack(pady=10)

#Entrada de links
entrada = ctk.CTkEntry(janela,text= "Digite o link do vídeo", width=300)
entrada.pack(pady=10)


# 2. Criar um rótulo (CTkLabel)
rotulo = ctk.CTkLabel(janela, text="Bem-vindo ao meu programa!")
rotulo.pack(pady=20)

janela.mainloop()
#Fim do programa