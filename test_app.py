test_db = []  # аналог тестовой базы данных
from src.app.Repository import Repository

test_obj = Repository() # временный обьект репозитория


class TestApp:
    """Для запуска всех тестов введите в терминале pytest.
    Для запуска конкретного теста введите в терминале pytest <Модуль где тесты>::<Класс теста>::<Название метода теста>.
    Пример: pytest test_mod.py::TestClass::test_method"""
    test_data = {"title": "my title",
                 "description": "description",
                 "category": "test",
                 "due_date": "2024-10-14",
                 "priority": "important",
                 "status": "status"} # можно поиграть с входящими данными и сделать их невалидными (Например: ввести некорректную дату или изменить категорию)

    def test_create_task(self):
        assert test_obj.create_new_todo(self.test_data, test_db) == {"Status": "Successfully added"}

    def test_update_task(self):
        assert test_obj.update_todo(self.test_data, 1, test_db) == {"Status": f"Task 1 successfully updated"}  # обновляем таск с айди 1

    def test_get_tasks_by_category(self):
        assert test_obj.get_todos_by_category("test", test_db) != {"Status": "There is no such category"} # ищем таски с категорией "test"

    def test_get_task_by_status(self):
        assert test_obj.search_todo_by_status("status", test_db) != {"Error": "Not found"} # ищем таски с статусом "status"

    def test_cross_out_task(self):
        assert test_obj.mark_todo_as_done(1, test_db) == {"Status": "Task 1 marked as done"} # помечаем таск с айди 1 как выполненное

    def test_delete_task(self):
        assert test_obj.delete_todo(1, test_db) == {"Status": "Task 1 deleted"} # удаляем таск с айди 1



