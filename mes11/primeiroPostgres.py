# CREATE SCHEMA DBO;
# DROP TABLE demo;
# --comando para criar a tabela cliente
# CREATE TABLE DBO.cliente(
#   username VARCHAR(50) NOT NULL,
#   senha VARCHAR(30) NOT NULL,
#   CONSTRAINT cliente_pk PRIMARY KEY(username)
# );

# CREATE SCHEMA DBO;
# DROP TABLE DBO.cliente;
# --comando para criar a tabela cliente
# CREATE TABLE DBO.tempo(
#   id_Tempo serial NOT NULL,
#   precipitacao VARCHAR(50) NOT NULL,
#   tempoMin CHAR
#   tempoMax 
#   dhColeta CHAR(17)
#   nomeCidade
#   CONSTRAINT tempo_pk PRIMARY KEY(idTempo)
#   --CONSTRAINT codigo FORWARD(username)
# );
# CREATE TABLE DBO.monitorada(
#   codigo VARCHAR(10) NOT NULL,
#   CONSTRAINT monitorada_pk PRIMARY KEY(codigo)
# );
# CREATE TABLE DBO.cidade(
#   id_cidade serial NOT NULL,
#   nome VARCHAR(150) NOT NULL,
#   estado CHAR(2) NOT NULL,
#   CONSTRAINT cidade_pk PRIMARY KEY(id_cidade)
# );