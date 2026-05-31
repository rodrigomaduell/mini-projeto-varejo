#==========================================================================
# Mini Projeto Avaliativo - Módulo 1
# Aluno: Rodrigo Maduell | Turma: T2
#==========================================================================


import pandas as pd
import numpy as np
import csv
import datetime

#==========================================================================
# SPRINT 1 - Importação e carregamento dos dados
#==========================================================================

# Carregamento com pandas para análise exploratória
df = pd.read_csv('data/Base_Varejo.csv', encoding='latin-1', sep=';')

# Carregamento nativo com csv.DictReader
with open('data/Base_Varejo.csv', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    dados_nativos = list(reader)


# Diagnóstico inicial
print('=' * 55)
print('SPRINT 1 - DIAGNÓSTICO INICIAL')
print('=' * 55)
print(f'Registros    : {df.shape[0]}')
print(f'Colunas      : {df.shape[1]}')
print(f'\nNomes das colunas: \n{df.columns}')
print(f'\nTipos de dados: \n{df.dtypes}')
# Verificação de nulos disfarçados
print()
strings_falsas = ['NULL', 'N/A', 'NA', 'NaN', 'none', 'None', '#N/D', '', ' ']
for col in df.select_dtypes(include='string').columns:
    for s in strings_falsas:
        count = (df[col] == s).sum()
        if count > 0:
            print(f'Nulos disfarçados: Coluna {col} | valor "{s}" | ocorrências: {count}')

#===========================================================================
# SPRINT 2 - Transformação de tipos
#===========================================================================

# Converter DATA de string para datetime    
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors="coerce")

#Garantir tipos numéricos corretos
df['CO_ID'] = pd.to_numeric(df['CO_ID'], errors='coerce')
df['CL_ID'] = pd.to_numeric(df['CL_ID'], errors='coerce')
df['CL_EC'] = pd.to_numeric(df['CL_EC'], errors='coerce')
df['CL_FHL'] = pd.to_numeric(df['CL_FHL'], errors='coerce')
df['PR_ID'] = pd.to_numeric(df['PR_ID'], errors='coerce')

# Padronizar strings - remover  espaços e aplicar title case
df['CL_GENERO'] = df['CL_GENERO'].str.strip().str.title()
df['CL_SEG'] = df['CL_SEG'].str.strip().str.title()
df['PR_CAT'] = df['PR_CAT'].str.strip().str.title()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.title()

print('\n' + '=' * 55)
print('SPRINT 2 - TRANSFORMAÇÃO DE TIPOS')
print('=' * 55)
print(f'Tipos após conversão: \n{df.dtypes}')
print(f'\nAmostra da coluna DATA: \n{df["DATA"].head(3).values}')
print(f'\nValores únicos em CL_GENERO: {df["CL_GENERO"].unique()}')
print(f'\nValores únicos em CL_SEG: {df["CL_SEG"].unique()}')

#===========================================================================
#SPRINT 3 - Limpeza de nulos e duplicatas
#===========================================================================

#Remover colunas vazias (Unnamed)
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])

# Relatórios de nulos antes da limpeza
print('\n' +'=' * 55)
print('\nSPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS')
print('\n' + '=' *55)
print(f'\nNulos por coluna antes da limpeza: {df.isnull().sum().sum()}')
print(f'\nDuplicatas encontradas: {df.duplicated().sum()}')

# Preencher categorias vazias com 'Sem Categoria'
# A decisão foi de manter os registros e somente sinalizar a ausência de categoria.
df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')
df['CL_SEG'] = df['CL_SEG'].fillna('Sem Segmento')

# Substituindo '#N/D' por "Sem Categoria" 
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Sem Categoria')
df['CL_SEG'] = df['CL_SEG'].replace('#N/D', 'Sem Segmento')
df['PR_NOME'] = df['PR_NOME'].replace('#N/D', 'Sem Nome')

# Remover duplicatas
# A decisão foi de remover todas colunas idênticas.
# Ausência de ID único de transação ou coluna quantidade impede de distinguir duplicatas de compras repetidas legítimas.
df = df.drop_duplicates().reset_index(drop=True)

# Relatório após limpeza
print(f'\nNulos por coluna após limpeza: {df.isnull().sum()}')
print(f'\nDuplicatas após limpeza: {df.duplicated().sum()}')
print(f'\nRegistros após limpeza: {df.shape[0]}')


#===========================================================================
# SPRINT 4 - Estatística descritiva - coluna CL_FHL(N° de filhos)
#===========================================================================

filhos = df['CL_FHL']

print('\n' + '=' * 55
      + '\nSPRINT 4 - ESTATÍSTICA DESCRITIVA - CL_FHL (N° DE FILHOS)'
      + '\n' + '=' * 55)
print(f'Média: {filhos.mean():.2f}')
print(f'Mediana: {filhos.median():.2f}')
print(f'Desvio Padrão: {filhos.std():.2f}')
print(f'Moda: {filhos.mode()[0]}')
print(f'Mínimo: {filhos.min()}')
print(f'Máximo: {filhos.max()}')
print(f'Contagem: {filhos.count()}')
print(f'\nQuartis:')
print(f'  Q1 (25%): {filhos.quantile(0.25)}')
print(f'  Q2 (50%): {filhos.quantile(0.50)}')
print(f'  Q3 (75%): {filhos.quantile(0.75)}')


#===========================================================================
# SPRINT 5 - Agrupamentos
#===========================================================================

print('\n' + '=' * 55)
print('\nSPRINT 5 - AGRUPAMENTOS')
print('\n' + '=' * 55)

# Agrupamento 1: Compras por gênero
genero = df.groupby('CL_GENERO').agg(
    total_compras=('PR_ID', 'count'),
    clientes_unicos=('CL_ID', 'nunique')
).round(2).reset_index()

print('\nAgrupamento 1 - Compras por Gênero:')
print(genero.to_string())


# Agrupamento 2: Categorias mais Vendidas
categoria = df.groupby('PR_CAT').agg(
    total_compras=('PR_CAT', 'count'),
).sort_values(by='total_compras', ascending=False).reset_index()

print('\nAgrupamento 2 - Categorias mais Vendidas:')
print(categoria.to_string())


#=======================================================================
# SPRINT 6 - Relatório final e conclusões
#=======================================================================

print('\n' + '=' * 55)
print('\nSPRINT 6 - RELATÓRIO FINAL - PRINCIPAIS INSIGHTS')
print('\n' + '=' * 55)
print(f"""
1. VOLUME DE DADOS:
      - Base original: {len(dados_nativos)} registros
      - Base limpa: {df.shape[0]} registros
      - Duplicatas removidas: {len(dados_nativos) - df.shape[0]}

2. QUALIDADE DOS DADOS:
        - Nulos remanescentes: {df.isnull().sum().sum()}
        - Categorias sem nome: {(df['PR_CAT'] == 'Sem Categoria').sum()}

3. PERFIL DOS CLIENTES:
        - Moda de filhos: {filhos.mode()[0]}
        - Mediana de filhos: {filhos.median():.2f}
        - Média de filhos: {filhos.mean():.2f}

4. COMPORTAMENTO POR GÊNERO:
        - Compras femininas: {genero.loc[genero['CL_GENERO'] == 'F', 'total_compras'].values[0]}
        - Compras masculinas: {genero.loc[genero['CL_GENERO'] == 'M', 'total_compras'].values[0]}

5. CATEGORIA MAIS VENDIDA:
        - Categoria líder: {categoria.loc[0, 'PR_CAT']} com {categoria.loc[0, 'total_compras']} compras
""")


