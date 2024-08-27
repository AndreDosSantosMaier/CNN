
# Classificação de doenças no tomate por meio da detecção das folhas.

Este projeto utiliza uma Rede Neural Convolucional (CNN) para a detecção de doenças em folhas de tomate. O modelo é treinado com um conjunto de dados de imagens de folhas de tomate, cada uma rotulada com a respectiva doença ou saudável e obteve uma acurácia de 90%. Algumas imagens já tratadas estão na pasta assets.


## Rodando localmente

Clone o projeto

```bash
    git clone https://github.com/BeloneDF/ABP-VISAO
```

Entre no diretório do projeto

```bash
    cd ABP-VISAO
```

Criação do ambiente virtual

```bash
    python -m venv ./venv
```

Ativação do ambiente virtual

```bash
    Windows:
    venv/scripts/activate

    Macos/Linux: 
    source venv/bin/activate
```

Instlação das bibliotecas
```bash
    python -m pip install -r requirements.txt

    Ou

    pip install -r requirements.txt
```

Iniciar a aplicação
```bash
    Windows:
    python main.py

    Macos/Linux: 
    python3 main.py
```
## Rodar o projeto

Para ver o front-end do projeto e testá-lo basta abrir o endpoint local:

```bash
  http://localhost:3000
```


## Documentação da API

#### Renderiza o front-end em Jinja2

```http
  GET /
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
|  |  | Retorna o front-end da aplicação |

#### Enviar imagem em base64 para a classficação

```http
  POST /api/cnn
```

| Body   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `foto`      | `string base64` | **Obrigatório**. A sua foto em base64 para a classficação do modelo |

Exemplo:
```bash
  {
    "foto": "string base64"
  }
```



## Stack utilizada

**Front-end:** Jinja2

**Back-end:** Python, Flaskapi

**CNN:** Python

**dataset:** https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf


## Autores

| [Belone Zorzeto Fraga](https://github.com/belonedf) | [Vitor Penteado](https://github.com/VPente) | [Vitor Hugo de Souza](https://github.com/souzavitorhugo) |
|------------------------------------------------------|---------------------------------------------|--------------------------------------------------------|
| ![Foto de Belone Zorzeto Fraga](https://github.com/belonedf.png?size=150) | ![Foto de Vitor Penteado](https://github.com/VPente.png?size=150) | ![Foto de Vitor Hugo de Souza](https://github.com/souzavitorhugo.png?size=150) |
