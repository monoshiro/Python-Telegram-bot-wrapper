__author__ = 'Mono'

import SETTING
import inspect
import requests

class Bot():
    def __init__(self):
        self.message_offset = 0

    def forward_message(self, chat_id, src, message_id, **kwargs):
        """
        Forward messages of any kind
        :param chat_id:
        :param src:
        :param message_id:
        :param kwargs:
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['from_chat_id'] = src
        data['message_id'] = message_id
        data.update(kwargs)

        req = requests.post(req_str, data=data)
        return req.json()

    def get_chat(self, chat_id):
        """

        :param chat_id:
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]
        data = dict()
        data['chat_id'] = chat_id

        req = requests.post(req_str, data=data)
        return req.json()

    def get_file(self, file_id):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['file_id'] = file_id

        req = requests.post(req_str, data=data)
        return req.json()

    def get_me(self):
        """
        Returns basic information about the bot in form of a User object.
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        req = requests.get(req_str)
        return req.json()

    def get_updates(self, **kwargs):
        """
        An Array of Update objects is returned.
        :param kwargs:
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        if kwargs.get('offset', None) is not None: data['offset'] = kwargs.pop('offset')
        if kwargs.get('limit', None) is not None: data['limit'] = kwargs.pop('limit')
        if kwargs.get('timeout', None) is not None: data['timeout'] = kwargs.pop('timeout')

        req = requests.post(req_str, data=data)
        data = req.json()

        if data['ok'] is True:
            self.update_offset(data['result'])

        return data

    def get_user_profile_photos(self, user_id, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['user_id'] = user_id

        if kwargs.get('offset', None) is not None: data['offset'] = kwargs.pop('offset')
        if kwargs.get('limit', None) is not None: data['offset'] = kwargs.pop('limit')

        req = requests.post(req_str, data=data)
        return req.json()

    def send_audio(self, chat_id, audio, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        if kwargs.get('duration', None) is not None: data['duration'] = kwargs.pop('duration')
        if kwargs.get('performer', None) is not None: data['performer'] = kwargs.pop('performer')
        if kwargs.get('title', None) is not None: data['title'] = kwargs.pop('title')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        with open(audio, 'rb') as file:
            files = {'audio': (file.name, file, 'audio/mpeg')}
            req = requests.post(req_str, files=files, data=data)
            return req.json()

    def send_contact(self, chat_id, phone_number, first_name, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['phone_number'] = phone_number
        data['first_name'] = first_name
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        req = requests.post(req_str, data=data)
        return req.json()

    def send_chat_action(self, chat_id, action):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['action'] = action

        req = requests.post(req_str, data=data)
        return req.json()

    def send_doc(self, chat_id, doc, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        if kwargs.get('caption', None) is not None: data['caption'] = kwargs.pop('caption')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        with open(doc, 'rb') as file:
            files = {'document': (file.name, file, 'application/octet-stream')}
            req = requests.post(req_str, files=files, data=data)
            return req.json()

    def send_location(self, chat_id, latitude, longitude, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['latitude'] = latitude
        data['longitude'] = longitude
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        req = requests.post(req_str, data=data)
        return req.json()

    def send_photo(self, chat_id, photo, **kwargs):
        """

        :param chat_id:
        :param photo:
        :param kwargs:
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        if kwargs.get('caption', None) is not None: data['caption'] = kwargs.pop('caption')
        if kwargs.get('no_preview', None) is not None: data['disable_web_page_preview'] = kwargs.pop('no_preview')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        with open(photo, 'rb') as file:
            files = {'photo': (file.name, file, 'image/jpeg')}
            req = requests.post(req_str, files=files, data=data)
            return req.json()

    def send_sticker(self, chat_id, sticker, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        with open(sticker, 'rb') as file:
            files = {'sticker': (file.name, file, 'image/webp')}
            req = requests.post(req_str, files=files, data=data)
            return req.json()

    def send_text(self, chat_id, text, **kwargs):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        :param chat_id:
            string / int:   The chat to send the message to
        :param text:
            string:         The text to send
        :param kwargs:
            parse_mode:
                string:     Either 'Markdown' or 'HTML'
            disable_web_page_preview:
                boolean:     Disables link previews for links in this message
            disable_notification:
                boolean:    Sends the message silently. iOS users will not receive a notification, Android users will receive a
                            notification with no sound.
            reply_to_message_id:
                int:        id of the message to reply to
            reply_markup:
                InlineKeyboardMarkup/
                ReplyKeyBoardMarkup/
                ReplyKeyboardHide/
                ForceReply: Additional interface options
        :return:
        """
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['text'] = text
        if kwargs.get('parse_mode', None) is not None: data['parse_mode'] = kwargs.pop('parse_mode')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        req = requests.post(req_str, data=data)
        return req.json()

    def send_venue(self, chat_id, latitude, longitude, title, address, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        data['latitude'] = latitude
        data['longitude'] = longitude
        data['title'] = title
        data['address'] = address
        if kwargs.get('foursquare_id', None) is not None: data['foursquare_id'] = kwargs.pop('foursquare_id')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        req = requests.post(req_str, data=data)
        return req.json()

    def send_video(self, chat_id, video, **kwargs):
        req_str = SETTING.BASE_URL + SETTING.BOT_REQUEST[inspect.currentframe().f_code.co_name]

        data = dict()
        data['chat_id'] = chat_id
        if kwargs.get('duration', None) is not None: data['duration'] = kwargs.pop('duration')
        if kwargs.get('width', None) is not None: data['width'] = kwargs.pop('width')
        if kwargs.get('height', None) is not None: data['height'] = kwargs.pop('height')
        if kwargs.get('caption', None) is not None: data['caption'] = kwargs.pop('caption')
        if kwargs.get('no_preview', None) is not None: data['disable_web_page_preview'] = kwargs.pop('no_preview')
        if kwargs.get('no_notif', None) is not None: data['disable_notification'] = kwargs.pop('no_notif')
        if kwargs.get('reply_to', None) is not None: data['reply_to_message_id'] = kwargs.pop('reply_to')
        if kwargs.get('markup', None) is not None: data['reply_markup'] = kwargs.pop('markup')

        with open(video, 'rb') as file:
            files = {'video': (file.name, file, 'video/mp4')}
            req = requests.post(req_str, files=files, data=data)
            return req.json()

    def update_offset(self, messages):
        for message in messages:
            if message['update_id'] >= self.message_offset:
                self.message_offset = messages[len(messages) - 1]['update_id'] + 1
