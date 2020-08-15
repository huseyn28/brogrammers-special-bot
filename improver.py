from constants import FN_CONFIRM_BRO


def improve_confirm_bro(args:list):
    new_text = "\n" + " ".join(args)
    file = open(FN_CONFIRM_BRO,"a")
    file.write(new_text)
    file.close()
