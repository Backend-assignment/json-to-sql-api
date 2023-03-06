from tinydb import TinyDB, Query

class SmartPhoneDB:
    def __init__(self) -> None:
        self.db = TinyDB('db.json')

    def get_tables(self):
        return self.db.tables()
    
    def get_all(self, table_name):
        return self.db.table(table_name).all()