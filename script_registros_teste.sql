﻿select * from app_setor;

--Fase
insert into app_fase (nome) values ('Levantamento');
insert into app_fase (nome) values ('Aguardando Resposta');
insert into app_fase (nome) values ('Analisado');

--EspecieDocumental
insert into app_especiedocumental (nome) values ('Ata');
insert into app_especiedocumental (nome) values ('Memorando');

--Elemento

insert into app_elemento (nome) values ('Logomarca');
insert into app_elemento (nome) values ('Numeração Sequencial');
insert into app_elemento (nome) values ('Datas');
insert into app_elemento (nome) values ('Numero setor destino');
insert into app_elemento (nome) values ('Assinatura');
insert into app_elemento (nome) values ('Título, se: despacho, memorando, outros');
insert into app_elemento (nome) values ('assunto');
insert into app_elemento (nome) values ('carimbo');

--Suporte
insert into app_suporte (nome) values ('Papel');
insert into app_suporte (nome) values ('Eletromagnético (Fita magnética)');
insert into app_suporte (nome) values ('Eletronico (Meio Digital)');
insert into app_suporte (nome) values ('Digitalizado');


-- Genero
insert into app_genero (nome) values ('Textual');
insert into app_genero (nome) values ('Imagem');
insert into app_genero (nome) values ('Audiovisual');
insert into app_genero (nome) values ('Bibliográfico');
insert into app_genero (nome) values ('Cartográfico');
insert into app_genero (nome) values ('Eletrônico');

--Restrição de acesso

insert into app_restricaoacesso (descricao) values ('informações relativas à intimidade, vida privada, honra e imagem das pessoas');
insert into app_restricaoacesso (descricao) values ('informações cujo conhecimento por pessoas não autorizadas possa acarretar danos ao andamento do processo em questão');
insert into app_restricaoacesso (descricao) values ('o documento compõe um Processo Administrativo Disciplinar');
insert into app_restricaoacesso (descricao) values ('o documento requer sigilo fiscal, bancário, comercial, entre outros');


-- Tipo Acumulo
insert into app_tipoacumulo (nome) values ('Caixa');
insert into app_tipoacumulo (nome) values ('Envelope');
insert into app_tipoacumulo (nome) values ('Pasta');


