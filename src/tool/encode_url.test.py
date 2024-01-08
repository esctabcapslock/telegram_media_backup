from encode_dict_values import encode_quary


param = {'chat_id': 1111, 'message_id': 2222, 'reaction': [{'type': 'emoji', 'emoji': '🐳'}]}
print(f"{encode_quary(param)}")