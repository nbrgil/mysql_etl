# MySQL ETL Fee
Autor: Rodrigo L. Gil

Esse projeto cria um ambiente com mysql e python para converter um grupo de arquivos .csv (exportados de um banco relacional) para um modelo dimensional.

# Estrutura de pastas

Temos a seguinte estrutura:
  - datafiles: Contém todos os arquivos .csv;
  - final_datafiles: Dump resultante do novo modelo;
  - init-sql: Contém o DDL do banco de dados dimensional;
  - model: Arquivo com o modelo do MySQL workbench. Caso não esteja corrompido, usar o model.png;
  - script: Script genéricos para limpar tabelas ou iniciar o processo;
  - src/csv_reader: Classes python que fazem a leitura dos arquivos;
  - src/table_importer: Classes python que importar para as tabelas finais;
  - scr/transformation: Classes python dedicadas às transformações;
  - util: Outras classes;
  - main.py: Arquivo que é executado quando o docker inicia;
  - docker-compose.yml: Inicia mysql e etl;
  - Dockerfile: Usado para compilar a imagem do docker;

### Analisando fora do ambiente

Foi escolhido trabalhar com docker porque foi a maneira mais prática de testar e subir um ambiente com mysql.
Mas para analisar em outro ambiente, basta subir o dump da pasta 'final_datafiles'

### Analisando no ambiente / Executando o ETL

Para executar com o docker, estando na pasta raiz:

```ssh
docker-compose -f docker-compose.yml up fee_db
```

Após o banco terminar de subir, execute:

```ssh
docker-compose -f docker-compose.yml up fee_etl
```

Esse processo vai ler os arquivos csv e importar os dados no MySQL.
Infelizmente ele mostra algumas mensagens de warning que ainda não foram resolvidas, mas terminar assim deu certo:
```ssh
fee_etl_1  | --> ok
```

Depois disso é só conferir as tabelas no banco.

### Modelo

O projeto foi feito considerando que hoje há uma grande dificuldade para saber qual a taxa correta a ser cobrar, porque existem muitas regras no banco de dados.
As regras foram colocadas no ETL, e todas as taxas vão parar em uma única tabela chamada "mydb.fee".

Com essa tabela, o usuário/aplicação/relatório poderão consultar qual o imposto a se pagar com um SELECT simples filtrando CONTA, FORMA DE PAGAMENTO e NÚMERO DA PARCELA, fazendo join somente em casos que deseja mais informações da conta ou do membro relativo ao pagamento.
