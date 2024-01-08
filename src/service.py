from datetime import datetime
import logging
from db import add_photo, get_photo_not_done, get_user_by_id, update_photo_done, update_photo_error
from tgtoken import CHAT_ID
from telegram import check_telegram_info, get_file_info, set_message_reaction, telegram_download_file
import sqlite3

from tool.get_file_extension import get_file_extension


download_queue = []

def init_download_queue(conn: sqlite3.Connection):
    logging.debug('[init_download_queue]')
    photo_list =  get_photo_not_done(conn)
    for row in photo_list:
        # (1, 'AgACAgUAAxkBAAMXZZwKpsIiQ5mclUkidbyJC07HCmQAAo27MRsaxdlUErt5WSTI-W0BAAMCAANzAAM0BA', -4030904827, 23, 1992250600, 0, 0)
        id , file_id, chat_id, message_id, user_id, done, error = row
        if done==1 or error == 1:
            logging.error(f"처리되지 않은 init_download_queue: {row}")
            continue
        tp = {'message_id':message_id, 'chat_id':chat_id, 'file_id':file_id, 'user_id':user_id}
        logging.debug(f"init_download_queue: tp:{tp}")
        download_queue.append(tp)


def update_msg_list(conn: sqlite3.Connection, chat_id:int):
    logging.debug(f'[update_msg_list]], chat_id:{chat_id}')
    d = check_telegram_info(chat_id)
    job_q = []
    for i in d:
        if 'message' not in i:
            continue
        update_id = i['update_id']
        message = i['message']
        message_id = message['message_id']
        sender_id = message['from']['id']
        chat_id = message['chat']['id']

        if 'photo' in message:
            media = message['photo']
            file_id = media[-1]['file_id']
            tp = {'update_id':update_id, 'message_id':message_id, 'chat_id':chat_id, 'file_id':file_id, 'user_id':sender_id}
            # print(f"tp:{tp}")
            job_q.append(tp)
            
        elif 'video' in message:
            media = message['video']
            file_id = media['file_id']
            tp = {'update_id':update_id, 'message_id':message_id, 'chat_id':chat_id, 'file_id':file_id, 'user_id':sender_id}
            job_q.append(tp)

    for tp in job_q:
        logging.debug(f'for job_p, tp:{tp}')
        exist =  add_photo(conn, chat_id=tp['chat_id'], message_id=tp['message_id'], file_id= tp['file_id'], user_id=tp['user_id'])
        if exist != False:
            tp['id'] = exist
            download_queue.append(tp)





def down_media(conn: sqlite3.Connection):
    while len(download_queue):
        tp = download_queue.pop()
        logging.debug(f"[down_media], {tp}")
        s = get_file_info(tp['file_id'])
        chat_id, message_id, file_id, user_id = tp['chat_id'], tp['message_id'], tp['file_id'], tp['user_id']
        if 'file_path' not in s:
            logging.error('file_path not exist')
            update_photo_error(conn, chat_id=chat_id, message_id=message_id, file_id= file_id, error=True)
            continue
        file_path = s['file_path']
        ext = get_file_extension(file_path)
        
        user_info = get_user_by_id(conn, user_id)
        save_path = user_id
        if user_info:
            _,_, save_path = user_info
        try:
            current_datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            telegram_download_file(file_path, f"data/{save_path}/{current_datetime_str}-{file_id}{ext}")
        except _ as e:
            logging.error(f"error 발생함, e:{e}")
        finally:
            r = set_message_reaction(chat_id, message_id)
            logging.debug(f'set_message_reaction: {r}')
            update_photo_done(conn, chat_id=chat_id, message_id=message_id, file_id= file_id, done=True)
            







