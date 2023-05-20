import os, shutil, json, datetime
from colorama import Fore

os.system("cls")

black = Fore.LIGHTBLACK_EX
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX



fail = 0

with open("config.json", "r+") as f:
    jsonfile = json.load(f)
path = jsonfile["path"]
pathtocopy = jsonfile["pathtocopy"]

while True:
    if os.path.exists(path):
        shutil.copy(path, pathtocopy)
        os.system(f"title NoxiusFileDrop ^| Done ^| {datetime.datetime.utcnow()}")
        break
    else:
        fail += 1
        print(f"{m}[{w}ERROR{m}] {r}NoxiusFileDrop {m}| {black}Tries: {r}{fail}")
        os.system(f"title NoxiusFileDrop ^| Errores: {fail} ^| {datetime.datetime.now():%H:%M:%S}")

print(f"{m}[{w}OK{m}] {g}Cracked Sucesffuly, copied to {y}{pathtocopy} {black}at the {y}{datetime.datetime.utcnow()}")
os.system("pause >nul")