from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot
from create_bot import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.donate_kb import kb_donate


async def donate(message: types.Message):
    await bot.send_message(message.from_user.id, "❗ Принять участие в развитии проекта можно бесплатно❗️\n\n"
                                                 "1️⃣ 📣 Расскажите об этом боте своим друзьям и знакомым\n\n"
                                                 "2️⃣ 🔗 Поделитесь ссылкой на бота в своих социальных сетях\n\n"
                                                 "3️⃣ Если вы опытный программист, поделитесь своими идеями\n"
                                                 "(если в боте нет вашего языка, для вас мы его добавим)\n\n"
                                                 "4️⃣ Мы очень комуникабельная команда и открыты к общению, приходите просто поговорить\n\n"
                                                 "5️⃣ Несмотря на то, что проект создан с минимальными затратами он требует вложений\n"
                                                 "💸 Оплата хостинга\n"
                                                 "💸 Оплата облачной базы данных\n"
                                                 "💸 Оплата сайта (домен и хостинг)\n"
                                                 "💸 Привлечение разработчиков мобильных и веб-приложений\n"
                                                 "💸 Реклама (естественно)\n\n"
                                                 "По мере роста проекта - необходимые вложения будут расти\n"
                                                 "и, к сожалению, команда из 4-х человек не сможет полноценно\n"
                                                 "обеспечивать все эти потребности.\n\nМы будем рады любой поддержке 🤝\n"
                                                 " ", reply_markup=kb_donate
                           )


def register_handlers_monetize(dp: Dispatcher):
    dp.register_message_handler(donate, Text(equals=config.get('RUSSIAN', 'donate_btn_text'), ignore_case=True))
