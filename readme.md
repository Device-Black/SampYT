// terminal tools:<br>
apt install ffmpeg -y<br>
apt install python -y<br>
apt install nodejs -y<br>
apt install php -y<br>
apt install git -y<br><br><br>



// baixar o sistema:<br>
cd ~/<br>
git clone https://github.com/Device-Black/SampYT.git<br>
mv SampYT/openurl.js ~/../usr/lib/node_modules/localtunnel/node_modules/openurl<br><br><br>



// nodejs tools:<br>
npm install -g localtunnel<br><br><br>



// python tools:<br>
pip install --upgrade pip<br>
pip install youtube-search-python<br>
pip install yt-dlp<br><br><br>



// Ligando o sistema:<br>
×× abra uma janela shell ××
cd ~/SampYT<br>
php -S localhost:8080 & python checker.py
<br><br>
×× deve retornar algo assim ××<br>
running<br><br><br>

×× abra outra janela shell ××<br>
lt --port 8080 --subdomain meuserver
<br><br>
×× deve retornar algo assim ××<br>
https://meuserver.loca.lt<br><br><br>



Para testar acesse dessa forma:<br>
https://meuserver.loca.lt/index.php?name=Outro%20Mundo<br><br>

Obs: %20 representa o espaço entre as palavras
