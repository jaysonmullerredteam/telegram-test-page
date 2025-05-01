import requests
import time
import threading

# Токен бота и chat_id
TOKEN = "7786051046:AAEd5j3dSn3ZU-a_uJk0ievx4B0FlAgKxWw"  # Заменить на свой токен
CHAT_ID = "6754382185"  # Заменить на свой chat_id

# Функция для отправки сообщения в Telegram
def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "📡 Ссылка открыта! \n📱 User-Agent:\n" + str(requests.get("https://www.google.com").headers)
    }
    try:
        response = requests.post(url, data=data)
        print("Сообщение отправлено!")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки сообщения: {e}")

# Функция для создания нагрузки на процессор
def cpu_stress():
    while True:
        # Безопасный способ создания нагрузки
        _ = [i**3 for i in range(1000)]

# Создаем и запускаем поток для нагрузки на процессор
cpu_thread = threading.Thread(target=cpu_stress, daemon=True)
cpu_thread.start()

# Отправляем сообщение
send_message()

# Задержка для тестирования (можно настроить по своему усмотрению)
time.sleep(5)
