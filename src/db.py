import logging
import sqlite3



def db_init() -> sqlite3.Connection:
    logging.debug('[db_init]')
    conn = sqlite3.connect('photo.db')
    cur = conn.cursor()
    cur.execute('''
       CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY,
            file_id TEXT UNIQUE,
            chat_id INTEGER,
            message_id INTEGER,
            user_id INTEGER,
            done INTEGER DEFAULT 0,
            error INTEGER DEFAULT 0
        );
    ''')
    # .open photo.db
    # ALTER TABLE photos ADD COLUMN error INTEGER DEFAULT 0;
    # .exit
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            save_name TEXT UNIQUE
        );
    ''')

    conn.commit()
    cur.close()

    return conn

def add_user(conn:sqlite3.Connection, user_id:int, name:str, save_name:str):

    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 유저 추가를 위한 SQL 쿼리
        query = "INSERT INTO users (id, name, save_name) VALUES (?, ?, ?)"
        cursor.execute(query, (user_id, name, save_name))

        # 변경사항을 데이터베이스에 반영
        conn.commit()

        print(f"User '{name}' added successfully!")

    except sqlite3.IntegrityError as e:
        # UNIQUE 제약 조건 위배 시 에러 처리
        print(f"Error: {e}")
        print(f"User with save_name '{save_name}' already exists.")

    finally:
        # 커서 닫기
        cursor.close()


def exists_photo(conn:sqlite3.Connection, chat_id:int, message_id:int, file_id:str) -> bool:
    # SQL 쿼리 작성 및 실행
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM photos WHERE chat_id = ? AND message_id = ? AND file_id = ?"
    cursor.execute(query, (chat_id, message_id, file_id))

    # 결과 가져오기
    count = cursor.fetchone()[0]

    cursor.close()

    # 레코드가 존재하는지 여부 반환
    return count > 0

import sqlite3

def add_photo(conn: sqlite3.Connection, chat_id: int, message_id: int, file_id: str, user_id: int, done: int = 0) -> bool|int:
    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 사진 추가를 위한 SQL 쿼리
        query = "INSERT OR FAIL INTO photos (chat_id, message_id, file_id, user_id, done) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (chat_id, message_id, file_id, user_id, done))

        # 변경사항을 데이터베이스에 반영
        conn.commit()

        last_inserted_id = cursor.lastrowid

        logging.debug(f"Photo with file_id '{file_id}' added successfully, last_inserted_id:{last_inserted_id}!")
        return last_inserted_id

    except sqlite3.IntegrityError as e:
        # UNIQUE 제약 조건 위배 시 에러 처리
        # print(f"Error: {e}")
        logging.debug(f"Photo with file_id '{file_id}' already exists.")
        return False

    finally:
        # 커서 닫기
        cursor.close()

# def add_photo(conn: sqlite3.Connection, chat_id: int, message_id: int, file_id: str, user_id: int, done: int = 0):
#     try:
#         # 데이터베이스 커서 생성
#         cursor = conn.cursor()

#         # 사진 추가를 위한 SQL 쿼리
#         query = "INSERT INTO photos (chat_id, message_id, file_id, user_id, done) VALUES (?, ?, ?, ?, ?)"
#         cursor.execute(query, (chat_id, message_id, file_id, user_id, done))

#         # 변경사항을 데이터베이스에 반영
#         conn.commit()

#         print(f"Photo with file_id '{file_id}' added successfully!")

#     except sqlite3.IntegrityError as e:
#         # UNIQUE 제약 조건 위배 시 에러 처리
#         print(f"Error: {e}")
#         print(f"Photo with file_id '{file_id}' already exists.")

#     finally:
#         # 커서 닫기
#         cursor.close()




def update_photo_done(conn: sqlite3.Connection, chat_id: int, message_id: int, file_id: str, done: bool=True):
    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 사진 업데이트를 위한 SQL 쿼리
        query = "UPDATE photos SET done = ?  WHERE chat_id = ? AND message_id = ? AND file_id = ?"
        cursor.execute(query, (int(done),  chat_id, message_id, file_id))

        # 변경사항을 데이터베이스에 반영
        conn.commit()

        print(f"Photo with file_id '{file_id}' updated successfully!")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # 커서 닫기
        cursor.close()



def update_photo_error(conn: sqlite3.Connection, chat_id: int, message_id: int, file_id: str, error:bool=True):
    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 사진 업데이트를 위한 SQL 쿼리
        query = "UPDATE photos SET error = ?  WHERE chat_id = ? AND message_id = ? AND file_id = ?"
        cursor.execute(query, (int(error), chat_id, message_id, file_id))

        # 변경사항을 데이터베이스에 반영
        conn.commit()

        print(f"Photo with file_id '{file_id}' updated successfully!")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # 커서 닫기
        cursor.close()

def get_photo_not_done(conn: sqlite3.Connection):
    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 아직 완료되지 않은 사진을 조회하는 SQL 쿼리
        query = "SELECT * FROM photos WHERE done = 0 AND error = 0"
        cursor.execute(query)

        # 결과 가져오기
        photos = cursor.fetchall()

        # print("Photos not done:")
        # for photo in photos:
        #     print(photo)

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # 커서 닫기
        cursor.close()
        return photos


def get_user_by_id(conn: sqlite3.Connection, user_id: int):
    try:
        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 사용자 ID로 사용자를 조회하는 SQL 쿼리
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))

        # 결과 가져오기
        user = cursor.fetchone()

        if user:
            print(f"User found with ID {user_id}: {user}")
        else:
            print(f"No user found with ID {user_id}")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # 커서 닫기
        cursor.close()
        return user

