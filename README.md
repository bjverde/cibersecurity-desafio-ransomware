# Desafio de Cibersegurança: Simulação de Criptografia e Descriptografia com Python

> ⚠️ **Aviso Legal / Disclaimer**: Este projeto foi desenvolvido exclusivamente para fins educacionais e acadêmicos no contexto do Bootcamp de Cibersegurança da [DIO (Digital Innovation One)](https://www.dio.me/). Os scripts operam apenas sobre um arquivo de teste local específico e visam demonstrar conceitos de criptografia simétrica e conscientização sobre ameaças cibernéticas.

---

## 📌 Visão Geral do Projeto

Este repositório contém a implementação prática de uma simulação básica de criptografia e descriptografia de arquivos em ambiente local utilizando a linguagem **Python** e a biblioteca **pyaes**.

O objetivo é compreender na prática como funcionam os algoritmos criptográficos aplicados por softwares maliciosos (como ransomwares) e, a partir dessa compreensão, desenvolver estratégias defensivas de proteção, mitigação e resposta a incidentes.

---

## 📂 Estrutura do Repositório

```text
├── encrypter.py          # Script responsável por ler o arquivo, criptografar e renomear com nova extensão
├── decrypter.py          # Script responsável por reverter o processo utilizando a chave simétrica
├── teste.txt             # Arquivo de texto utilizado como amostra no teste local
└── README.md             # Documentação técnica do desafio
```

---

## 🧠 Conceitos Teóricos Abordados

### 1. Criptografia Simétrica (AES)
- Utiliza a **mesma chave** tanto para o processo de cifragem (criptografia) quanto para a decifragem (descriptografia).
- Algoritmo utilizado: **AES (Advanced Encryption Standard)**, padrão mundial de criptografia por blocos.

### 2. Modo de Operação CTR (Counter Mode)
- Transforma uma cifra de bloco em uma cifra de fluxo (*stream cipher*).
- Gera o próximo fluxo de chaves criptografando valores sucessivos de um contador.

### 3. Chave de Criptografia
- Nos scripts de exemplo, foi utilizada uma chave simétrica de 16 bytes (128 bits):
  ```python
  key = b"msantos2026sant"  # 16 caracteres / 128 bits
  ```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.8+** instalado.
- Biblioteca `pyaes` instalada no ambiente Python.

### 1. Instalação das Dependências
Instale o módulo `pyaes` via terminal:
```bash
pip install pyaes
```

### 2. Executando a Criptografia
Certifique-se de que o arquivo de exemplo `teste.txt` existe no diretório e execute:
```bash
python encrypter.py
```
**Resultado esperado:**
- O arquivo original `teste.txt` é removido.
- É gerado o arquivo criptografado `teste.txt.ransomwaretroll`.

### 3. Executando a Descriptografia (Restauração)
Para restaurar o arquivo original a partir dos dados criptografados, execute:
```bash
python decrypter.py
```
**Resultado esperado:**
- O arquivo criptografado `teste.txt.ransomwaretroll` é removido.
- O arquivo original `teste.txt` é restaurado com seu conteúdo legível original.

---

## 🛡️ Medidas de Segurança e Prevenção Defensiva

O estudo do funcionamento desse tipo de ameaça reforça a necessidade de implementação de controles de segurança defensiva em ambientes corporativos e pessoais:

1. **Estratégia de Backup (Regra 3-2-1):**
   - Manter 3 cópias dos dados importantes;
   - Em 2 tipos de mídias diferentes;
   - Sendo 1 cópia armazenada *offsite* ou imutável (fora do alcance da rede local).
2. **Princípio do Menor Privilégio (PoLP):**
   - Usuários e processos devem possuir apenas os privilégios estritamente necessários para suas funções.
3. **Soluções de EDR e Antivírus:**
   - Monitoramento comportamental para detectar alterações massivas de arquivos e criação de extensões suspeitas.
4. **Conscientização do Usuário:**
   - Treinamento contínuo contra ataques de *phishing* e engenharia social (principais vetores de entrega de malwares).

---

## 🎓 Conclusão

A prática permitiu consolidar os fundamentos do uso de criptografia simétrica com Python, evidenciando tanto a eficiência dos algoritmos modernos de criptografia quanto a criticidade de políticas preventivas para proteção e integridade de dados.
