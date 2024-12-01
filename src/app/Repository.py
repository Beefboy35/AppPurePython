from abc import ABC, abstractmethod

from src.utils.utils import verify_date

todo_id = 1  # Уникальный идентификатор задания


class BaseRepository(ABC):  # Абстрактный класс наследующийся от ABC, в нем объявляем все наши методы
    @abstractmethod
    def get_all_todos(self, db: list):
        pass

    @abstractmethod
    def get_todos_by_category(self, category: str, db: list):
        pass

    @abstractmethod
    def create_new_todo(self, data: dict, db: list):
        pass

    @abstractmethod
    def update_todo(self, data: dict, id: int, db: list):
        pass

    @abstractmethod
    def delete_todo(self, id: int, db: list):
        pass

    @abstractmethod
    def search_todo_by_status(self, status: str, db: list):
        pass

    @abstractmethod
    def mark_todo_as_done(self, id: int, db: list):
        pass


class Repository(BaseRepository):  # Дочерний класс в котором прописывается основная логика, здесь уже определяем методы

    def get_all_todos(self, db: list):  # метод получения списка всех задач
        return db

    def get_todos_by_category(self, category, db: list):  # метод получения задач по категории
        todos_by_category = []
        for i in db:
            if i["category"] == category:
                todos_by_category.append(i)
        if not todos_by_category:
            return {"Status": "There is no such category"}
        return todos_by_category

    def create_new_todo(self, data: dict, db: list):  # метод для создания нового задания
        global todo_id  # объявляем уникальный идентификатор
        try:
            if data:
                data["due_date"] = verify_date(data["due_date"])
                data["id"] = todo_id
                db.append(data)
                todo_id += 1
                return {"Status": "Successfully added"}
        except Exception as e:
            return e

    def update_todo(self, data: dict, id: int, db: list):  # метод для обновления задания
        for i in db:
            if i["id"] == id:
                try:
                    i["title"] = data["title"]
                    i["description"] = data["description"]
                    i["category"] = data["category"]
                    i["due_date"] = verify_date(data["due_date"])
                    i["priority"] = data["priority"]
                    return {"Status": f"Task {i["id"]} successfully updated"}
                except Exception as e:
                    return e
        return {"Status": f"Task {id} was not updated"}

    def delete_todo(self, id: int, db: list):  # метод для удаления задания
        for i in db:
            if i["id"] == id:
                del db[id - 1]  # удаляем таск с айди id из бд (id - 1 тк индексы нумеруются с нуля)
                return {"Status": f"Task {id} deleted"}
        return {"Status": f"Task {id} not found"}

    def search_todo_by_status(self, status: str, db: list):  # метод для поиска задания по статусу
        todos_left = []
        for i in db:
            if i["status"] == status:
                todos_left.append(i)
        if not todos_left:
            return {"Error": "Not found"}
        return todos_left

    def mark_todo_as_done(self, id: int, db: list):  # метод для отметки заданий в качестве выполненных
        for i in db:
            if i["id"] == id:
                i["status"] = "done"
                return {"Status": f"Task {id} marked as done"}
        return {"Status": f"Task {id} not found"}
