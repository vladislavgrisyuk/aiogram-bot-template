from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = '1640795372:AAGbw9ga8vbKQBQj2O3o_fmZiEKFbIRW9NI' # Забираем значение типа str
ADMINS = '12312123123'  # Тут у нас будет список из админов
IP = '123213123123'  # Тоже str, но для айпи адреса хоста
