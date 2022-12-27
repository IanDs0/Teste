## Instalar as bibliotecas utilizadas

`pip install -r requirements.txt`

## Comando para executar cada um dos arquivos .py

### Executa o arquivo que pega os contatos e salva em um '.csv'

`python ./csv/pegarcontatos.py`

### Executa o sistema de envio de mensagens que pega os contatos e salvos e procura o padrão de grupos ou contato que estão em um '.csv' que deve ser colocado

`python enviomensagem.py`

## Fazer o Arquivo '.exe'

`python -m PyInstaller --onefile -w arquivo_desejado.py`