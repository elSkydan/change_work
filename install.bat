@echo off
echo Проверка и установка зависимостей проекта...

:: Проверяем pip
python -m ensurepip
python -m pip install --upgrade pip setuptools wheel packaging

:: Устанавливаем зависимости
pip install -r requirements.txt

echo Зависимости установлены!
pause
