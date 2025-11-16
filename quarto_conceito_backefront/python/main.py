import customtkinter as ctk
from funcoes.funs import inserir_usuario, listar_usuarios, buscar_usuario, deletar_usuario

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CRUDApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x600")
        self.title("CRUD SQLite - Go + Python")
        
        self.criar_widgets()
        self.atualizar_lista()
    
    def criar_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(main_frame, text="Gerenciador de Usuários", 
                              font=("Arial", 20, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Frame de entrada
        entrada_frame = ctk.CTkFrame(main_frame)
        entrada_frame.pack(fill="x", pady=10)
        
        # Nome
        ctk.CTkLabel(entrada_frame, text="Nome:").pack(pady=(10, 5))
        self.entrada_nome = ctk.CTkEntry(entrada_frame, width=300)
        self.entrada_nome.pack(pady=(0, 10))
        
        # Idade
        ctk.CTkLabel(entrada_frame, text="Idade:").pack(pady=(5, 5))
        self.entrada_idade = ctk.CTkEntry(entrada_frame, width=300)
        self.entrada_idade.pack(pady=(0, 10))
        
        # CPF
        ctk.CTkLabel(entrada_frame, text="CPF:").pack(pady=(5, 5))
        self.entrada_cpf = ctk.CTkEntry(entrada_frame, width=300)
        self.entrada_cpf.pack(pady=(0, 10))
        
        # Frame de botões
        botoes_frame = ctk.CTkFrame(main_frame)
        botoes_frame.pack(fill="x", pady=10)
        
        # Botões de ação
        ctk.CTkButton(botoes_frame, text="Inserir Usuário", 
                     command=self.botao_inserir, width=140).pack(side="left", padx=5, pady=10)
        ctk.CTkButton(botoes_frame, text="Deletar Selecionado", 
                     command=self.botao_deletar, width=140, 
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5, pady=10)
        ctk.CTkButton(botoes_frame, text="Atualizar Lista", 
                     command=self.atualizar_lista, width=140).pack(side="left", padx=5, pady=10)
        
        # Label de status
        self.label_status = ctk.CTkLabel(main_frame, text="", text_color="yellow")
        self.label_status.pack(pady=5)
        
        # Lista de usuários
        ctk.CTkLabel(main_frame, text="Usuários Cadastrados:", 
                    font=("Arial", 14, "bold")).pack(pady=(15, 5))
        
        self.lista_usuarios = ctk.CTkTextbox(main_frame, width=450, height=250)
        self.lista_usuarios.pack(pady=5)
    
    def botao_inserir(self):
        nome = self.entrada_nome.get().strip()
        idade_texto = self.entrada_idade.get().strip()
        cpf = self.entrada_cpf.get().strip()
        
        if not nome or not idade_texto or not cpf:
            self.label_status.configure(text="⚠️ Preencha todos os campos!", 
                                       text_color="orange")
            return
        
        try:
            idade = int(idade_texto)
            if idade < 0 or idade > 150:
                raise ValueError("Idade fora do intervalo válido")
        except ValueError as e:
            self.label_status.configure(text=f"⚠️ Idade inválida! Digite um número entre 0 e 150.", 
                                       text_color="orange")
            return
        
        try:
            resposta = inserir_usuario(nome, idade, cpf)
            self.label_status.configure(text=f"✓ Usuário '{nome}' inserido com sucesso!", 
                                       text_color="green")
            
            # Limpa os campos
            self.entrada_nome.delete(0, 'end')
            self.entrada_idade.delete(0, 'end')
            self.entrada_cpf.delete(0, 'end')
            
            self.atualizar_lista()
        except Exception as e:
            self.label_status.configure(text=f"✗ Erro ao inserir: {str(e)}", 
                                       text_color="red")
    
    def atualizar_lista(self):
        try:
            usuarios = listar_usuarios()
            self.lista_usuarios.delete("1.0", "end")
            
            if not usuarios or len(usuarios) == 0:
                self.lista_usuarios.insert("1.0", "Nenhum usuário cadastrado.\n\nClique em 'Inserir Usuário' para adicionar o primeiro registro.")
            else:
                texto = ""
                for u in usuarios:
                    # Tratamento seguro de campos que podem não existir
                    user_id = u.get('Id', u.get('id', '?'))
                    nome = u.get('Nome', u.get('nome', '?'))
                    idade = u.get('Idade', u.get('idade', '?'))
                    cpf = u.get('Cpf', u.get('cpf', '?'))
                    
                    texto += f"ID: {user_id} | {nome} | {idade} anos | CPF: {cpf}\n"
                    texto += "-" * 60 + "\n"
                self.lista_usuarios.insert("1.0", texto)
            
            self.label_status.configure(text=f"✓ Lista atualizada ({len(usuarios)} usuário(s))", 
                                       text_color="green")
        except Exception as e:
            self.label_status.configure(text=f"✗ Erro ao listar usuários: {str(e)}", 
                                       text_color="red")
            # Debug
            print(f"Erro detalhado: {e}")
    
    def botao_deletar(self):
        # Pega o texto selecionado
        try:
            texto_selecionado = self.lista_usuarios.selection_get()
            # Extrai o ID (assumindo formato "ID: X |...")
            if "ID:" in texto_selecionado:
                id_str = texto_selecionado.split("ID:")[1].split("|")[0].strip()
                usuario_id = int(id_str)
                
                resposta = deletar_usuario(usuario_id)
                self.label_status.configure(text=f"✓ Usuário ID {usuario_id} deletado!", 
                                           text_color="green")
                self.atualizar_lista()
            else:
                self.label_status.configure(text="⚠️ Selecione uma linha de usuário válida", 
                                           text_color="orange")
        except Exception as e:
            self.label_status.configure(text="⚠️ Selecione um usuário na lista para deletar", 
                                       text_color="orange")

# Inicia a aplicação
if __name__ == "__main__":
    app = CRUDApp()
    app.mainloop()