pyinstaller tictacto.py -w --noconfirm
copy manual.html dist\tictacto
md dist\tictacto\sounds
copy sounds\ dist\tictacto\sounds\