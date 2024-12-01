from src.app import Repository
from src.database.db import Json, fake_db


def get_cmd(cmd: str, obj: Repository): # функция для обработки доступных команд
    fields = ["",
              "your title",
              "your description",
              "your category",
              "your due date (format: yyyy-mm-dd)",
              "your priority",
              "your status"
              ] # cписок ключевых слов для указания определенных полей для каждого задания
    if cmd == "create task":  # создаем новое задание
        data = {}
        for i in range(1, 7):
            payload = input(f'Enter {fields[i]}: ')
            data[list(Json.keys())[i]] = payload
        print(obj.create_new_todo(data, fake_db))

    elif cmd == "get all tasks":  # получаем список всех задач
        print(obj.get_all_todos(fake_db))
    elif cmd == "update task":  # обновляем задания по id
        id = int(input("Enter id of the task to update: "))
        data = {} # dвременный словарь
        for i in range(1, 6):
            payload = input(f'Enter {fields[i]}: ')
            data[list(Json.keys())[i]] = payload # добавляем данные в словарь по заранее определенному ключу, таким образом избегаем кучу ошибок от пользователя и упрощаем код
        print(obj.update_todo(data, id, fake_db))
    elif cmd == "get tasks by category":  # получаем задания по категории
        category = input("Enter your category: ")
        print(obj.get_todos_by_category(category, fake_db))
    elif cmd == "delete task":  # удаляем задание по id
        id = int(input("Enter id of the task to delete: "))
        print(obj.delete_todo(id, fake_db))
    elif cmd == "get tasks by status":  # получаем задания по статусу
        status = input("Specify your status: ")
        print(obj.search_todo_by_status(status, fake_db))
    elif cmd == "cross out task":  # помечаем задания как выполненное
        id = int(input("Enter id of the task: "))
        print(obj.mark_todo_as_done(id, fake_db))
    else:
        print({"Error": f"Command {cmd} doesn't exist"})  # симулируем выброс ошибки об отсутствии команды
        print({"Detail": "Use commands only from the list"})