<strong>🤖 Sobre — Automação em Python (Cadastro de Produtos)</strong>

Aqui está um "Sobre" / README pronto e claro para o seu script automacao.py — descrevendo o que ele faz, como configurar, executar e dicas importantes para rodar com segurança.
Copie e cole onde quiser (GitHub, README.md, documentação).

<strong>🧾 Automação: Cadastro de Produtos com PyAutoGUI</strong>

Descrição curta
Script em Python que automatiza o cadastro de produtos em um sistema web usando pyautogui para controlar o teclado/mouse e pandas para ler uma base (produtos.csv). O script abre o navegador, faz login e preenche o formulário produto a produto.

<strong>🔎 O que o script faz</strong>

Abre o navegador (via atalho do Windows) e navega até a página de login.

Faz login com as credenciais definidas no código.

Lê produtos.csv com pandas.

Para cada linha do CSV, preenche campos (código, marca, tipo, categoria, preço, custo, observação) usando cliques e tab.

Envia o formulário e rola a página para continuar o cadastro.

Salva tempo e trabalho repetitivo em cadastros manuais.

<strong>✅ Requisitos</strong>

Sistema operacional: Windows (usa conio.h no outro projeto e SetConsoleCursorPosition em outro código; este script de automação usa atalhos do Windows).

Python 3.8+

Bibliotecas Python:

pyautogui

pandas

<strong>🗂️ Formato esperado do produtos.csv</strong>

O CSV usado no script deve ter colunas (nomes de coluna sensíveis ao código):

codigo,marca,tipo,categoria,preco_unitario,custo,obs

exemplo->

codigo,marca,tipo,categoria,preco_unitario,custo,obs <br>
1001,MarcaA,Alimento,Ingredientes,12.50,8.00,Primeiro lote <br>
1002,MarcaB,Utensílio,Cozinha,25.00,15.00, <br>

<strong>📞 Contato / autoria</strong>

Desenvolvido por Caio Renan.
