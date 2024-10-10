[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->


  <h3 align="center">Telegram GIF BOT</h3>
  <p align="center">
    Телеграм бот, который умеет создавать гифки из слов
    <br />


## О проекте

Бот был создан в качестве pet проекта для использования в чате друзей.

Как это работает:
* Пользователь отправляет боту слово или словосочетание кириллицей.
* В ответ пользователь получает визуализацию своего запроса в виде gif анимации.


### Код написан на:

* [![Python][Python]][Python-url]


## Особенности работы

* В папке "gif_chars" хранятся заранее подготовленные gif файлы, визуализирующие каждую из букв русского алфавита.
* При желании можно заменить эти файлы на свои.
* При запуске бота на сервере создается папка "user_gifs",
в которой хранятся последние 5 анимаций, созданных пользователем. 

### Настройка

_Ниже представлены возможности по настройке_

1. Получи токен [Туториал](https://core.telegram.org/bots/tutorial)
2. Скопируй репозиторий
   ```sh
   git clone https://github.com/ABCser/gif_bot.git
   ```
3. Введи свой токен в следующую строку в файле `gif_bot.py`
   ```py
   BOT_TOKEN = 'TOKEN' # Заменить на токен выданный Telegram
   ```
4. Запусти `gif_bot.py` на удаленном сервере предварительно скопировав папку `gif_chars`
5. Можно также заменить анимации в папке `gif_chars` на пользовательские, сохраняя при этом имена файлов
6. Бот хранит последние 5 gif созданных пользователем. Для изменения количества замени `5` на необходиме число в этой части кода:
   ```py
   def manage_gifs():
    gif_files = sorted(os.listdir(USER_GIFS_DIRECTORY),
                       key=lambda f: os.path.getmtime(os.path.join(USER_GIFS_DIRECTORY, f)))
    if len(gif_files) > 5:
        for gif in gif_files[:-5]:
            os.remove(os.path.join(USER_GIFS_DIRECTORY, gif))
   ```

<p align="right">(<a href="#readme-top">Наверх</a>)</p>


## Контакты

Serj MG - [@mogilats](https://t.me/@mogilats)

Ссылка на проект: [https://github.com/ABCser/gif_bot](https://github.com/ABCser/gif_bot)

<p align="right">(<a href="#readme-top">Наверх</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ABCser/gif_bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ABCser/gif_bot/network/members
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ABCser/gif_bot/issues
[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/