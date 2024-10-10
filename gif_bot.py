import os
import telebot
from moviepy.editor import concatenate_videoclips as conc, VideoFileClip as clip

BOT_TOKEN = 'TOKEN' # Заменить на токен выданный Telegram
GIF_CHAR_DIRECTORY = "./gif_chars/" # Папка с GIF для символов
USER_GIFS_DIRECTORY = "./user_gifs/" # Папка для хранения готовых GIF

# Создание директории для пользовательских GIF-файлов, если она не существует.
if not os.path.exists(USER_GIFS_DIRECTORY):
    os.makedirs(USER_GIFS_DIRECTORY)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Привет, чатик! Я умею делать гифки из слов! "
        "Напиши мне слово или словосочетание на русском без знаков препинания!"
    )
    bot.send_message(message.from_user.id, welcome_text)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет'")
    elif message.text.startswith("/make_gif"):
        bot.send_message(message.from_user.id, "Для создания гифки напиши слово.")
    else:
        create_gif(message)


def create_gif(message):
    user_input = message.text.strip()
    if user_input:
        print(user_input)
        bot.send_message(message.from_user.id, "Создаю гифку!")

        try:
            gif_path = make_gif(user_input)
            if gif_path:
                with open(gif_path, 'rb') as img:
                    bot.send_animation(message.from_user.id, img)
                manage_gifs()
        except FileNotFoundError:
            bot.send_message(message.from_user.id, "Ошибка: не все гифки доступны. Проверьте введенные слова.")
        except Exception as e:
            bot.send_message(message.from_user.id, f"Произошла ошибка: {str(e)}")
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, введите непустое слово.")


def gif_list(usr_inp):
    gifs = []
    for char in usr_inp.upper():
        if char == " ":
            gifs.append(clip(f'{GIF_CHAR_DIRECTORY}/space.gif'))
        else:
            gif_path = f'{GIF_CHAR_DIRECTORY}/{char}.gif'
            if os.path.exists(gif_path):
                gifs.append(clip(gif_path))
            else:
                print(f"GIF не найден для: {char}")
    return gifs


def make_gif(inp):
    clips = gif_list(inp)
    if clips:
        final_gif_path = f'{USER_GIFS_DIRECTORY}/{inp}.gif'
        final = conc(clips)
        final.write_gif(final_gif_path)
        return final_gif_path


def manage_gifs():
    gif_files = sorted(os.listdir(USER_GIFS_DIRECTORY),
                       key=lambda f: os.path.getmtime(os.path.join(USER_GIFS_DIRECTORY, f)))
    if len(gif_files) > 5:
        for gif in gif_files[:-5]:
            os.remove(os.path.join(USER_GIFS_DIRECTORY, gif))


bot.infinity_polling()
