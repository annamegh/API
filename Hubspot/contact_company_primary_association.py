
# Esta requisição possuí o intuíto de trocar a associação primária de um contato de uma empresa para outra.

import requests
import json
import pandas as pd
import time

# Authentication
headers = {
    'Authorization': f'Bearer ...',
    'Content-Type': 'application/json'
}

# Caminho do arquivo CSV
file_path = r'\contacts.csv'

# Transformar para dataframe
df = pd.read_csv(file_path)
print(df)

# Pegar as colunas de interesse do dataframe
empresas = df['company_id']
contatos = df['contact_id']


for i in range(df.shape[0]):

    # Requisição, o /1 no final é o código de associação de contato e empresa (primário) encontrado em https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values
    # Para cada objeto diferente, deve ser mudado o nome do objeto e o código de associação
    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contatos[i]}/associations/companies/{empresas[i]}/1'
    response = requests.put(url, headers=headers)
    data = json.loads(response.text)
    print(data)
    print(response.status_code)  # Check response status, se for 200 deu certo

