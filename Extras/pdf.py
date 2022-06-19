from itertools import count
import re as regex
from tkinter import E
import fitz  # this is pymupdf
import pandas as pd
with fitz.open("424009-1-22.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

te = text[1110:2000]
stt = 'adquirentes'
end = '213.924'
###------------------------NOME-------------------------------
nome = ':'
nomefim = ','
nomefinal = (te[te.index(nome)+len(nome):te.index(nomefim)])

###------------------------CPF-------------------------------
cpf = 'CPF/MF'
cpffim = 'residente'
cpfsujo = (te[te.index(cpf)+len(cpf):te.index(cpffim)])
###------------------------UNIDADE-------------------------------
unidade = 'n°'
unidadefim = '(“'
unidadefinal = (te[te.index(unidade)+len(unidade):te.index(unidadefim)])
###------------------------BLOCO-------------------------------
bloco = '”)'
blocofim = 'loc'
blocosujo = (te[te.index(bloco)+len(bloco):te.index(blocofim)])
###------------------------EMPREENDIMENTO-------------------------------
empreendimento = 'torre,'
empreendimentofim = 'ser'
empreendimentosujo = (te[te.index(empreendimento)+len(empreendimento):te.index(empreendimentofim)])
empreendimento1 = 'Residencial'
empreendimentofim2 = 'a'
empreendimentolimpo2 = (empreendimentosujo[te.index(empreendimento1)+len(empreendimento1):te.index(empreendimentofim2)])




data = {'Empreendimento':  [empreendimentolimpo2],
        'Bloco': [blocosujo],
        'Unidade': [unidadefinal],
        'Nome': [nomefinal],
        'CPF': [cpfsujo],
         }

df = pd.DataFrame(data)
print(df)
print(empreendimentolimpo2)
print(empreendimentosujo)
df.to_excel (r'C:\Users\T-Gamer\OneDrive - Fundação São Paulo\Documentos\excel\ ', header=True)

