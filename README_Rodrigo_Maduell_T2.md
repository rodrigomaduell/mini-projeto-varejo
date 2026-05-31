
# Mini Projeto Avaliativo - Análise Exploratória de Dados de Varejo
**Aluno:** Rodrigo Maduell | **Turma:** T2

## Como executar
1. Clone o repositório
2. Ative o ambiente virtual: 'source venv/bin/activate'
3. Instale as dependências: 'pip install -r requirements.txt
4. Execute: 'python Miniprojeto_RodrigoMaduell_T2.py'

## Sobre o projeto
Análise Exploratória de Dados aplicada a uma base de varejo contendo 830.000 registros, cobrindo diagnóstico, limpeza, transformação e geração de insigths com Python e Pandas.


## Problemas identificados nos dados

1. **Duplicatas:** 
96.553 registros duplicados encontrados, o que representa 11,6% da base.
Devido o fato de não haver ID único de transação para poder distinguir duplicatas de compras repetidas legítimas, optou-se pela remoção.

2. **Nulos disfarçados:** 
Foram identificados 3.650 registros com valor '#N/D' nas colunas 'PR_CAT' e 'PR_NOME', este tipo de identificação costuma vir do Excel.
Os mesmos foram tratados como 'Sem Categoria' e 'Sem Nome' respectivamente.

3. **Data como string**
Identificado que os dados de data estavam alocados como texto - Foi feita a conversão com o método datetime.

## Perguntas de negócio

**1. Qual gênero realiza mais compras e qual a diferença proporcional?**
Mulheres realizaram 382.427 compras contra 351.020 dos homens, indicando uma diferença de 8,9%.
Aproporção de clientes é bem similar, sendo de 519(Feminino) e 481(Masculino), isso indica que mulheres compram com maior frequência.

**2. Quais categorias concentram a maioor parte das vendas?**
A categoria 'Alimentos' lidera com 384.197 vendas (52% do total).
As categorias de 'Higiene' e 'Limpeza' somam 266.334 (36%).
Juntas, as três categorias representam 88% de todas as vendas da base.

**3. Qual o perfil familiar dos clientes e o que isso indica sobre o público alvo?**
Moda e Mediana iguais a zero, com média de 1,15 filhos.
A maioria dos clientes não tem filhos, mas a média acima de 1 indica uma parcela relevante com famílias maiores.
Foi feito uma verificação via 'IQR', identificando a ausência de outliers e confirmando que a distribuição reflete o perfil real da base de dados.

## Insights

1. Base com altovolume de duplicatas (11,6) - Algum possível problema no sistema de origem.

2. Público predominantemente sem filhos - estratégias de marketing familiaar têm menor alcance nesta base.

3. Mulheres são o público mais frequênte - campanhas direcionadas podem ter maior retorno.

4. Alimentos, Higiene e Limpeza dominam 88% das vendas - perfil de compras essênciais do dia a dia, não de consumo por impulso.

5. Ausência de coluna com valor/preço impede análise financeira - limitação relevante para análises de ticket médio e receita.


## Reflexão sobre ETL e qualidade de dados

ETL(Extract, Transform, Load) é o processo que garante que dados brutos cheguem limpos e confiáveis para análise. Nneste projeto foram aplicadas as três etapas:

**Extract:** - carregamento com 'pandas' e 'csv.DictReader'

**Transform:** - remoção de duplicatas,tratamento de nulos disfarçados, conversão de tipose padronização de strings.

**Load:** - geração do DataFrame limpo para dashboards ou modelos.

A qualidade dos dados não é opcional, decisões baseadas em dados sujos geram resultados incorretos.
Os 96.553 registros duplicados, se ignorados, distorceriam qualquer análise de frequência de compra ou segmentação.