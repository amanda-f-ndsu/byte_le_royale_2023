@echo off
del /q *.pyz

xcopy /s/e/i "game" "wrapper/game"
mkdir "./wrapper/server/"
xcopy /s/e/i "./server/client" "./wrapper/server/client"
python -m zipapp "wrapper" -o "launcher.pyz" -c
del /q/s "wrapper/game"
del /q/s "wrapper/server/client"
del /q/s "wrapper/server"