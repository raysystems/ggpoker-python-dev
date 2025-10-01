#  Instruções de instalação

A aplicação encontra-se dockerizada. Para uma melhor compatibilidade foi testado em amd64 e arm64 em mackbook M1, sem problemas.

1. Git Clone
```bash
git clone https://github.com/raysystems/ggpoker-python-dev.git
```
2. Entrar no dir do repo cloned

3. Dar build na imagem do docker.
```bash
docker build -t ggpoker-dev-docker .
```

Nota: Poderá demorar um pouco, dado que o playwright tem de fazer download dos browsers e das dependências exigidas na documentação.

#  Como Iniciar a aplicação 

1. Executar o container com a imagem criada `ggpoker-dev-docker`
2. 
```bash
docker run -it -p 8000:8000 ggpoker-dev-docker
```

-it para ficar interativo e poder ver as logs do webserver.
-p 8000:8000 para fazer o mapping das portas e o port fowarding.

2. Após os passos referidos acima no guia de instalação deverá estar a correr normalmente: http://localhost:8000



#  Como utilizar a API 


Rota: /weatherForecast/{destrict}/{city}/{day}

Parâmetros (por ordem):
- {destrict} - Nome do Distrito (Ex: Lisboa)
- {city} - Nome da Cidade (Ex: Lisboa)
- {day} - Dia do mês (Ex: 15) - Como o IPMA Só disponibiliza previsão para 7 dias deverá ter sido em consideração este aspeto, caso contrário dará um erro.


IMPORTANTE: destrict e city devem estar exatamente como está no dropdown do site do IPMA 
Método: GET


1. Exemplo de API Call #1:
- Consultar a previsão do tempo para a Madeira no funchal dos 7 dias completos.
```bash
http://localhost:8000/weatherForecast/Madeira/Funchal/all
```
Método: GET

2. Exemplo de API Call #2:
- Consultar a previsão do tempo para a Madeira no funchal do dia 3.
```bash
http://localhost:8000/weatherForecast/Madeira/Funchal/3
```
Método: GET

3. Exemplo de API Call #3:
- Consultar a previsão do tempo para a Lisboa em Odivelas do dia 4.
```bash
http://localhost:8000/weatherForecast/Lisboa/Odivelas/4
```
Método: GET
