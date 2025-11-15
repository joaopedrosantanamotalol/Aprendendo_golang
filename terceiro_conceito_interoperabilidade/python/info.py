import subprocess
import json
import os
import sys
from customtkinter import *


# Caminho do script Python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Escolha qual arquivo Go executar:
# Opção A: executar main.go na raiz do projeto
go_file = os.path.normpath(os.path.join(script_dir, "..", "main.go"))

# Executa o Go
proc = subprocess.run(["go", "run", go_file], capture_output=True, text=True)

if proc.returncode != 0:
    print("Erro ao executar o programa Go:", file=sys.stderr)
    print(proc.stderr, file=sys.stderr)
    sys.exit(proc.returncode)

# Tenta decodificar JSON da saída do Go
try:
    data = json.loads(proc.stdout)
except json.JSONDecodeError:
    print("Saída do Go não é JSON válido. Saída:", file=sys.stderr)
    print(proc.stdout, file=sys.stderr)
    sys.exit(1)


user_name = data.get("nome")
user_idade = data.get("idade")
user_cpf = data.get("cpf")

class tela(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x500")
        self.title("Telinha")
        self.configure(fg_color="black")

        titulo = CTkLabel(self, text=user_name, font=("Arial", 20), text_color="green")
        titulo.place(relx=0.5, rely=0.1, anchor=CENTER)

        nome_us = CTkLabel(self, text=f"Nome: {user_name}", font=("Arial", 15), text_color="green")
        nome_us.place(relx=0.5, rely=0.2, anchor=CENTER)

        idade_us = CTkLabel(self, text=f"Idade: {user_idade}", font=("Arial", 15), text_color="green")
        idade_us.place(relx=0.5, rely=0.3, anchor=CENTER)

        cpf_us = CTkLabel(self, text=f"CPF: {user_cpf}", font=("Arial", 15), text_color="green")
        cpf_us.place(relx=0.5, rely=0.4, anchor=CENTER)

if __name__ == "__main__":
    app = tela()
    app.mainloop()