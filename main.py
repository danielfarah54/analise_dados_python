import pandas as pd
import plotly.express as px

# PASSOS 1 e 2:
# Importar base
df = pd.read_csv('telecom_users.csv')
df = df.drop('Unnamed: 0', axis=1)

# Mostrar base
display(df)

# PASSO 3:
print(df.info())

# 3.a:
# Transformar coluna que deveria ser número e está como texto em número
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')
print(df.info())

# 3.b:
# Remover a coluna que está 100% vazia
df = df.dropna(how='all', axis=1)

# Remover a linha que tem um item vazio
df = df.dropna()

print(df.info())

# PASSO 4:
display(df['Churn'].value_counts())
display(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# PASSO 5:
# Para edições nos gráficos: https://plotly.com/python/histograms/
for coluna in df:
    if coluna != 'IDCliente':
        # Criar a figura
        fig = px.histogram(df, x=coluna, color='Churn')
        # Exibir a figura
        fig.show()
        display(df.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente'])

# Conclusão e Ações:

'''
- MesesComoCliente baixo em MUITO cancelamento -> retenção de clientes é horrível:
    - Ou o pós venda é péssimo/1as experiências do cliente
    - Ou a captação de clientes traz muitos clientes desqualificados

- Métodos de pagamento:
    - Os métodos automáticos tem uma taxa de churn menor
    - O Boleto Eletronico é horrível, se puder, vamos evitar -> ideia: oferecer benefícios caso a pessoa escolha um método automático (débito automático, cartao de credito)
    
- Tipo de contrato é bizarra a diferença
    - Contratos mensais tendem a ser MUITO mais cancelados do que contratos anuais
    - Quase 90% dos cancelamentos estão em contratos mensais
    
- Pessoas que não têm os serviços extras (Tech Support, Device Protection, Online Security) tendem a cancelar muito mais do que o normal
    - Quase 80% dos cancelamentos não usam esses serviços
    
- Ponto de Atenção:
    - Fibra Ótica -> taxa de cancelamento bem maior do que os outros serviços (o triplo de cancelamentos em relação a DSL, mesmo com menos clientes)
'''