
import json
import logging
from urllib.parse import quote, urlencode
# from urllib.parse import urlencode

def encode_dict_values(original_dict:dict)->dict:
    encoded_dict = {}
    # 딕셔너리 순회
    for key, value in original_dict.items():
        # 값이 문자열이나 숫자인 경우 그대로 사용
        if isinstance(value, (str, int, float)):
            encoded_dict[key] = value
        # 그 외의 경우 URL 인코딩 적용
        elif isinstance(value, (list, dict)):
            encoded_dict[key] = json.dumps(value)
        else:
            raise TypeError("아직 코딩 안 한거임")
    logging.debug(f'encode_dict_values: {original_dict} -> {encoded_dict}')
    return encoded_dict

def encode_quary(orig_params:dict)->str:
    params = encode_dict_values(orig_params)
    # return quote(str(params))
    out = []
    for key, value in params.items():
        out.append(f"{quote(key)}={quote(str(value))}")
    return '&'.join(out)
