# PingPong

O comando para que o cliente consiga mandar o ping é '**-p**'<br>
Caso outro cliente queira utilizar, funcionará. Pois está com thread.

Protocolo utilizado: **UDP** <br>
Arquitetura: **Cliente-Servidor**<br>

Caso o o cliente envie um '**-p**' ao servidor, ele imediantamente enviará ao cliente umas resposta
denominada '**pong**'. Na mesma hora de recebimento de '**pong**' o cliente irá subtrair (usando a lib
timeit) a hora de chegada pela a hora de envio do pacote, retornando em MS. Sendo assim calculado o TIMESTAMP.
