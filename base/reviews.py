import sqlite3

def maxID():
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM reviews;"
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

def insert(review):
    try:
        sqlite_connection = sqlite3.connect('ibuyPizza.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO reviews (id, review)
                            VALUES (?, ?);''' 
        data_tuple = (maxID() + 1, review)              
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

        sqlite_selection_query = "SELECT * From reviews;"
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

        sqlite_selection_query = "SELECT * FROM reviews WHERE id=?;"
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