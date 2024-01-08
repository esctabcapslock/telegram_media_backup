import logging
import requests
import os

# https://api.telegram.org/file/bot<token>/<file_path>.
def download_and_save_file(url, local_path):
    """
    주어진 URL에서 파일을 다운로드하고 지정된 로컬 경로에 저장하는 함수.

    Parameters:
    - url (str): 다운로드할 파일의 URL
    - username (str): 사용자명
    - local_path (str): 로컬에 저장될 파일 경로
    """
    try:
        # 파일 다운로드
        response = requests.get(url)
        response.raise_for_status()

        logging.debug("[download_and_save_file] Response Headers:")
        for key, value in response.headers.items():
            logging.debug(f"{key}: {value}")


        # 디렉토리가 존재하지 않으면 생성
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # 파일 저장
        with open(local_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded and saved to {local_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download file. Error: {e}")

# 예시 사용
# download_and_save_file('https://a.com/path1', 'your_username', 'data/your_username/path2')
