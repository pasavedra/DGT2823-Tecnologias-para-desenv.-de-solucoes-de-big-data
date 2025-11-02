# Microatividade 1: Descrever como ler um arquivo CSV usando a biblioteca Pandas
# Analista de Dados - Leitura de dados externos

# PROCEDIMENTO 2.1: Importe a biblioteca pandas
import pandas as pd

print("=== MICROATIVIDADE 1: LEITURA DE ARQUIVO CSV COM PANDAS ===\n")
print("✓ Passo 2.1: Biblioteca pandas importada com sucesso")

# PROCEDIMENTO 2.2: Cria uma variável
dados_lidos = None
print("✓ Passo 2.2: Variável 'dados_lidos' criada")

# PROCEDIMENTO 2.3 e 2.4: Leia o conteúdo do arquivo CSV e atribua à variável
print("\n--- LEITURA DO ARQUIVO CSV ---")

# DEMONSTRAÇÃO COM ARQUIVO REAL:
# Para ler um arquivo CSV real localizado na pasta raiz do projeto, use:
dados_lidos = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')
print("✓ Passo 2.3 e 2.4: Arquivo CSV lido e dados atribuídos à variável 'dados_lidos'")

# Informações sobre os parâmetros utilizados
print("\n--- PARÂMETROS UTILIZADOS NA LEITURA ---")
print("• sep=';'        → Define o separador de colunas como ponto e vírgula")
print("• engine='python' → Especifica o motor de análise Python")
print("• encoding='utf-8' → Define a codificação de caracteres")

# PROCEDIMENTO 2.5: Imprima/exiba em tela os dados da variável
print("\n--- PASSO 2.5: EXIBIÇÃO DOS DADOS LIDOS ---")

print("=== DADOS COMPLETOS DO ARQUIVO CSV ===")
print(dados_lidos)

print("\n=== INFORMAÇÕES ADICIONAIS SOBRE OS DADOS ===")
print(f"Formato do DataFrame: {dados_lidos.shape}")
print(f"Colunas: {list(dados_lidos.columns)}")
print(f"Tipos de dados:")
print(dados_lidos.dtypes)

print("\n=== PRIMEIRAS 5 LINHAS ===")
print(dados_lidos.head())

print("\n=== ÚLTIMAS 5 LINHAS ===")
print(dados_lidos.tail())

print("\n=== ESTATÍSTICAS BÁSICAS ===")
print(dados_lidos.describe())

print("\n=== MICROATIVIDADE 1 CONCLUÍDA COM SUCESSO! ===")
print("✅ Biblioteca pandas importada")
print("✅ Variável criada")
print("✅ Arquivo CSV lido com parâmetros especificados")
print("✅ Dados atribuídos à variável")
print("✅ Conteúdo exibido em tela")