def get_token() -> str:
    with open('pw/token.txt', 'r') as file:
        return file.read().strip()
TOKEN = get_token()

CHAT_ID = int(open('pw/chat_id.txt').read().strip()) if open('pw/chat_id.txt', 'r', encoding='utf-8', errors='ignore') else -1
CHAT_ID_LIST = [CHAT_ID]