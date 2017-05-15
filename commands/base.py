import re

class CommandBase:

    def remove_prefix(self, msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg
