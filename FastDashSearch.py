from guardacaminho import guardacaminho, guardalupa
import pandas as pd
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkImage
from tkinter import ttk
from PIL import Image
from tabulate import *

file = pd.read_csv(guardacaminho, delimiter=',', encoding="utf8")
coluna_tipodelink = file.columns[2]

def search_customer():
    # Função para busca de clientes (a ser implementada)
    pass

def pesquisarIndividual():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink]=="Individual"]
       
        if not search_query:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="white", anchor="center")
            return

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="white")
            
            global tree_frame
            for widget in tree_frame.winfo_children():  # Limpa o frame antes de adicionar novo conteúdo
                widget.destroy()
            
            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_frame, columns=columnst, show="headings", style="Treeview")
            tree.pack(fill="both", expand=True)
            
            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=30)
                   
            # Adicionando dados
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))
            
            # Adicionando barra de rolagem
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")
            tree.configure(yscroll=scrollbar.set)
        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="red")
    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="red")

    root.mainloop()

def pesquisarAplicativo():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink]=="Aplicativo"]

        if not search_query:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="white", anchor="center")
            return

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="white")
            
            global tree_frame
            for widget in tree_frame.winfo_children():  # Limpa o frame antes de adicionar novo conteúdo
                widget.destroy()
            
            
            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_frame, columns=columnst, show="headings", style="Treeview")
            tree.pack(fill="both", expand=True)
            
            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=30)
                   
            # Adicionando dados
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))
            
            # Adicionando barra de rolagem
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="red")
    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="red")
    
    root.mainloop()

def pesquisarWorkspace():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink]=="Workspace"]

        if not search_query:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="white", anchor="center")
            return

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="white")
            
            global tree_frame
            for widget in tree_frame.winfo_children():  # Limpa o frame antes de adicionar novo conteúdo
                widget.destroy()
        
            
            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_frame, columns=columnst, show="headings", style="Treeview")
            tree.pack(fill="both", expand=True)
            
            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=30)
                   
            # Adicionando dados
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))
            
            # Adicionando barra de rolagem
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="red")
    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="red")
    
    root.mainloop()

def resultado_pesquisa(x, resultado):
    if x:
        SearchResultBar.configure(text=f"Resultado encontrado: {', '.join(map(str, resultado))}", text_color="green")
    else:
        SearchResultBar.configure(text="Resultado não encontrado", text_color="red")

# Janela principal
def update_search(func):
    global x
    x = func
    func()

root = CTk()
root.title("Fast Dash Search")
root.geometry("854x480")
root.configure(fg_color="gray20")  # Cor de fundo
root.resizable(None)

#barra superior
top_bar = CTkFrame(root, fg_color="#212671")
top_bar.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.110)

# Contêiner para os botões principais
button_container = CTkFrame(root, fg_color="#212671")
button_container.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)



# Botões principais
button1 = CTkButton(button_container, text="DASHS\nINDIVIDUAIS", fg_color="#101524", hover_color="#202631", text_color="white", command=lambda: update_search(pesquisarIndividual), font= ('Gill Sans', 13, 'bold'))
button1.place(relx=0.004, rely=0.1, relwidth=0.14, relheight=1)

button2 = CTkButton(button_container, text="WORKSPACE", fg_color="#101524", hover_color="#202631", text_color="white",  command=lambda: update_search(pesquisarWorkspace), font= ('Gill Sans', 13, 'bold'))
button2.place(relx=0.145, rely=0.1, relwidth=0.14, relheight=1)

button3 = CTkButton(button_container, text="APLICATIVO", fg_color="#101524", hover_color="#202631", text_color="white",command=lambda: update_search(pesquisarAplicativo), font= ('Gill Sans', 13, 'bold'))
button3.place(relx=0.287, rely=0.1, relwidth=0.14, relheight=1)

# Barra de pesquisa
SearchString = CTkEntry(root, placeholder_text="Pesquisar...", width=250, height=40, fg_color="white", text_color="black")
SearchString.place(relx=0.64, rely=0.01)

# Botão de pesquisa com ícone
lupaimage = CTkImage(light_image=Image.open(guardalupa), size=(30, 30))
SearchButton = CTkButton(root, text="", image=lupaimage, width=40, height=40, fg_color="#212671", hover_color="gray30", command=pesquisarIndividual, border_color="#212671")
SearchButton.place(relx=0.94, rely=0.01)

# Barra de resultados
SearchResultBar = CTkLabel(root, text="", text_color="white", font=("Arial", 14))
SearchResultBar.place(relx=0.05, rely=0.2)

# Frame para exibição da tabela
tree_frame = CTkFrame(root)
# Configuração Global de Estilo para a Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#282c34",
                foreground="white",
                rowheight=25, 
                fieldbackground="#282c34", 
                font=("Arial", 12))
style.configure("Treeview.Heading", background="#3a3f4b", foreground="white", font=("Arial", 12, "bold"))
style.map("Treeview", background=[("selected", "#1f6aa5")])
tree_frame.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7)


# Executa a interface
root.mainloop()