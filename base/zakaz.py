import sqlite3

def maxID():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM zakaz_bulochki;"
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

def insert(eda_id, adress, name, number, comment):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO zakaz_bulochki (id, eda_id, adress, name, number, comment)
                            VALUES (?, ?, ?, ?, ?, ?);''' 
        data_tuple = (maxID() + 1, eda_id, adress, name, number, comment)              
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
# 
def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From zakaz_bulochki;"
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

        sqlite_selection_query = "SELECT * FROM zakaz_bulochki WHERE id=?;"
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

        sqlite_delete_query = "DELETE FROM zakaz_bulochki WHERE id=?;"
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

def maxID2():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM zakaz_burgeri;"
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

def insert2(eda_id, adress, name, number, comment):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO zakaz_burgeri (id, eda_id, adress, name, number, comment)
                            VALUES (?, ?, ?, ?, ?, ?);''' 
        data_tuple = (maxID() + 1, eda_id, adress, name, number, comment)              
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

        sqlite_selection_query = "SELECT * From zakaz_burgeri;"
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

        sqlite_selection_query = "SELECT * FROM zakaz_burgeri WHERE id=?;"
        cursor.execute(sqlite_selection_query, (id,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def delete2(id):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM zakaz_burgeri WHERE id=?;"
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