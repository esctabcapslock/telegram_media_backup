import telegram

d = [{'update_id': 10034908, 'my_chat_member': {'chat': {'id': -4030904827, 'title': 'test2', 'type': 'group', 'all_members_are_administrators': True}, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'en'}, 'date': 1704722928, 'old_chat_member': {'user': {'id': 6414831328, 'is_bot': True, 'first_name': 'photoCollector', 'username': 'my_photo_auto_collector_bot'}, 'status': 'left'}, 'new_chat_member': {'user': {'id': 6414831328, 'is_bot': True, 'first_name': 'photoCollector', 'username': 'my_photo_auto_collector_bot'}, 'status': 'member'}}}, {'update_id': 10034909, 'message': {'message_id': 20, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'en'}, 'chat': {'id': -4030904827, 'title': 'test2', 'type': 'group', 'all_members_are_administrators': True}, 'date': 1704722928, 'group_chat_created': True}}, {'update_id': 10034910, 'my_chat_member': {'chat': {'id': -4030904827, 'title': 'test2', 'type': 'group', 'all_members_are_administrators': True}, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'ko'}, 'date': 1704723237, 'old_chat_member': {'user': {'id': 6414831328, 'is_bot': True, 'first_name': 'photoCollector', 'username': 'my_photo_auto_collector_bot'}, 'status': 'member'}, 'new_chat_member': {'user': {'id': 6414831328, 'is_bot': True, 'first_name': 'photoCollector', 'username': 'my_photo_auto_collector_bot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': True, 'can_delete_messages': True, 'can_invite_users': True, 'can_restrict_members': True, 'can_pin_messages': True, 'can_promote_members': False, 'can_manage_video_chats': True, 'is_anonymous': False, 'can_manage_voice_chats': True}}}, {'update_id': 10034911, 'message': {'message_id': 21, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'ko'}, 'chat': {'id': -4030904827, 'title': 'test2', 'type': 'group', 'all_members_are_administrators': True}, 'date': 1704723246, 'text': 'Hihi'}}, {'update_id': 10034912, 'message': {'message_id': 22, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'en'}, 'chat': {'id': 1992250600, 'first_name': '로마 내돈돌려줘', 'type': 'private'}, 'date': 1704723510, 'text': '1'}}, {'update_id': 10034913, 'message': {'message_id': 23, 'from': {'id': 1992250600, 'is_bot': False, 'first_name': '로마 내돈돌려줘', 'language_code': 'en'}, 'chat': {'id': -4030904827, 'title': 'test2', 'type': 'group', 'all_members_are_administrators': True}, 'date': 1704725158, 'photo': [{'file_id': 'AgACAgUAAxkBAAMXZZwKpsIiQ5mclUkidbyJC07HCmQAAo27MRsaxdlUErt5WSTI-W0BAAMCAANzAAM0BA', 'file_unique_id': 'AQADjbsxGxrF2VR4', 'file_size': 802, 'width': 90, 'height': 67}, {'file_id': 'AgACAgUAAxkBAAMXZZwKpsIiQ5mclUkidbyJC07HCmQAAo27MRsaxdlUErt5WSTI-W0BAAMCAANtAAM0BA', 'file_unique_id': 'AQADjbsxGxrF2VRy', 'file_size': 17984, 'width': 320, 'height': 240}, {'file_id': 'AgACAgUAAxkBAAMXZZwKpsIiQ5mclUkidbyJC07HCmQAAo27MRsaxdlUErt5WSTI-W0BAAMCAAN4AAM0BA', 'file_unique_id': 'AQADjbsxGxrF2VR9', 'file_size': 113762, 'width': 800, 'height': 600}, {'file_id': 'AgACAgUAAxkBAAMXZZwKpsIiQ5mclUkidbyJC07HCmQAAo27MRsaxdlUErt5WSTI-W0BAAMCAAN5AAM0BA', 'file_unique_id': 'AQADjbsxGxrF2VR-', 'file_size': 216146, 'width': 1280, 'height': 960}]}}]

if __name__ == '__main__':
    # telegram.check_telegram_info(-4030904827)
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
            file_id = media[0]['file_id']
            tp = {update_id, message_id, chat_id, file_id}
            print(f"tp:{tp}")
        elif 'video' in message:
            media = message['video']
            file_id = media[0]['file_id']
            tp = {update_id, message_id, chat_id, file_id}
            print(f"tp:{tp}")
