import os
import pyaes

file_name = "teste.txt.ransomwaretroll"

print(f"[*] Localizando o arquivo criptografado: {file_name}...")
if not os.path.exists(file_name):
    print(f"[!] Erro: Arquivo '{file_name}' não encontrado no diretório.")
    exit()

# Abrir e ler o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave simétrica para descriptografia (deve ser idêntica à utilizada na criptografia)
key = b"testeransomwares"
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
