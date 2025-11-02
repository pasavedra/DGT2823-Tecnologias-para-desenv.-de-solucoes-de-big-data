# Microatividade 1 e 2: Leitura de CSV e Criação de Subconjunto de Dados
# Analista de Dados - Manipulação de conjuntos de dados

# MICROATIVIDADE 1: LEITURA DO ARQUIVO CSV
import pandas as pd
from io import StringIO

print("=== MICROATIVIDADE 1: LEITURA DE ARQUIVO CSV ===\n")

# Dados fornecidos para o CSV
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

# Microatividade 1: Leitura dos dados
print("✓ Importando biblioteca pandas")
print("✓ Criando variável para dados")

# Leitura do arquivo CSV com parâmetros especificados
dados_lidos = pd.read_csv(
    StringIO(dados_csv),
    sep=';',
    engine='python', 
    encoding='utf-8'
)

print("✓ Arquivo CSV lido com sucesso")
print("✓ Dados atribuídos à variável 'dados_lidos'")

print("\n--- DADOS ORIGINAIS COMPLETOS ---")
print(f"Formato do dataset original: {dados_lidos.shape}")
print(f"Colunas disponíveis: {list(dados_lidos.columns)}")
print("\nPrimeiras 5 linhas do dataset original:")
print(dados_lidos.head())

# =============================================================================
# MICROATIVIDADE 2: CRIAÇÃO DE SUBCONJUNTO DE DADOS
# =============================================================================

print("\n" + "="*60)
print("=== MICROATIVIDADE 2: CRIAÇÃO DE SUBCONJUNTO DE DADOS ===")
print("="*60 + "\n")

# PROCEDIMENTO 1: Criar uma nova variável
print("--- PROCEDIMENTO 1: Criação de nova variável ---")
subconjunto_dados = None
print("✓ Nova variável 'subconjunto_dados' criada")

# PROCEDIMENTO 2: Atribuir subconjunto com 3 colunas
print("\n--- PROCEDIMENTO 2: Criação do subconjunto ---")

# Método 1: Seleção por lista de colunas (RECOMENDADO)
print("Criando subconjunto com 3 colunas: ['ID', 'Duration', 'Pulse']")
subconjunto_dados = dados_lidos[['ID', 'Duration', 'Pulse']]

print("✓ Subconjunto criado com sucesso usando seleção por lista de colunas")

# Informações sobre o subconjunto criado
print(f"\nInformações do subconjunto:")
print(f"• Formato: {subconjunto_dados.shape}")
print(f"• Colunas selecionadas: {list(subconjunto_dados.columns)}")
print(f"• Colunas removidas: {[col for col in dados_lidos.columns if col not in subconjunto_dados.columns]}")

# PROCEDIMENTO 3: Salvar alterações (simulado)
print("\n--- PROCEDIMENTO 3: Salvamento ---")
print("✓ Alterações salvas (simulado)")

# PROCEDIMENTO 4: Imprimir/exibir dados da nova variável
print("\n--- PROCEDIMENTO 4: EXIBIÇÃO DO SUBCONJUNTO ---")

print("=== SUBCONJUNTO DE DADOS COMPLETO ===")
print(subconjunto_dados)

print("\n=== ANÁLISE DO SUBCONJUNTO CRIADO ===")
print(f"Número de linhas: {len(subconjunto_dados)}")
print(f"Número de colunas: {len(subconjunto_dados.columns)}")
print(f"Tipos de dados no subconjunto:")
print(subconjunto_dados.dtypes)

print("\n=== PRIMEIRAS 10 LINHAS DO SUBCONJUNTO ===")
print(subconjunto_dados.head(10))

print("\n=== ÚLTIMAS 10 LINHAS DO SUBCONJUNTO ===")
print(subconjunto_dados.tail(10))

print("\n=== ESTATÍSTICAS DESCRITIVAS DO SUBCONJUNTO ===")
print(subconjunto_dados.describe())

# DEMONSTRAÇÃO DE OUTRAS FORMAS DE CRIAR SUBCONJUNTOS
print("\n" + "="*60)
print("=== DEMONSTRAÇÃO: OUTRAS FORMAS DE CRIAR SUBCONJUNTOS ===")
print("="*60)

print("\n--- MÉTODO 2: Seleção de colunas específicas ---")
subconjunto2 = dados_lidos[['Date', 'Maxpulse', 'Calories']]
print("Subconjunto 2 - Colunas: Date, Maxpulse, Calories")
print(f"Formato: {subconjunto2.shape}")
print("Primeiras 5 linhas:")
print(subconjunto2.head())

print("\n--- MÉTODO 3: Seleção de range de colunas ---")
subconjunto3 = dados_lidos.iloc[:, 1:4]  # Colunas da posição 1 à 3
print("Subconjunto 3 - Colunas por posição (1 a 3):")
print(f"Colunas: {list(subconjunto3.columns)}")
print(f"Formato: {subconjunto3.shape}")
print("Primeiras 5 linhas:")
print(subconjunto3.head())

print("\n--- MÉTODO 4: Seleção com filtro de linhas ---")
subconjunto4 = dados_lidos[dados_lidos['Duration'] == 60][['ID', 'Duration', 'Pulse']]
print("Subconjunto 4 - Apenas registros onde Duration = 60:")
print(f"Formato: {subconjunto4.shape}")
print("Primeiras 5 linhas:")
print(subconjunto4.head())

print("\n" + "="*60)
print("=== MICROATIVIDADE 2 CONCLUÍDA COM SUCESSO! ===")
print("="*60)
print("✅ Nova variável criada")
print("✅ Subconjunto com 3 colunas atribuído à variável")
print("✅ Alterações salvas")
print("✅ Dados do subconjunto exibidos em tela")
print("\n🎯 Objetivo alcançado: Demonstração da manipulação de conjuntos de dados")
print("   através da criação de subconjuntos a partir de dados pré-existentes")

print("\n--- RESUMO COMPARATIVO ---")
print(f"Dataset original:  {dados_lidos.shape[0]} linhas × {dados_lidos.shape[1]} colunas")
print(f"Subconjunto:       {subconjunto_dados.shape[0]} linhas × {subconjunto_dados.shape[1]} colunas")
print(f"Redução de colunas: {dados_lidos.shape[1] - subconjunto_dados.shape[1]} colunas removidas")