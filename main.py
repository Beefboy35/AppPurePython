from src.app.Repository import Repository # подход с репозиторием позволит легко расширить проект в будущем
from src.app.app import get_cmd



if __name__ == "__main__":  # после остановки программы бд автоматически отчищается!!!
    obj = Repository()  # создаем обьект нашего репозитория для работы с его методами
    print("Hello! Via this application you can interact with the database")
    while True:
        print(
            "List of available commands: create task, get all tasks, get tasks by category, update task, delete task, get tasks by status, cross out task")
        print("if you want to leave enter 'stop'")
        cmd = input("Enter the command: ")
        if cmd == "stop":  # останавливаем программу
            print("Have a good day!")
            break
        else:
            get_cmd(cmd, obj)

