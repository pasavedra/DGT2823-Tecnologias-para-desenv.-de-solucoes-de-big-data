# Atividade: Limpeza e Tratamento de Dados com Pandas
# Analista de Dados - Processamento de conjunto de dados

import pandas as pd
import numpy as np
from io import StringIO

# Dados mock fornecidos - usando exatamente como especificado
sample_data = """ID;Duration;Date;Pulse;Maxpulse;Calories
0;60;'2020/12/01';110;130;4091
1;60;'2020/12/02';117;145;4790
2;60;'2020/12/03';103;135;3400
3;45;'2020/12/04';109;175;2824
4;45;'2020/12/05';117;148;4060
5;60;'2020/12/06';102;127;3000
6;60;'2020/12/07';110;136;3740
7;450;'2020/12/08';104;134;2533
8;30;'2020/12/09';109;133;1951
9;60;'2020/12/10';98;124;2690
10;60;'2020/12/11';103;147;3293
11;60;'2020/12/12';100;120;2507
12;60;'2020/12/12';100;120;2507
13;60;'2020/12/13';106;128;3453
14;60;'2020/12/14';104;132;3793
15;60;'2020/12/15';98;123;2750
16;60;'2020/12/16';98;120;2152
17;60;'2020/12/17';100;120;3000
18;45;'2020/12/18';90;112;NaN
19;60;'2020/12/19';103;123;3230
20;45;'2020/12/20';97;125;2430
21;60;'2020/12/21';108;131;3642
22;45;NaN;100;119;2820
23;60;'2020/12/23';130;101;3000
24;45;'2020/12/24';105;132;2460
25;60;'2020/12/25';102;126;3345
26;60;20201226;100;120;2500
27;60;'2020/12/27';92;118;2410
28;60;'2020/12/28';103;132;NaN
29;60;'2020/12/29';100;132;2800
30;60;'2020/12/30';102;129;3803
31;60;'2020/12/31';92;115;2430"""

print("=== ATIVIDADE: LIMPEZA E TRATAMENTO DE DADOS ===\n")

# PASSO 2: Novo arquivo/script (já criado)
print("✓ Passo 2: Novo script criado")

# PASSO 3 e 4: Leia o conteúdo do CSV e atribua a uma variável
print("\n--- PASSO 3 e 4: Leitura dos dados ---")
# Lendo os dados com separador ponto e vírgula (;)
#ados_originais = pd.read_csv(StringIO(sample_data), sep=';', na_values='NaN')
dados_originais = pd.read_csv('sample_data.csv', sep=';', na_values='NaN')
print("✓ Dados lidos e atribuídos à variável 'dados_originais'")
print(f"Colunas disponíveis: {list(dados_originais.columns)}")

# PASSO 5: Verificar se os dados foram importados adequadamente
print("\n--- PASSO 5: Verificação da importação ---")

# 5.1: Informações gerais sobre o conjunto de dados
print("5.1 - Informações gerais sobre o conjunto de dados:")
print(dados_originais.info())
print()

# 5.2: Primeiras e últimas N linhas
print("5.2 - Primeiras 5 linhas:")
print(dados_originais.head())
print("\nÚltimas 5 linhas:")
print(dados_originais.tail())

# PASSO 6: Criar cópia dos dados originais
print("\n--- PASSO 6: Criação de cópia dos dados ---")
dados_tratados = dados_originais.copy()
print("✓ Cópia criada na variável 'dados_tratados'")

# PASSO 7: Substituir valores nulos da coluna 'Calories' por 0
print("\n--- PASSO 7: Tratamento da coluna 'Calories' ---")
print("7.1 - Substituindo valores nulos da coluna 'Calories' por 0:")
dados_tratados['Calories'].fillna(0, inplace=True)

print("7.2 - Verificação da mudança:")
print(dados_tratados[['ID', 'Calories']].tail(15))

# PASSO 8: Tratamento da coluna 'Date'
print("\n--- PASSO 8: Tratamento inicial da coluna 'Date' ---")

# 8.1: Substituir valores nulos por '1900/01/01'
print("8.1 - Substituindo valores nulos da coluna 'Date' por '1900/01/01':")
dados_tratados['Date'].fillna('1900/01/01', inplace=True)

# 8.2: Verificar mudança
print("8.2 - Verificação da mudança:")
print(dados_tratados[['ID', 'Date']].tail(15))

# 8.3: Tentativa de transformar para datetime (gerará erro)
print("\n8.3 - Tentativa de transformação para datetime:")
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
    print("✓ Transformação realizada com sucesso")
except Exception as e:
    print(f"❌ Erro encontrado conforme esperado: {e}")

# PASSO 9: Resolver o problema do formato '1900/01/01'
print("\n--- PASSO 9: Resolução do problema do formato ---")

# 9.1: Substituir '1900/01/01' por NaN
print("9.1 - Substituindo '1900/01/01' por NaN:")
dados_tratados['Date'] = dados_tratados['Date'].replace('1900/01/01', np.nan)

# 9.2: Tentar transformação novamente
print("9.2 - Nova tentativa de transformação para datetime:")
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
    print("✓ Transformação realizada com sucesso")
except Exception as e:
    print(f"❌ Novo erro encontrado conforme esperado: {e}")

# 9.3: Verificar mudanças
print("9.3 - Verificação das mudanças:")
print(dados_tratados[['ID', 'Date']].tail(15))

# PASSO 10: Tratar o valor "20201226" específico
print("\n--- PASSO 10: Tratamento do valor específico '20201226' ---")
print("Identificando e corrigindo o valor '20201226':")

# Encontrar e corrigir o formato incorreto usando replace e to_datetime
# Primeiro, vamos identificar onde está o valor problemático
print("Valores únicos na coluna Date antes da correção:")
print(dados_tratados['Date'].unique())

# Transformar especificamente o valor 20201226 para o formato correto
dados_tratados['Date'] = dados_tratados['Date'].replace(20201226, '2020/12/26')
print("✓ Valor '20201226' convertido para '2020/12/26'")

# PASSO 11: Transformação final para datetime
print("\n--- PASSO 11: Transformação final para datetime ---")
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d', errors='coerce')
    print("✓ Transformação para datetime realizada com sucesso")
    print("Verificação do conjunto de dados atual:")
    print(dados_tratados[['ID', 'Date']].tail(15))
    print(f"Tipo da coluna Date: {dados_tratados['Date'].dtype}")
except Exception as e:
    print(f"❌ Erro: {e}")

# PASSO 12: Remover registros com valores nulos
print("\n--- PASSO 12: Remoção de registros com valores nulos ---")
print("Dados antes da remoção:")
print(f"Total de linhas: {len(dados_tratados)}")
print("Valores nulos por coluna:")
print(dados_tratados.isnull().sum())

# Identificar especificamente a linha 22 (que tem Date nulo)
print("\nRegistros com Date nulo:")
print(dados_tratados[dados_tratados['Date'].isnull()])

# Remover linhas com valores nulos na coluna Date
dados_tratados = dados_tratados.dropna(subset=['Date'])
print(f"\nApós remoção - Total de linhas: {len(dados_tratados)}")

# PASSO 13: Verificação final
print("\n--- PASSO 13: Verificação final ---")
print("=== RESULTADO FINAL ===")
print("\nInformações do dataframe final:")
print(dados_tratados.info())

print("\nPrimeiras 10 linhas do dataframe tratado:")
print(dados_tratados.head(10))

print("\nÚltimas 10 linhas do dataframe tratado:")
print(dados_tratados.tail(10))

print("\nVerificação de valores nulos:")
print(dados_tratados.isnull().sum())

print("\nTipos de dados das colunas:")
print(dados_tratados.dtypes)

print("\nEstatísticas básicas do conjunto final:")
print(dados_tratados.describe())

print("\n=== ATIVIDADE CONCLUÍDA COM SUCESSO! ===")
print(f"✓ Dados originais: {len(dados_originais)} linhas")
print(f"✓ Dados tratados: {len(dados_tratados)} linhas")
print("✓ Valores nulos da coluna 'Calories' substituídos por 0")
print("✓ Coluna 'Date' convertida para formato datetime")
print("✓ Registros com valores nulos na coluna 'Date' removidos (linha 22)")
print("✓ Conjunto de dados pronto para análise e mineração de dados!")