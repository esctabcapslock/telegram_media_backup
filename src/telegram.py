import logging
import requests
from tool.download_and_save_file import download_and_save_file
from tgtoken import TOKEN
from tool.encode_dict_values import encode_dict_values, encode_quary

class HTTPReqError(Exception):
    pass





def http_req_wrop(url, params:dict):
    
    res = requests.get(url, params=encode_quary(params))
    if res.status_code != 200:
        raise HTTPReqError(f"This is a http error!, url:{url}, param:{params}, res.url:{res.url} code:{res.status_code}, body:{res.text}")
    
    json_data = res.json()
    if 'ok' not in json_data:
        raise HTTPReqError("ok not in json_data")
    if json_data['ok'] != True:
        raise HTTPReqError(f"json_data.ok != 'True', it's {json_data['ok']}")
    result = json_data['result']
    return result


def check_telegram_info(chat_id:int=-1):
    # 모든 체팅 내역을 가져오기.
    if chat_id==-1:
        chat_id = '@chat'
    
    data = http_req_wrop(f"https://api.telegram.org/bot{TOKEN}/getUpdates", {'chat_id':chat_id})
    logging.debug(f'check_telegram_info res:{data}')
    return data

def get_file_info(file_id:str):
    if type(file_id) != str:
        raise TypeError("file_id not string")
    data = http_req_wrop(f"https://api.telegram.org/bot{TOKEN}/getFile", {'file_id':file_id})
    logging.debug(f'get_file_info res:{data}')
    return data




# https://api.telegram.org/file/bot<token>/<file_path>.
def telegram_download_file(file_path, local_path):
    download_and_save_file(f"https://api.telegram.org/file/bot{TOKEN}/{file_path}", local_path)

# 예시 사용
# download_and_save_file('https://a.com/path1', 'your_username', 'data/your_username/path2')


def set_message_reaction(chat_id:int, message_id):
    # setMessageReaction?chat_id=1111&message_id=2222&reaction=[{"type":"emoji","emoji":"🐳"}]
    data = http_req_wrop(f"https://api.telegram.org/bot{TOKEN}/setMessageReaction", 
                         {'chat_id':chat_id,
                          'message_id': message_id,
                          'reaction':[{
                              'type':'emoji',
                              'emoji':"🐳"
                          }]
                          })
    return data