<h1>FAST DASH SEARCH - BUSCA RÁPIDA DE DASH</h1>

Busca rápida de links de relatórios de PowerBI através de filtragem por cliente ou pesquisa por palavras chave. Qualquer elemento na área da tabela da aplicação pode ser copiado com um clique duplo do botão esquerdo do mouse.

<img width="852" height="506" alt="image" src="https://github.com/user-attachments/assets/5d7e9f3a-6d21-4897-b742-067414d965b6" /><p></p>

A ideia é que o analista de dados/BI consiga coletar rapidamente algum link de relatório solicitado, seja o link do dash específico, o link do workspace do cliente, ou o link do dash no aplicativo.

Em assets, o arquivo teste.csv deve ser utilizado como base de dados, com os dados separados por vírgula. Por exemplo:<p></p>
<b>Cliente,Nome,Tipo de Link,Link,Keywords<p></p>
ABC,DASH DE GESTÃO,Individual,facebook.com,funcionários</b>

O arquivo <b>guardacaminho.py</b> deve ser editado da seguinte forma:

<img width="301" height="45" alt="image" src="https://github.com/user-attachments/assets/9f4ab4be-f1db-4490-8e44-ae3568a347a3" />

<ul>
  <li><b>"guardacaminho"</b> deve possuir o path de <b>"teste.csv", na pasta de assets.</b>.</li>
  <li><b>"guardalupa"</b> deve possuir o path de <b>"lupa1.png"</b>, também na pasta de assets.</li>
</ul>
