from guardacaminho import guardacaminho, guardalupa
import pandas as pd
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkImage, CTkScrollableFrame
import tkinter as tk
from tkinter import ttk
from PIL import Image

file = pd.read_csv(guardacaminho, delimiter=',', encoding="utf8")
file = file.sort_values(by=['Cliente'])
coluna_tipodelink = file.columns[2]
coluna_clientes = file.iloc[:,0].unique()
coluna_clientes = coluna_clientes.tolist()

def copiar_celula(event, tree=None):
    selected_item = tree.selection()  # Obtém a linha selecionada

    if selected_item:
        col_index = tree.identify_column(event.x)  # Identifica a coluna clicada
        col_index = int(col_index[1:]) - 1  # Converte "#1", "#2" para índice 0, 1, etc.
        item_values = tree.item(selected_item, "values")  # Pega os valores da linha

        if col_index < len(item_values):  # Evita erro se índice for inválido
            valor_copiado = item_values[col_index]
            root.clipboard_clear()  # Limpa a área de transferência
            root.clipboard_append(valor_copiado)  # Copia o valor
            root.update()  # Atualiza a área de transferência
            SearchResultBar.configure(text="Valor copiado!", text_color="#fffffe", font=("Gill Sans", 14), fg_color="#272343")
            root.after(1000, limpar_search_result)

def limpar_search_result():
    SearchResultBar.configure(text="", text_color="white", fg_color="#fffffe")


def pesquisarIndividual():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink] == "Individual"]

        if filtro_cliente:
            file_filtred = file_filtred[file_filtred.iloc[:, 0] == filtro_cliente]

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        # Limpa os widgets dentro do tree_frame
        for widget in tree_frame.winfo_children():
            widget.destroy()

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="#272343", font=("Gill Sans", 14))

            # Criando o container da tabela
            tree_container = CTkFrame(tree_frame)
            tree_container.pack(fill="both", expand=True)

            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_container, columns=columnst, show="headings", style="Treeview")
            tree.pack(side="left", fill="both", expand=True)

            # Criando uma única Scrollbar funcional
            scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")

            # Vinculando a Scrollbar corretamente
            tree.configure(yscrollcommand=scrollbar.set)

            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=100)  # Ajustei o tamanho para melhor visualização

            # Adicionando dados na tabela
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))

            # Definindo atalho de copiar
            tree.bind("<Double-Button-1>", lambda event: copiar_celula(event, tree))


        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="#272343", font=("Gill Sans", 14))

    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="#272343", font=("Gill Sans", 14))

    root.mainloop()

def pesquisarAplicativo():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink]=="Aplicativo"]

        if filtro_cliente:
            file_filtred = file_filtred[file_filtred.iloc[:, 0] == filtro_cliente]

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        # Limpa os widgets dentro do tree_frame
        for widget in tree_frame.winfo_children():
            widget.destroy()

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="#272343", font=("Gill Sans", 14))

            # Criando o container da tabela
            tree_container = CTkFrame(tree_frame)
            tree_container.pack(fill="both", expand=True)

            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_container, columns=columnst, show="headings", style="Treeview")
            tree.pack(side="left", fill="both", expand=True)

            # Criando uma única Scrollbar funcional
            scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")

            # Vinculando a Scrollbar corretamente
            tree.configure(yscrollcommand=scrollbar.set)

            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=100)  # Ajustei o tamanho para melhor visualização

            # Adicionando dados na tabela
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))

            # Definindo atalho de copiar
            tree.bind("<Double-Button-1>", lambda event: copiar_celula(event, tree))



        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="#272343")

    except Exception as e:
        SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="#272343", font=("Gill Sans", 14))
    
    root.mainloop()

def pesquisarWorkspace():
    try:
        search_query = SearchString.get().lower()

        file_filtred = file[file[coluna_tipodelink]=="Workspace"]

        if filtro_cliente:
            file_filtred = file_filtred[file_filtred.iloc[:, 0] == filtro_cliente]

        resultado = file_filtred[file_filtred.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

        # Limpa os widgets dentro do tree_frame
        for widget in tree_frame.winfo_children():
            widget.destroy()

        if not resultado.empty:
            SearchResultBar.configure(text="Resultados encontrados:", text_color="#272343", font=("Gill Sans", 14))
            # Criando o container da tabela
            tree_container = CTkFrame(tree_frame)
            tree_container.pack(fill="both", expand=True)

            # Criando a Treeview
            columnst = list(resultado.columns)
            tree = ttk.Treeview(tree_container, columns=columnst, show="headings", style="Treeview")
            tree.pack(side="left", fill="both", expand=True)

            # Criando uma única Scrollbar funcional
            scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")

            # Vinculando a Scrollbar corretamente
            tree.configure(yscrollcommand=scrollbar.set)

            # Definição dos cabeçalhos
            for col in columnst:
                tree.heading(col, text=col, anchor="w")
                tree.column(col, anchor="w", width=100)  # Ajustei o tamanho para melhor visualização

            # Adicionando dados na tabela
            for _, row in resultado.iterrows():
                tree.insert("", "end", values=list(row))

            # Definindo atalho de copiar
            tree.bind("<Double-Button-1>", lambda event: copiar_celula(event, tree))


        else:
            SearchResultBar.configure(text="Nenhum resultado encontrado.", text_color="#272343", font=("Gill Sans", 14))

    except Exception as e:
     SearchResultBar.configure(text=f"Erro: {str(e)}", text_color="#272343")
    
    root.mainloop()

def resultado_pesquisa(x, resultado):
    if x:
        SearchResultBar.configure(text=f"Resultado encontrado: {', '.join(map(str, resultado))}", text_color="#272343")
    else:
        SearchResultBar.configure(text="Resultado não encontrado", text_color="#272343")

#Faz a filtragem do tipo de ambiente
def update_search(func):
    global x
    x = func
    func()


def atualizar_filtro(event):
    global filtro_cliente

    filtro_cliente = filtro_frame.get()

def limpar_filtro():
    filtro_frame.set("")  # Define um valor vazio no Combobox
    global filtro_cliente
    filtro_cliente = None  # Remove o filtro aplicado
    update_search(x)
    

# Janela principal
root = CTk()
root.title("Fast Dash Search")
root.geometry("854x480")
root.configure(fg_color="#fffffe")  # Cor de fundo
root.resizable(False, False)

#barra superior
top_bar = CTkFrame(root, fg_color="#272343", corner_radius=0)
top_bar.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.110)

# Contêiner para os botões principais
button_container = CTkFrame(root, fg_color="#272343", corner_radius=0)
button_container.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)

x = pesquisarAplicativo

# Botões principais
button1 = CTkButton(button_container, text="DASHS\nINDIVIDUAIS", fg_color="#ffd803", hover_color="#d18d26", text_color="#001e1d", command=lambda: update_search(pesquisarIndividual), font= ('Gill Sans', 13, 'bold'))
button1.place(relx=0.015, rely=0.1, relwidth=0.133, relheight=1)

button2 = CTkButton(button_container, text="WORKSPACE", fg_color="#ffd803", hover_color="#d18d26", text_color="#001e1d",  command=lambda: update_search(pesquisarWorkspace), font= ('Gill Sans', 13, 'bold'))
button2.place(relx=0.159, rely=0.1, relwidth=0.133, relheight=1)

button3 = CTkButton(button_container, text="APLICATIVO", fg_color="#ffd803", hover_color="#d18d26", text_color="#001e1d",command=lambda: update_search(pesquisarAplicativo), font= ('Gill Sans', 13, 'bold'))
button3.place(relx=0.303, rely=0.1, relwidth=0.133, relheight=1)

# Barra de pesquisa
SearchString = CTkEntry(root, placeholder_text="Pesquisar...", 
                        width=200, 
                        height=44, 
                        fg_color="#fffffe", 
                        text_color="black", 
                        border_color="#272343", 
                        corner_radius=0)
SearchString.place(relx=0.70, rely=0.007)
SearchString.bind('<Return>', lambda event: update_search(x))


# Botão de pesquisa com ícone
lupaimage = CTkImage(light_image=Image.open(guardalupa), size=(20, 20))
SearchButton = CTkButton(root, text="", 
                         image=lupaimage, 
                         width=40, height=40, 
                         fg_color="#ffd803", 
                         hover_color="#ffd803", 
                         command=lambda: update_search(x), 
                         border_color="#212671", 
                         font=("Gill Sans", 14), 
                         corner_radius=0)
SearchButton.place(relx=0.94, rely=0.01)

# Barra de resultados
SearchResultBar = CTkLabel(root, text="", text_color="white", font=("Gill Sans", 14), fg_color="#fffffe", corner_radius=0)
SearchResultBar.place(relx=0.05, rely=0.13)

filtro_frame = ttk.Combobox(root, background="#fffffe", foreground="#2d334a", font=("Gill Sans", 10), width=12, height=40)
filtro_frame['values'] = coluna_clientes
filtro_cliente=filtro_frame.set("")
filtro_frame.place(relx=0.5, rely=0.03)
filtro_frame.bind("<<ComboboxSelected>>", atualizar_filtro)

limpar_filtro_frame = CTkButton(root, text="LIMPAR\nCLIENTE", 
                                command=limpar_filtro,
                                fg_color="#332c61", 
                                hover_color="#1e1a3d", 
                                text_color="white", 
                                font= ('Gill Sans', 10, 'bold'),
                                width=40,
                                height=40,
                                border_width=1,
                                border_color="white",
                                corner_radius=0)

limpar_filtro_frame.place(relx=0.635, rely=0.01)

# Frame para exibição da tabela
tree_frame = CTkFrame(root, fg_color="#fffffe")
# Configuração Global de Estilo para a Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#fffffe",
                foreground="#2d334a",
                rowheight=25,
                fieldbackground="#fffffe", 
                font=("Arial", 12))
style.configure("Treeview.Heading", background="#272343", foreground="white", font=('Gill Sans', 12, "bold"), fg_color="#fffffe")
style.map("Treeview", background=[("selected", "#1f6aa5")])
tree_frame.place(relx=0.05, rely=0.20, relwidth=0.9, relheight=0.7)

# Executa a interface
root.mainloop(update_search(x))