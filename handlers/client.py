from re import I
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from base import menu as m
from base import reviews as r
from base import zakaz as z
from keyboards import kb_general, kb_cancel, kb_menu, kb_zakaz_menu

class FSMClient(StatesGroup):
    review = State()


async def send_welcome(message: types.Message):
    await message.reply("Привет, меня создал @sokudo_chief!", reply_markup=kb_general)

async def send_menu(message: types.Message):
    await message.reply("Меню", reply_markup=kb_menu)

async def send_general(message: types.Message):
    await message.reply("Главная страница", reply_markup=kb_general)

async def send_zakaz(message: types.Message):
    await message.reply("Меню заказа", reply_markup=kb_zakaz_menu)

#---------------------------------------------------------------------

async def upload(message: types.Message):
    await FSMClient.review.set()
    await message.reply("Напишите отзыв.", reply_markup=kb_cancel)

async def insert_review(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Отзыв'] = message.text
        review =  data.get('Отзыв')
        record = (review)
        print(record)
        r.insert(record)
        answer = "Отзыв оставлен"
        await message.answer(str(answer), reply_markup=kb_general)
    await state.finish()

#---------------------------------------------------------------------

async def select_burgeri(message: types.Message):
    menu = m.SelectTable()
    answer = ''
    try:
        for eda in menu:
            eda = m.recordID(eda[0])
            answer = 'ID: ' + str(eda[0][0]) + ', ' + eda[0][2] + ': ' + eda[0][3]
            await message.answer_photo(eda[0][1], caption=answer)
            # answer = answer + eda[0][1] + 'ID: ' + str(eda[0][0]) + ', ' + eda[0][2] + ': ' + eda[0][3]
            # answer = answer + '\n'

    except IndexError:
        answer = "Ошибка"

    # await message.reply(answer)

async def select_bulochki(message: types.Message):
    menu = m.SelectTable2()
    answer = ''

    try:
        for eda in menu:
            eda = m.recordID2(eda[0])
            
            answer = answer + 'ID: ' + str(eda[0][0]) + ', ' + eda[0][1] + ': ' + eda[0][2]
            answer = answer + '\n'

    except IndexError:
        answer = "Ошибка"
    print(answer)
    await message.reply(answer)

async def select_reviews(message: types.Message):
    menu = r.SelectTable()
    answer = ''

    try:
        for eda in menu:
            eda = r.recordID(eda[0])
            
            answer = answer + 'ID: ' + str(eda[0][0]) + ', ' + eda[0][1]
            answer = answer + '\n'

    except IndexError:
        answer = "Ошибка"
    print(answer)
    await message.reply(answer)

async def select_numbers(message: types.Message):
    answer = ''

    try:
        answer = '+375292868672' + '\n' + '+375295158562' + '\n' + '+375254582654' + '\n'
    except IndexError:
        answer = "Ошибка"
    print(answer)
    await message.reply(answer)

#---------------------------------------------------------------------

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Отменено", reply_markup=kb_general)

#---------------------------------------------------------------------

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=['Отмена'], state='*')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_welcome, Text(equals='start', ignore_case=True))

    dp.register_message_handler(send_menu, commands=['Меню'])
    dp.register_message_handler(send_menu, Text(equals='меню', ignore_case=True))

    dp.register_message_handler(send_zakaz, commands=['Сделать_заказ'])
    dp.register_message_handler(send_zakaz, Text(equals='Сделать заказ', ignore_case=True))

    dp.register_message_handler(send_general, commands=['Главное'])
    dp.register_message_handler(send_general, Text(equals='главное', ignore_case=True))

    dp.register_message_handler(select_burgeri, commands=['Бургеры'])
    dp.register_message_handler(select_burgeri, Text(equals='бургеры', ignore_case=True))

    dp.register_message_handler(select_bulochki, commands=['Булочки'])
    dp.register_message_handler(select_bulochki, Text(equals='булочки', ignore_case=True))

    dp.register_message_handler(select_numbers, commands=['Телефоны'])
    dp.register_message_handler(select_numbers, Text(equals='телефоны', ignore_case=True))

    dp.register_message_handler(select_reviews, commands=['Отзывы'])
    dp.register_message_handler(select_reviews, Text(equals='отзывы', ignore_case=True))

    dp.register_message_handler(upload, commands=['Оставить_отзыв'], state=None)
    dp.register_message_handler(upload, Text(equals='оставить отзыв', ignore_case=True))
    dp.register_message_handler(insert_review, state=FSMClient.review)