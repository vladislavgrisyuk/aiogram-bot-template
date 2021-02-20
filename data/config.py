from environs import Env
import os
from dotenv import load_dotenv

# Теперь используем вместо библиотеки python-dotenv библиотеку environs

load_dotenv()
BOT_TOKEN = '1640795372:AAGbw9ga8vbKQBQj2O3o_fmZiEKFbIRW9NI' # Забираем значение типа str
ADMINS = '12312123123'  # Тут у нас будет список из админов
IP = '123213123123'  # Тоже str, но для айпи адреса хоста
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
