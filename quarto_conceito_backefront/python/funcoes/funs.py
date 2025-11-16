import subprocess
import json
import os
from pathlib import Path

# Obtém o diretório raiz do projeto (quarto_conceito_backfront)
# Assumindo que funs.py está em: quarto_conceito_backfront/python/funcoes/funs.py
SCRIPT_DIR = Path(__file__).parent  # funcoes/
PYTHON_DIR = SCRIPT_DIR.parent      # python/
PROJECT_DIR = PYTHON_DIR.parent     # quarto_conceito_backefront
CRUD_EXE = PROJECT_DIR / "crud.exe"

def verificar_crud_exe():
    """Verifica se o crud.exe existe e está acessível"""
    if not CRUD_EXE.exists():
        raise FileNotFoundError(
            f"O arquivo crud.exe não foi encontrado em: {CRUD_EXE}\n"
            f"Diretório do projeto: {PROJECT_DIR}\n"
            f"Certifique-se de que o crud.exe está na raiz do projeto."
        )
    return str(CRUD_EXE)

def executar_comando(args):
    """Executa o crud.exe com os argumentos fornecidos"""
    try:
        crud_path = verificar_crud_exe()
        result = subprocess.run(
            [crud_path] + args,
            capture_output=True,
            text=True,
            check=False,  # Não lança exceção automaticamente
            cwd=str(PROJECT_DIR)  # Define o diretório de trabalho
        )
        
        # Debug: imprime a saída bruta
        if result.returncode != 0:
            raise Exception(f"Erro ao executar crud.exe (código {result.returncode}): {result.stderr}")
        
        # Verifica se há saída
        if not result.stdout or result.stdout.strip() == "":
            # Retorna lista vazia para comando 'listar' sem dados
            if "listar" in args:
                return []
            return None
        
        # Tenta fazer o parse do JSON
        try:
            data = json.loads(result.stdout)
            return data
        except json.JSONDecodeError as e:
            # Se não for JSON válido, mostra o que foi retornado
            raise Exception(
                f"Resposta não é JSON válido.\n"
                f"Saída: {result.stdout[:200]}\n"
                f"Erro: {str(e)}"
            )
            
    except FileNotFoundError as e:
        raise Exception(f"Erro de caminho: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro: {str(e)}")

def inserir_usuario(nome, idade, cpf):
    """Insere um novo usuário no banco de dados"""
    resultado = executar_comando(["inserir", nome, str(idade), cpf])
    return resultado if resultado else {"status": "ok"}

def listar_usuarios():
    """Lista todos os usuários do banco de dados"""
    resultado = executar_comando(["listar"])
    # Garante que sempre retorna uma lista
    if resultado is None:
        return []
    if isinstance(resultado, list):
        return resultado
    # Se retornar um objeto com lista dentro
    if isinstance(resultado, dict) and "usuarios" in resultado:
        return resultado["usuarios"]
    return []

def buscar_usuario(id):
    """Busca um usuário específico por ID"""
    return executar_comando(["buscar", str(id)])

def deletar_usuario(id):
    """Deleta um usuário específico por ID"""
    resultado = executar_comando(["deletar", str(id)])
    return resultado if resultado else {"status": "ok"}

# Teste de diagnóstico (útil para debug)
if __name__ == "__main__":
    print(f"Diretório do script: {SCRIPT_DIR}")
    print(f"Diretório Python: {PYTHON_DIR}")
    print(f"Diretório do projeto: {PROJECT_DIR}")
    print(f"Caminho do crud.exe: {CRUD_EXE}")
    print(f"crud.exe existe? {CRUD_EXE.exists()}")
    
    if CRUD_EXE.exists():
        print("\n✓ crud.exe encontrado!")
        
        # Teste de listagem
        try:
            print("\nTestando listagem...")
            usuarios = listar_usuarios()
            print(f"✓ Listagem OK! {len(usuarios)} usuário(s) no banco.")
            if usuarios:
                print("\nPrimeiros usuários:")
                for u in usuarios[:3]:
                    print(f"  - ID: {u.get('Id', '?')}, Nome: {u.get('Nome', '?')}")
        except Exception as e:
            print(f"✗ Erro ao listar: {e}")
        
        # Teste de inserção
        try:
            print("\nTestando inserção...")
            resultado = inserir_usuario("Teste Python", 25, "123.456.789-00")
            print(f"✓ Inserção OK! Resultado: {resultado}")
        except Exception as e:
            print(f"✗ Erro ao inserir: {e}")
            
        # Lista novamente
        try:
            usuarios = listar_usuarios()
            print(f"\n✓ Após inserção: {len(usuarios)} usuário(s) no banco.")
        except Exception as e:
            print(f"✗ Erro ao listar novamente: {e}")
    else:
        print("\n✗ crud.exe NÃO encontrado!")
        print(f"Procure o arquivo em: {CRUD_EXE}")