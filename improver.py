from constants import FN_CONFIRM_BRO, FN_MUSIC


def improve_confirm_bro(args:list):
    new_text = "\n" + " ".join(args)
    file = open(FN_CONFIRM_BRO,"a")
    file.write(new_text)
    file.close()


def improve_music(args:list):
    new_text = "\n" + " ".join(args)
    file = open(FN_MUSIC,"a")
    file.write(new_text)
    file.close()
