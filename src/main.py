from db import db_init
from service import down_media, init_download_queue, update_msg_list
import time

from tgtoken import CHAT_ID_LIST


import logging

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,  # 로깅 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # 파일로 로그 저장
        logging.StreamHandler()  # 콘솔에 로그 출력
    ]
)



if __name__ == '__main__':
    
    c = db_init()
    init_download_queue(c)
    down_media(c)
    while True:
        for chat_id in CHAT_ID_LIST:
            logging.debug(f"[main>while] chat_id: {chat_id}")
            update_msg_list(c, chat_id)
            down_media(c)
        time.sleep(10)