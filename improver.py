from constants import FN_CONFIRM_BRO, FN_MUSIC
from services import file_service
from interceptors import logger_interceptor


@logger_interceptor
def improve_confirm_bro(args:list):
    new_text = "\n" + " ".join(args)
    file_service.write_to_file(FN_CONFIRM_BRO, new_text)


@logger_interceptor
def improve_music(args:list):
    if not check_link_unique(args[0]):
        return False
    new_text = "\n" + args[0]
    file_service.write_to_file(FN_MUSIC, new_text)
    return True


@logger_interceptor
def check_link_unique(link:str):
    if '?' in link:
        video_id = link.split('?')[1].split('=')[1]
        if '&' in video_id:
            video_id = video_id.split('&')[0]
    else:
        temp = link.split('/')
        video_id = temp[len(temp)-1]

    list_messages = file_service.get_message_from_file(FN_MUSIC)
    for l in list_messages:
        if video_id in l:
            return False
    return True

