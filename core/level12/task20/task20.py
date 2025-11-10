# Исключение несериализуемых полей

# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),
# чтобы исключить эти поля при сериализации и восстановить их при десериализации.

# Напишите тут ваш код
# Write your code here
import pickle
import sqlite3


class CustomClass:
    def __init__(self, file_path: str, db_dsn: str):
        self.file_path = file_path
        self.db_dsn = db_dsn
        self.file_handle = open(self.file_path, "a", encoding="utf-8")
        self.db_conn = sqlite3.connect(self.db_dsn)

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop('file_handle', None)
        state.pop('db_conn', None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        try:
            self.file_handle = open(self.file_path, "a", encoding="utf-8")
        except FileNotFoundError:
            self.file_handle = None
        try:
            self.db_conn = sqlite3.connect(self.db_dsn)
        except sqlite3.Error:
            self.db_conn = None

    def close(self):
        fh = getattr(self, "file_handle", None)
        if fh:
            try: fh.close()
            except FileNotFoundError: pass
        conn = getattr(self, "db_conn", None)
        if conn:
            try: conn.close()
            except sqlite3.Error: pass

    def __repr__(self):
        return (f"CustomClass(file_path={self.file_path!r}, db_dsn={self.db_dsn!r}, "
                f"file_handle_open={bool(getattr(self, 'file_handle', None))}, "
                f"db_conn_open={bool(getattr(self, 'db_conn', None))}")


obj = CustomClass("example.txt", ":memory:")
data = pickle.dumps(obj)
obj.close()
new = pickle.loads(data)
print(new)
obj.close()
