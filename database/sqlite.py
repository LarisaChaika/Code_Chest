import sqlite3 as sql
from create_bot import bot
import random
from keyboards import kb_client

global base, cursor

def sql_start():

    base = sql.connect('code_chest.db')
    if base:
        print('Connected to database')
    base.execute("CREATE TABLE if NOT EXISTS projects(level TEXT, language TEXT, name TEXT, description TEXT)")
    base.commit()


async def sql_add_project(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message, state):
    async with state.proxy() as data:
        try:
            execute = cursor.execute(
                f"SELECT * FROM projects WHERE level == '{data['choise_level']}' AND language LIKE '{data['choise_lang']}'")
            result = execute.fetchall()
            answer = result[random.randint(0, len(result) - 1)]
            await bot.send_message(message.from_user.id,
                                   f'Уровень {answer[0]}\n Язык {answer[1]}\n Название проекта {answer[2]}\n Описание {answer[3]}',
                                   reply_markup=kb_client)

        except Exception:
            await bot.send_message(message.from_user.id, "Проектов по заданным критериям нет", reply_markup=kb_client)
