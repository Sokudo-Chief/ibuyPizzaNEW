from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from base import zakaz as z

class zakaz(StatesGroup):
    eda_id = State()
    adress = State()
    name = State()
    number = State()
    comment = State()

from keyboards import kb_general, kb_cancel

#-------------------------------------------------------------------

async def upload2(message: types.Message):
    await zakaz.eda_id.set()
    await message.reply("Введите айди еды", reply_markup=kb_cancel)

async def insert_eda_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Айди еды'] = message.text
    await zakaz.next()
    await message.reply("Введите адрес")

async def insert_adress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Адрес'] = message.text
    await zakaz.next()
    await message.reply("Введите имя")

async def insert_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Имя'] = message.text
    await zakaz.next()
    await message.reply("Введите номер")

async def insert_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Номер'] = message.text
    await zakaz.next()
    await message.reply("Введите комментарий (если не нужно, пишите \"нет\")")

async def insert_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Комментарий'] = message.text
        eda_id = int(data.get('Айди еды'))
        adress = data.get('Адрес')
        name = data.get('Имя')
        number = int(data.get('Номер'))
        comment = data.get('Комментарий')
        print(eda_id, adress, name, number, comment)
        z.insert(eda_id, adress, name, number, comment)
        answer = 'Айди еды: ' + str(eda_id) + '\n' + 'Адрес: ' + str(adress) + '\n' + 'Номер: ' + str(number) + '\n' + 'Имя: ' + name + '\n' + 'Комментарий: ' + str(comment)
        await message.answer(str(answer), reply_markup=kb_general)
    await message.answer('Заказ добавлен')
    await state.finish()

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
    
    dp.register_message_handler(upload2, commands=['Заказать_булочки'], state=None)
    dp.register_message_handler(upload2, Text(equals='заказать булочки', ignore_case=True))
    dp.register_message_handler(insert_eda_id, state=zakaz.eda_id)
    dp.register_message_handler(insert_adress, state=zakaz.adress)
    dp.register_message_handler(insert_name, state=zakaz.name)
    dp.register_message_handler(insert_number, state=zakaz.number)
    dp.register_message_handler(insert_comment, state=zakaz.comment)