import pandas as pd

#dataframe = pd.DataFrame({"produto":["chocolate", "banana"], "quantidade":[200,80], "preco":[3.00,0.50]})
#print(dataframe)

admissoes = pd.read_csv("./ipea_admissoes.csv")
admissoes.head()
print("\n ----------------")

demissoes = pd.read_csv("./ipea_demissoes.csv")
#print(demissoes)

print("somatorio das demissoes ------------- \n", demissoes.demissoes.sum())
print("somatorio das demissoes ------------- \n", demissoes['demissoes'].sum())
