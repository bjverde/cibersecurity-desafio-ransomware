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
    print("DECRYPTER - SIMULADOR DE DESCRIPTOGRAFIA".center(width))
    print("=" * width)
    print("Resumo: Restaura o arquivo criptografado (.ransomwaretroll)".center(width))
    print("revertendo a cifra com a chave simétrica AES-128.".center(width))
    print("=" * width)
    print()


show_header()

file_name = "teste.txt.ransomwaretroll"

print(f"[*] Localizando o arquivo criptografado: {file_name}...")
if not os.path.exists(file_name):
    print(f"[!] Erro: Arquivo '{file_name}' não encontrado no diretório.")
    exit()

# Abrir e ler o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave simétrica para descriptografia (deve ser idêntica à utilizada na criptografia)
key = b"msantos2026santo"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar os dados
print("[*] Descriptografando os dados com AES modo CTR...")
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)
print(f"[-] Arquivo criptografado '{file_name}' removido.")

# Criar e salvar o arquivo restaurado
new_file_name = "teste.txt"
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"[+] Sucesso! Arquivo restaurado: {new_file_name}")
print()
print()
print()