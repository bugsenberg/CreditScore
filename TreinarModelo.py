import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Carrega os dados
df = pd.read_csv("clientes.csv")

# Codifica colunas categóricas
encoder_profissao = LabelEncoder()
df["profissao"] = encoder_profissao.fit_transform(df["profissao"])

encoder_mix = LabelEncoder()
df["mix_credito"] = encoder_mix.fit_transform(df["mix_credito"])

encoder_pagamento = LabelEncoder()
df["comportamento_pagamento"] = encoder_pagamento.fit_transform(df["comportamento_pagamento"])

# Mantém apenas as colunas desejadas
X = df[["profissao", "mix_credito", "comportamento_pagamento"]]
y = df["score_credito"]

# Treina o modelo
modelo = RandomForestClassifier()
modelo.fit(X, y)

# Salva o modelo e os encoders
with open("modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

with open("encoder_profissao.pkl", "wb") as f:
    pickle.dump(encoder_profissao, f)

with open("encoder_mix.pkl", "wb") as f:
    pickle.dump(encoder_mix, f)

with open("encoder_pagamento.pkl", "wb") as f:
    pickle.dump(encoder_pagamento, f)

print("✅ Novo modelo treinado e salvo com sucesso!")
