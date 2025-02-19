from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Категория заявок", callback_data="categories")],
    [InlineKeyboardButton(text="Личный кабинет", callback_data="cabinet")],
    [InlineKeyboardButton(text="Написать в поддержку", callback_data="support")],
    [InlineKeyboardButton(text="FAQ", callback_data="faq")]
]

back_to_menu = [
    [InlineKeyboardButton(text="Назад", callback_data="menu")]
]

admin = [
    [InlineKeyboardButton(text="SEO", callback_data="admin_menu1")],
    [InlineKeyboardButton(text="SMM", callback_data="admin_menu2")],
    [InlineKeyboardButton(text="Видеомонтаж", callback_data="admin_menu3")],
    [InlineKeyboardButton(text="Дизайн", callback_data="admin_menu4")],
    [InlineKeyboardButton(text="Контекст", callback_data="admin_menu5")],
    [InlineKeyboardButton(text="Копирайтинг", callback_data="admin_menu6")],
    [InlineKeyboardButton(text="Продюсирование", callback_data="admin_menu7")],
    [InlineKeyboardButton(text="Разработка", callback_data="admin_menu8")],
    [InlineKeyboardButton(text="Сайт", callback_data="admin_menu9")],
    [InlineKeyboardButton(text="Таргет", callback_data="admin_menu10")],
    [InlineKeyboardButton(text="Назад", callback_data="admin_back")]
]

load_post = [
    [InlineKeyboardButton(text="Загрузить заявку", callback_data="load_post")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
back_to_menu = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
admin = InlineKeyboardMarkup(inline_keyboard=admin)
load_post = InlineKeyboardMarkup(inline_keyboard=load_post)