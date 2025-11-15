import subprocess
import json
import os
import sys

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

# Acessa os campos (use .get para evitar KeyError)
print(data.get("nome"), data.get("idade"), data.get("cpf"))
