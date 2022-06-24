// terminal tools:
apt install ffmpeg -y
apt install python -y
apt install nodejs -y
apt install php -y
apt install git -y



// baixar o sistema:
cd ~/
git clone {url}
mv SampYT/openurl.js ~/../usr/lib/node_modules/localtunnel/node_modules/openurl



// nodejs tools:
npm install -g localtunnel



// python tools:
pip install --upgrade pip
pip install youtube-search-python
pip install yt-dlp



// Ligando o sistema:
×× abra uma janela shell ××
cd ~/SampYT
php -S localhost:8080 & python checker.py

×× deve retornar algo assim ××
running

×× abra outra janela shell ××
lt --port 8080 --subdomain meuserver

×× deve retornar algo assim ××
https://meuserver.loca.lt



Para testar acesse dessa forma:
https://meuserver.loca.lt/index.php?name=Outro%20Mundo

Obs: %20 representa o espaço entre as palavras
