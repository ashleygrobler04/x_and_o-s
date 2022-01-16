pyinstaller tictacto.py -w --noconfirm
copy manual.html dist\tictacto
copy changes.txt dist\tictacto
md dist\tictacto\sounds
copy sounds\ dist\tictacto\sounds\