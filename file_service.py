def write_to_file(file_name:str,new_text:str):
    file = open(file_name, "a")
    file.write(new_text)
    file.close()


def get_message_from_file(file_name:str):
    file = open(file_name, "r")
    listMessages = file.readlines()
    file.close()
    return listMessages
