def run():
    # -*- coding: utf-8 -*-
    """mapeamento_ean_chave.ipynb

    Automatically generated by Colaboratory.

    Original file is located at
        https://colab.research.google.com/drive/1_zX7ldAq9uzc_ozhUrANmMYSUBsg6LhI
    """

    import pandas as pd

    df_mapping = pd.read_pickle('../datasets/ean_key_mapping.pkl')
    print(df_mapping.shape)
    df_mapping.head()

    """### Aplicando as substituições"""

    medicamentos_data_path = '../datasets/medicamentos/augmented/'
    anvisa_data_path = '../datasets/anvisa/augmented/'

    medicamentos_data_file = 'medicamentos_aumentado_preproc.csv'
    anvisa_pa_data_file = 'anvisa_principio_ativo_aumentado_preproc.csv'
    anvisa_prod_data_file = 'anvisa_produto_aumentado_preproc.csv'

    """### MEDICAMENTOS"""

    df = pd.read_csv('{}{}'.format(medicamentos_data_path, medicamentos_data_file),
                     sep=';',
                     dtype={0:int, 1:str, 2:str})
    print(df.shape)
    df.head()

    dfm = pd.merge(df, df_mapping, on='ean')
    print(dfm.shape)
    dfm.head()

    del dfm['ean']

    data_file = 'medicamentos_aumentado_preproc_mapped.csv'

    dfm.to_csv('{}{}'.format(medicamentos_data_path, data_file),
               sep=';',
               index=False,
               encoding='utf-8')

    """### ANVISA PRINCIPIO_ATIVO"""

    df = pd.read_csv('{}{}'.format(anvisa_data_path, anvisa_pa_data_file),
                     sep=';',
                     dtype={0:int, 1:str, 2:str})
    print(df.shape)
    df.head()

    dfm = pd.merge(df, df_mapping, on='ean')
    print(dfm.shape)

    del dfm['ean']

    data_file = 'anvisa_principio_ativo_aumentado_preproc_mapped.csv'

    dfm.to_csv('{}{}'.format(anvisa_data_path, data_file),
               sep=';',
               index=False,
               encoding='utf-8')

    """### ANVISA PRODUTO"""

    df = pd.read_csv('{}{}'.format(anvisa_data_path, anvisa_prod_data_file),
                     sep=';',
                     dtype={0:int, 1:str, 2:str})
    print(df.shape)
    df.head()

    dfm = pd.merge(df, df_mapping, on='ean')
    print(dfm.shape)

    del dfm['ean']

    data_file = 'anvisa_produto_aumentado_preproc_mapped.csv'

    dfm.to_csv('{}{}'.format(anvisa_data_path, data_file),
               sep=';',
               index=False,
               encoding='utf-8')