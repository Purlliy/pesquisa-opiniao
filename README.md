## 📊Sistema de Pesquisa de Opinião ao Atendimento ao Cliente

---

## 📌Sobre o Projeto
Este projeto é um programa em Python que realiza uma pesquisa de satisfação com clientes. Ele coleta informações de entrevistados, como o seu nome, idade e opinião sobre o atendimento. Por final, apresenta um resumo com os resultados.
O objetivo do programa é registrar as opiniões de clientes sobre um atendimento, validar os dados inseridos e exibir um relatório final simples.
<div style="display: inline_block"><br>
<img align="center" alt="Python" height="40" width="50"
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> 
  
---

## ⚙️Funcionalidade
O programa consegue armazenar a entrada de dados de múltiplos entrevistados, validação da idade (verificando se a idade é maior que 0 e menor que 120), percebe se algum valor errado foi inserido (exemplo: entrada inválida de texto na idade, ao invés de número). Além disso, o programa limpa a tela a cada novo entrevistado, para não poluir a tela. O programa segue em algumas partes regras de validação. Como na idade, em que deve ser inserido um número inteiro entre 1 à 119, caso o usuário digite um valor inválido, o programa solicita novamente a entrada e não continua até o valor válido ser inserido. Outra parte em que segue essas regras é na opinião, em que se qualquer outro valor além de 1 à 3, o programa vai considerar a resposta como invalida e não vai contabilizar na contagem final.

---

## 🖥️Como usar
Primeiro o código vai pedir para o usuário inserir o seu nome, e depois sua idade (a idade tem que ser válida, não podendo ser menor que 1 e maior que 119, além de não poder ter texto nela). Após o usuário ter colocado seu nome e idade, o programa pede para inserir a sua satisfação com o atendimento, indo de 1 (excelente), 2 (bom) e 3 (ruim). Caso seja inserido algum valor além desses 3, o programa desconsidera a resposta e continua para o proximo entrevistado. Se o valor inserido for correto, o programa contabiliza a sua resposta e continua para o proximo entrevistado. Por final, após ser entrevistado 50 pessoas, o código irá mostrar um relatório simples, contendo a quantidade de pessoas que escolheram a opção 1 (excelente), e a opção 3 (ruim).

<img alt="Static Badge" src="https://img.shields.io/badge/pesquisa-opiniao-brightgreen?style=for-the-badge">
<img alt="Static Badge" src="https://img.shields.io/badge/Github-black?logo=github">
