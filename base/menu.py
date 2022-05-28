import sqlite3

def convert(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


    
def maxID():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM burgeri;"
        cursor.execute(sqlite_selection_query)
        records = cursor.fetchone()
        cursor.close()
        return records[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert(photo, name, description):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO burgeri (id, photo, name, description)
                            VALUES (?, ?, ?, ?);''' 
        data_tuple = (maxID() + 1, photo, name, description)              
        cursor.execute(insert_query, data_tuple)
        sqlite_connection.commit()
        print('Запись успешно добавлена.')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From burgeri;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def recordID(id):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM burgeri WHERE id=?;"
        cursor.execute(sqlite_selection_query, (id,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def delete(id):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM bulochki WHERE id=?;"
        cursor.execute(sqlite_delete_query, (id,))
        sqlite_connection.commit()
        print("Запись", id, "успешна удалена.")
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert2(photo, name, description):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO bulochki (id, photo, name, description)
                            VALUES (?, ?, ?, ?);''' 
        # maxID() + 1
        data_tuple = (maxID() + 1, photo, name, description)              
        cursor.execute(insert_query, data_tuple)
        sqlite_connection.commit()
        print('Запись успешно добавлена.')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def SelectTable2():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From bulochki;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def recordID2(id):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM bulochki WHERE id=?;"
        cursor.execute(sqlite_selection_query, (id,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def update1(photo, id):
    try:
        sqlite_connection = sqlite3.connect("ibuyPizza.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE burgeri SET photo=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (photo, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# photo = convert(r"C:\Users\perek\Pictures\recept_5112_nf2l.jpg")
# name = "Чизбургер"
# description = "Две булочки, посередине мясо, сыр, огурцы, соус."
# insert(photo, name, description)
# print(SelectTable())
# update1(photo, 1)