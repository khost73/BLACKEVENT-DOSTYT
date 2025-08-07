import time
from rich import print
from rich.console import Console
console = Console()
import keyboard
import random

console.print("██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗███████╗██╗░░░██╗███████╗███╗░░██╗████████╗", style="#000000")
console.print("██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝██║░░░██║██╔════╝████╗░██║╚══██╔══╝", style="#000000")
console.print("██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░", style="#000000")
console.print("██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░", style="#000000")
console.print("╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░", style="#000000")
console.print("\n[bold red]🔥 Присоединяйся к нам в Telegram![/bold red]", style="bold red")
console.print("[bold white]⚔ Хочешь больше утилит, скриптов и обновлений?[/bold white]")
console.print("[bold green]👉 https://t.me/BlackEvent_Official[/bold green]\n")

console.print("[1] Введите количество циклов", style="#ffffff")
Cycles = int(input(''))
console.print("[2] Задержка отправки сообщений", style="#ffffff")
Delay = int(input(''))
console.print("[3] Ввести текст в ручную-[7] Включить список слов-[8] ", style="#ffffff")

mod = int(input(''))


spisok_slov = [
    "⚡ Кто разрешил вам молчать?",
    "📡 Уровень шума недостаточен. Исправляю.",
    "💥 Чат — ты не готов к этому шквалу.",
    "🔥 Я здесь, чтобы было громко.",
    "👁‍🗨 Вижу слабость в сообщениях.",
    "🚷 Тут теперь мои правила.",
    "📢 Не нравится — закрой глаза.",
    "🛑 Тишина — мой личный враг.",
    "📛 Кто думал, что будет спокойно — ошибся.",
    "🎯 Сообщение за сообщением. Чувствуешь давление?",
    "🧨 Молчи, если не можешь кричать.",
    "🕶 Это не флуд — это демонстрация власти.",
    "🔊 Уровень агрессии: включён.",
    "💣 Если не за мной — в стороне стой.",
    "🧠 Каждый пост — удар по тишине.",
    "🧱 Я строю хаос. Камень за камнем.",
    "🛰 Твои фильтры бессильны.",
    "⚙️ Скрипт завёлся. Теперь держись.",
    "🪓 Пауза — не наш стиль.",
    "🔗 Разорви поток? Слабо.",
    "тг "
]


def oss():
    time.sleep(5)
    for number in range(Cycles):
        g = (random.choice(spisok_slov))
        time.sleep(Delay)
        keyboard.write(g)
        keyboard.send("enter")
        keyboard.send("ctrl+tab")








if mod == 7:
    console.print("Введите текст", style="#ffffff")
    text = input()
    time.sleep(5)
    for number in range(Cycles):
        time.sleep(Delay)
        keyboard.write(text)
        keyboard.send("enter")
        keyboard.send("ctrl+tab")
else:
    oss()
