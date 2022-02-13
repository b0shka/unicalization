DEFAULT_PARAM_NOISE_PHOTO = 30
DEFAULT_PARAM_BRIGHTNESS_PHOTO = 1.2
DEFAULT_PARAM_BRIGHTNESS_VIDEO = 0.1

SETTINGS_PARAM = {
    'low_brightness_photo': 0.8,
    'middle_brightness_photo': DEFAULT_PARAM_BRIGHTNESS_PHOTO,
    'high_brightness_photo': 1.5,
    'low_brightness_video': 0.001,
    'middle_brightness_video': DEFAULT_PARAM_BRIGHTNESS_VIDEO,
    'high_brightness_video': 0.2,
    'little_noise_photo': 10,
    'middle_noise_photo': DEFAULT_PARAM_NOISE_PHOTO,
    'big_noise_photo': 50,
}

NAME_SETTINGS = {
    'low': 'Низкая',
    'high': 'Высокая',
    'middle': 'Средняя',
    'little': 'Маленький',
    'big': 'Большой'
}


REPLACE_SYMBOLS_1 = "###"
REPLACE_SYMBOLS_2 = "$$$"
REPLACE_SYMBOLS_3 = "@@@"
REPLACE_SYMBOLS_4 = "***"

START_MESSAGE = """
Привет! 👋

Коротко о возможностях:
1) Уникализация фото и видео 
2) Вы можете сами задавать параметры (яркость, уровни шума и т.д) под ваше усмотрение, так и воспользоваться стандартом, который мы задали
3) Полная очистка метаданных
4) Быстрая обработка (Фото 1-10 секунд, видео 10-30 секунд)
5) В разделе инфо вы можете посмотреть различные фишки по проверке ваших креативов
"""

UNOCALIZATION = """
Отправьте фотографию или видео
"""

INFORMATION = """
На данном сайте вы можете проверить свои креативы на разные параметры. 
Узнайте, как будет видеть искусственный интеллект ваши креативы, что позволит вам убрать нежелательные моменты с ваших фото и видео.
👉🏻 https://cloud.google.com/vision

Короткая инструкция. 
1) Заходите на сайт
2) Загружайте фото, где написано Try the API
3) Смотрите параметры вашего креатива
"""

SETTINGS = """
Настройки
"""

GET_SETTINGS = f"""
Яркость фотографии: {REPLACE_SYMBOLS_1}
Яркость видео: {REPLACE_SYMBOLS_2}
Шум на фотографии: {REPLACE_SYMBOLS_3}
"""

CHOICE_TEXT = ('Меня еще этому не научили', 'Я не знаю про что вы', 'У меня нет ответа', 'Я еще этого не умею', 'Беспонятия про что вы')

VERY_LONG_VIDEO = """
Максимальная продолжительность видео 1 минута
"""

STATISTIC = f"""
Всего пользователей - {REPLACE_SYMBOLS_1}
Использовавшие уникализацию - {REPLACE_SYMBOLS_2}
Использовавшие уникализацию сегодня - {REPLACE_SYMBOLS_3}
Не использовавшие уникализацию ни разу - {REPLACE_SYMBOLS_4}
"""