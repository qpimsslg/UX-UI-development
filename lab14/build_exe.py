import os
import sys

script_name = "lab14.py"  # укажите имя вашего скрипта
output_folder = "dist"  # папка с exe файлом

command = f"pyinstaller --onefile --distpath {output_folder} {script_name}"

print(f"Запускается команда: {command}")
os.system(command)

print(f"Готовый exe-файл находится в папке: {output_folder}")
