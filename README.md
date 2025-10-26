# Messageria-Segura
### Fluxo
Usuário faz login, escolhe escrever mensagem para alguém (informa o usuário do destino), escreve a mensagem (min. 
50 caracteres) e informa a chave criptografica. Neste momento a mensagem é cifrada e gravada no banco mongo na coleção
Messages (cifrada).
Um usuário determinado, acessa o sistema e escolhe:
Ler minhas novas mensagens ou obter as novas mensagens (não lidas em ordem descrescente) e mostrar o remetente limpo 
(from Pedro, dia e hora). Em seguida o usuário escolhe qual mensagem quer ler e o sistema solicita a chave criptográfica
para decifrar a mensagem.
#
### Banco: MongoDB
Gravar no banco como: 

from (nome) to (nome)

status: lido/não lido
#
### Outras definições
Perguntar a chave sempre quando for acessar uma mensagem.

Opção mostrar novas mensagens e mostrar mensagens antigas.
    
Caso a chave não esteja certa, pergunte ao usuário se a chave está correta.

Escolher qual algoritmo simétrico usar
#
### Dicas de implementação
pymongo (driver de conexão do python com o MongoDB Atlas)
Criar uma classe para gerenciar a conexão, outra para mensagem, usuário, POJO, Auth, etc
