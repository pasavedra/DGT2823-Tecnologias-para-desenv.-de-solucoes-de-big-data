import pandas as pd
from io import StringIO

# Dados fornecidos para o CSV (mesmo das microatividades anteriores)
dados_csv = """ID;Duration;Date;Pulse;Maxpulse;Calories
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

# 1. Criar o DataFrame a partir dos dados CSV
df = pd.read_csv(StringIO(dados_csv), delimiter=';')

print("ANÁLISE COMPLETA DO CONJUNTO DE DADOS")
print("=" * 70)

# 2.1. Informações gerais sobre o conjunto de dados
print("\n1. INFORMAÇÕES GERAIS DO DATASET (método .info()):")
print("-" * 50)
df.info()

print("\n" + "=" * 70)

# 2.2. Extraindo informações específicas
print("2. INFORMAÇÕES DETALHADAS EXTRAÍDAS:")
print("-" * 50)

# 2.2.1. Total de linhas
total_linhas = len(df)
print(f"Total de linhas: {total_linhas}")

# 2.2.2. Total de colunas
total_colunas = len(df.columns)
print(f"Total de colunas: {total_colunas}")

# 2.2.3. Quantidade de dados nulos
print(f"\n Dados nulos por coluna:")
dados_nulos = df.isnull().sum()
for coluna, qtd_nulos in dados_nulos.items():
    if qtd_nulos > 0:
        print(f"   • {coluna}: {qtd_nulos} valores nulos")
    else:
        print(f"   • {coluna}: 0 valores nulos")

total_nulos = df.isnull().sum().sum()
print(f"Total de valores nulos no dataset: {total_nulos}")

# 2.2.4. Tipo de dado de cada coluna
print(f"\n Tipos de dados por coluna:")
tipos_dados = df.dtypes
for coluna, tipo in tipos_dados.items():
    print(f"   • {coluna}: {tipo}")

# 2.2.5. Quantidade de memória utilizada
print(f"\n Uso de memória:")
memoria_info = df.memory_usage(deep=True)
for coluna, memoria in memoria_info.items():
    if coluna == 'Index':
        print(f"   • Índice: {memoria} bytes")
    else:
        print(f"   • {coluna}: {memoria} bytes")

memoria_total = df.memory_usage(deep=True).sum()
print(f"Memória total utilizada: {memoria_total} bytes ({memoria_total/1024:.2f} KB)")
print("\n" + "=" * 70)

# Informações adicionais úteis
print("3. INFORMAÇÕES COMPLEMENTARES:")
print("-" * 50)
print(f"Dimensões do dataset: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(f"Nomes das colunas: {list(df.columns)}")
print(f"Índice: de {df.index.min()} até {df.index.max()}")

# Verificar duplicatas
duplicatas = df.duplicated().sum()
print(f"Linhas duplicadas: {duplicatas}")

# Estatísticas básicas para colunas numéricas
print(f"\n Resumo estatístico das colunas numéricas:")
print(df.describe())

print("\n" + "=" * 70)
print("RESUMO DA ANÁLISE:")
print("-" * 50)
print(f"Dataset com {total_linhas} registros e {total_colunas} variáveis")
print(f"{total_nulos} valores ausentes identificados")
print(f"Memória total: {memoria_total/1024:.2f} KB")
print(f"Principais tipos de dados: numéricos e texto")
if duplicatas > 0:
    print(f"⚠️  Atenção: {duplicatas} linha(s) duplicada(s) encontrada(s)")
else:
    print(f"✅ Nenhuma linha duplicada encontrada")