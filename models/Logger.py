from datetime import datetime


class Logger(object):

    start_log_text = "{} method started. Start time : {}"
    finish_log_text = "{} method finished. Finish time : {}"

    def __init__(self, method_name: str):
        self.method_name = method_name

    def start_log(self):
        now = datetime.now()
        print(self.start_log_text.format(self.method_name,now.strftime("%d/%m/%Y %H:%M:%S")))

    def finish_log(self):
        now = datetime.now()
        print(self.finish_log_text.format(self.method_name,now.strftime("%d/%m/%Y %H:%M:%S")))
