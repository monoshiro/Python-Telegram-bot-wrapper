__author__ = 'Mono'

BOT_TOKEN = 'bot' + 'TOKEN_GOES HERE'
BASE_URL = 'https://api.telegram.org/' + BOT_TOKEN

BOT_REQUEST = dict(
    forward_message='/forwardMessage',
    get_chat='/getChat',                                #
    get_file='/getFile',                                #
    get_me='/getMe',                                    #
    get_updates='/getUpdates',                          #
    get_user_profile_photos='/getUserProfilePhotos',    #
    send_audio='/sendAudio',                            #
    send_chat_action='/sendChatAction',                 #
    send_contact='/sendContact',                        #
    send_doc='/sendDocument',                           #
    send_location='/sendLocation',                      #
    send_photo='/sendPhoto',                            #
    send_sticker='/sendSticker',                        #
    send_text='/sendMessage',                           #
    send_venue='/sendVenue',                            #
    send_video='/sendVideo',                            #
    send_voice='/sendVoice',
)

