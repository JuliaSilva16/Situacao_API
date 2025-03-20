from flask_pydantic_spec import FlaskPydanticSpec
from flask import Flask,jsonify
from datetime import datetime
app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                        title='First API - SENAI',
                         version='1.0',
                         )
spec.register(app)
"""
    API para calcular a diferença entre as datas
    
    ##Endpoint
    ('/verificacao_datas/<data_dia>/<data_mes>/<data_ano>')
    
    ##Parâmentro
    (data_dia,data_mes,data_ano) ( XX/XX/XX) - qualquer outro jeito digitado irá dar errado
    
    ## Resposta(JSON)
    
    }
    "Data digitada":verificar_data.strftime("%d/%m/%Y"),
    "Data atual":data_atual.strftime("%d/%m/%Y"),
    "Situacao": situacao,
    "Dias":int(diferenca_dia),
    "Mes":str(diferenca_mes),
    "Ano":str(diferenca_ano)
    }


    ##Erros possíveis:
    except ValueError:
    return jsonify({'Error'}) - vai dar erro se o formato da dta estiver incorreto
    
"""

@app.route('/verificacao_datas/<data_dia>/<data_mes>/<data_ano>')
def verificacao_datas(data_dia,data_mes,data_ano):
    try:
        data_atual = datetime.now()
        verificar_data = datetime(day=int(data_dia), month=int(data_mes), year=int(data_ano))

        if data_atual == verificar_data:
            situacao = "Presente"

        elif data_atual < verificar_data:
            situacao = "Futuro"

        else:
            situacao = "Passado"

        if situacao == "Futuro" or situacao == "Passado":
            diferenca_dia = int(abs(verificar_data - data_atual).days)
            diferenca_mes = abs((verificar_data.year - data_atual.year ) * 12 + verificar_data.month - verificar_data.month)
            diferenca_ano = abs(verificar_data.year - data_atual.year)
            if diferenca_mes % 12 == 0 and verificar_data.day > 0:
                diferenca_mes = diferenca_dia - 1

            return jsonify({"Data digitada":verificar_data.strftime("%d/%m/%Y"),
                            "Data atual":data_atual.strftime("%d/%m/%Y"),
                            "Situacao": situacao,
                            "Dias":int(diferenca_dia),
                            "Mes":str(diferenca_mes),
                            "Ano":str(diferenca_ano)
                            })

    except ValueError:
        return jsonify({'Error'})

if __name__ == '__main__':
    app.run(debug=True)

