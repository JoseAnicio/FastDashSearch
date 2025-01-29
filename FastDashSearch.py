from guardacaminho import guardacaminho
import pandas as pd
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkImage
from PIL import Image

def search_customer():
    # Função para busca de clientes (a ser implementada)
    pass

def open_workspace():
    # Função para abrir o workspace (a ser implementada)
    pass

def open_application():
    # Função para abrir o aplicativo (a ser implementada)
    pass

def pesquisar():
    try:
        # Lendo o arquivo CSV
        file = pd.read_csv(guardacaminho, delimiter=',', encoding="utf8")
        print(guardacaminho)

        search_query = SearchString.get().lower()  # Obtém o texto digitado e converte para minúsculas
        
        # Verifica se a pesquisa está vazia
        if not search_query:
            SearchResultBar.configure(text="Digite algo para pesquisar.", text_color="yellow")
            return

        # Procura a string em todas as colunas
        resultado = file[file.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        # Atualiza a barra de resultados
        if not resultado.empty:
            resultados_texto = resultado.to_string(index=False)  # Converte o DataFrame em string sem o índice
            SearchResultBar.configure(text=f"Resultados encontrados:\n{resultados_texto}", text_color="green")
        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="red")
    
    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="red")

def resultado_pesquisa(x, resultado):
    if x:
        SearchResultBar.configure(text=f"Resultado encontrado: {', '.join(map(str, resultado))}", text_color="green")
    else:
        SearchResultBar.configure(text="Resultado não encontrado", text_color="red")

# Janela principal
root = CTk()
root.title("Fast Dash Search")
root.geometry("854x480")
root.configure(fg_color="gray20")  # Cor de fundo

#barra superior
top_bar = CTkFrame(root, fg_color="#212671")
top_bar.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.110)

# Contêiner para os botões principais
button_container = CTkFrame(root, fg_color="#212671")
button_container.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)


# Botões principais
button1 = CTkButton(button_container, text="DASHS\nÚNICOS", fg_color="#101524", hover_color="#202631", text_color="white", command=open_workspace, font= ('Gill Sans', 13, 'bold'))
button1.place(relx=0.004, rely=0.1, relwidth=0.14, relheight=1)

button2 = CTkButton(button_container, text="WORKSPACE", fg_color="#101524", hover_color="#202631", text_color="white", command=open_application, font= ('Gill Sans', 13, 'bold'))
button2.place(relx=0.145, rely=0.1, relwidth=0.14, relheight=1)

button3 = CTkButton(button_container, text="APLICATIVO", fg_color="#101524", hover_color="#202631", text_color="white", command=open_application, font= ('Gill Sans', 13, 'bold'))
button3.place(relx=0.287, rely=0.1, relwidth=0.14, relheight=1)

# Barra de pesquisa
SearchString = CTkEntry(root, placeholder_text="Pesquisar...", width=250, height=40, fg_color="white", text_color="black")
SearchString.place(relx=0.64, rely=0.01)

# Botão de pesquisa com ícone
lupaimage = CTkImage(light_image=Image.open("C:/Users/Anício/OneDrive/Área de Trabalho/lupa1.png"), size=(30, 30))
SearchButton = CTkButton(root, text="", image=lupaimage, width=40, height=40, fg_color="#212671", hover_color="gray30", command=pesquisar, border_color="#212671")
SearchButton.place(relx=0.94, rely=0.01)

# Barra de resultados
SearchResultBar = CTkLabel(root, text="", text_color="white", font=("Arial", 14))
SearchResultBar.place(relx=0.05, rely=0.25)


# Executa a interface
root.mainloop()
