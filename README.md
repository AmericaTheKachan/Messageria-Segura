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
### Como rodar

Copie a string de conexão do Driver Atlas no mongodb

Cole a string no arquivo .env no campo ATLAS_URI

Execute o arquivo main.py
