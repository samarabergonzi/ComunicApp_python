import tkinter as tk
import pygame

# Dicionário de palavras, frases e arquivos de som correspondentes
word_phrase_sound_dict = {
    "Comida": {"frase": "Estou com fome.", "som": "C:\\Users\\Samara\\Nova_pasta\\sons\\estou com fome.mp3"},
    "Água": {"frase": "Quero beber água.", "som": "C:\\Users\\Samara\\Nova_pasta\\sons\\quero_beber_agua.mp3"},
    "Banheiro": {"frase": "Preciso ir ao banheiro.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\preciso ir ao banheiro.mp3" },
    "Brincar": {"frase":"Vamos brincar!", "som": "C:\\Users\\Samara\\Nova_pasta\\sons\\vamos brincar.mp3"},
    "Sono": {"frase": "Estou com sono.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\estou com sono.mp3"},
    "Frio": {"frase": "Estou com frio.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\estou com frio.mp3"},
    "Calor": {"frase": "Estou com calor.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\estou com calor.mp3"},
    "Medo": {"frase": "Estou com medo.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\estou com medo.mp3"},
    "Ficar Sozinho": {"frase": "Quero ficar sozinho.", "som":"C:\\Users\\Samara\\Nova_pasta\\sons\\quero ficar sozinho.mp3"},
    "Sim": {"frase": "Sim.", "som": "C:\\Users\\Samara\\Nova_pasta\\sons\\sim.mp3"},
    "Não": {"frase": "Não.", "som": "C:\\Users\\Samara\\Nova_pasta\\sons\\não.mp3"},
    # Adicione mais palavras, frases e arquivos de som conforme necessário
}  

def on_button_click(word):
    # Função chamada quando um botão é clicado
    if word in word_phrase_sound_dict:
        phrase = word_phrase_sound_dict[word]["frase"]
        sound_file = word_phrase_sound_dict[word]["som"]
        label.config(text=phrase)
        pygame.mixer.init()  # Inicializa o mixer pygame
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

# Crie a janela principal
root = tk.Tk()
root.title("COMUNICAÇÃO PARA CRIANÇAS")

# Crie um rótulo para exibir a frase
label = tk.Label(root, text="", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=4, pady=20)  # Coluna estendida para ocupar 4 colunas

# Dicionário de imagens correspondentes às palavras
word_image_dict = {
    "Comida": "C:\\Users\\Samara\\Nova_pasta\\food\\food.png",
    "Água": "C:\\Users\\Samara\\Nova_pasta\\water\\water.png",
    "Banheiro": "C:\\Users\\Samara\\Nova_pasta\\toilet\\toilet.png",
    "Brincar": "C:\\Users\\Samara\\Nova_pasta\\play\\play.png",
    "Sono": "C:\\Users\\Samara\\Nova_pasta\\sono\\sono.png",
    "Frio": "C:\\Users\\Samara\\Nova_pasta\\frio\\frio.png",
    "Calor": "C:\\Users\\Samara\\Nova_pasta\\calor\\calor.png",
    "Medo": "C:\\Users\\Samara\\Nova_pasta\\medo\\medo.png",
    "Ficar Sozinho": "C:\\Users\\Samara\\Nova_pasta\\ficar sozinho\\ficar sozinho.png",
    "Sim": "C:\\Users\\Samara\\Nova_pasta\\sim\\sim.png",
    "Não": "C:\\Users\\Samara\\Nova_pasta\\nao\\nao.png",
}

# Número de colunas na grade
num_columns = 4

# Contador para controlar a posição na grade
row_num = 1
col_num = 0

# Espaçamento horizontal e vertical entre os botões
padx = 20
pady = 20

for word in word_phrase_sound_dict.keys():
    if word in word_image_dict:
        button_image = tk.PhotoImage(file=word_image_dict[word])

        button = tk.Button(root, text=word, compound="top", width=210, height=210, font=("Arial", 16),
                           command=lambda w=word: on_button_click(w), image=button_image)
        button.image = button_image
        button.grid(row=row_num, column=col_num, padx=padx, pady=pady)

        # Atualize a posição na grade
        col_num += 1
        if col_num >= num_columns:
            col_num = 0
            row_num += 1

# Configuração para alinhar no centro horizontalmente
for i in range(num_columns):
    root.grid_columnconfigure(i, weight=1)

# Inicie a interface gráfica
root.mainloop()
