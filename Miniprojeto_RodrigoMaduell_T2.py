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


print('=' * 55)
#SPRINT 3 - Limpeza de nulos e duplicatas
print('=' * 55)

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

# Investigação das duplicatas
print('\nAmostra das duplicatas:')
print(df[df.duplicated(keep=False)].sort_values('CO_ID').head(10).to_string())

# Remover duplicatas
df = df.drop_duplicates().reset_index(drop=True)

# Relatório após limpeza
print(f'\nNulos por coluna após limpeza: {df.isnull().sum()}')
print(f'\nDuplicatas após limpeza: {df.duplicated().sum()}')
print(f'\nRegistros após limpeza: {df.shape[0]}')

