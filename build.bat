@echo off
if exist build\ (
    rmdir /s /q build
    )
if not exist build\ (
    md build
    md build\tictacto
    md build\tictacto\sounds
    )
echo building
python -m nuitka --quiet --standalone --python-flag=no_site --user-plugin=CytolkPlugin.py --windows-disable-console --windows-force-stderr=%program%\tictacto.log --windows-force-stdout=%program%\tictacto.log tictacto.py
xcopy /E /I /Q tictacto.dist build\tictacto
echo build completed
echo copying required data files
copy manual.html build\tictacto
copy changes.txt build\tictacto
xcopy /E /I /Q sounds build\tictacto\sounds
if exist tictacto.dist\ (
    rmdir /s /q tictacto.dist
    )
if exist tictacto.build\ (
    rmdir /s /q tictacto.build
    )
echo build successfull