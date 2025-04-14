from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Carrega modelo e encoders
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

with open("encoder_profissao.pkl", "rb") as f:
    encoder_profissao = pickle.load(f)

with open("encoder_mix.pkl", "rb") as f:
    encoder_mix = pickle.load(f)

with open("encoder_pagamento.pkl", "rb") as f:
    encoder_pagamento = pickle.load(f)

@app.route("/")
def index():
    return render_template("formulario.html",
                           profissoes=encoder_profissao.classes_,
                           mixes=encoder_mix.classes_,
                           comportamentos=encoder_pagamento.classes_)


from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Carrega modelo e encoders
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

with open("encoder_profissao.pkl", "rb") as f:
    encoder_profissao = pickle.load(f)

with open("encoder_mix.pkl", "rb") as f:
    encoder_mix = pickle.load(f)

with open("encoder_pagamento.pkl", "rb") as f:
    encoder_pagamento = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None

    if request.method == "POST":
        try:
            profissao = request.form["profissao"]
            mix = request.form["mix"]
            comportamento = request.form["comportamento"]

            profissao_cod = encoder_profissao.transform([profissao])[0]
            mix_cod = encoder_mix.transform([mix])[0]
            comportamento_cod = encoder_pagamento.transform([comportamento])[0]

            entrada = pd.DataFrame({
                "profissao": [profissao_cod],
                "mix_credito": [mix_cod],
                "comportamento_pagamento": [comportamento_cod]
            })

            score = modelo.predict(entrada)[0]

        except Exception as e:
            score = f"Erro detectado: {e}"

    return render_template("formulario.html",
                           profissoes=encoder_profissao.classes_,
                           mixes=encoder_mix.classes_,
                           comportamentos=encoder_pagamento.classes_,
                           score=score)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
