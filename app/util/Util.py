from datetime import datetime

class Util:
    def formatar_data(self, data: datetime):
        return data.strftime("%Y-%m-%d %H:%M:%S")