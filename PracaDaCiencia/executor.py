import subprocess

with open("executor.txt") as f:
    try:
        for line in f:
            cmd = line.strip()
            if cmd:  # pula linhas vazias
                print(f"Executando: {cmd}")
                subprocess.run(cmd, shell=True)
        print("Scrips finalizados com Sucesso!\n Para executar o Back-End, basta utilizar:\n -- python manage.py runserver")
    except(KeyError):
        print(f"Error {KeyError}")