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
print('SPRINT 1 - DIAFNÓSTICO INICIAL')
print('=' * 55)
print(f'Registros    : {df.shape[0]}')
print(f'Colunas      : {df.shape[1]}')
print(f'\nNomes das colunas: \n{df.columns}')
print(f'\nTipos de dados: \n{df.dtypes}')


