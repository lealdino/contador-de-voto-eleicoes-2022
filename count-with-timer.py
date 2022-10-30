import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")

while True:


    QTD_ELEITORES = 156454011

    url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"
    df = pd.read_json(url)

    new_df = pd.DataFrame.from_records(df['cand'],index=['1', '2'])

    votos_totais  = df['c'][0]
    votos_validos = df['vvc'][0]
    votos_nulos = df['tvn'][0]
    votos_brancos = df['vb'][0]
    abstencoes = df['a'][0]
    eleitorado_apurado = df['ea'][0] * 100 / QTD_ELEITORES

    votacao = new_df[['n','nm','pvap','vap']]
    votacao['pvap'] = votacao['pvap'].str.replace(',','.')

    votacao.columns = ['numero', 'nome_candidato', '%_votos', 'qtde_votos']
    print(votacao)
    print("")
    print("")
    print('votos totais: ', votos_totais )
    print('votos validos: ', votos_validos)
    print('votos nulos: ', votos_nulos)
    print('votos brancos: ', votos_brancos)
    print('abstencoes: ', abstencoes)
    print('% eleitorado_apurado: ', round(eleitorado_apurado, 2))
    print('diferenca %: ', float(votacao['%_votos'][0]) - float(votacao['%_votos'][1]))
    print('diferenca de votos: ', int(votacao['qtde_votos'][0]) - int(votacao['qtde_votos'][1]))

    print("")
    print("")
    print("")

    time.sleep(5)


