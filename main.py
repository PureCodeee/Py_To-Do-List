version = 0.0003
print(f'To-Do List alpha version {version}')

def add_task(task):
    with open('tasks.txt', 'a', encoding='utf-8') as file:
            file.write(f'{task}\n')

def read_tasks():
    print('Список задач:')
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            tasks = file.readlines()

        if not tasks:
            print('Список задач пуст!')
            return

        for i, task in enumerate(tasks, 1):
            task = task.strip()
            if task:
                print(f'{i}. {task}')

    except FileNotFoundError:
        print('Список задач пуст!')

def delete_task(number):
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        
        if not tasks:
            print('Список задач пуст!')
            return
        
        index = int(number) - 1

        if 0 <= index < len(tasks):
            removed_task = tasks[index].strip()

            del tasks[index]

            with open('tasks.txt', 'w', encoding='utf-8') as file:
                 file.writelines(tasks)
            print(f'Задача {number}. "{removed_task}" удалена!')
        else:
            print('неверный номер задачи!')
        
    except ValueError:
         print('Пожалуйста введите число')
    except Exception as e:
         print(f'Ошибка при удалении: {e}')

def delete_all_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as file:
         pass
    print('Все задачи удалены!')

def edit_task():
     try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        read_tasks()
        print('Выберите задачу для редактирования')
        index = int(input()) - 1
        if 0 <= index < len(tasks):
            old_task = tasks[index].strip()
            print(f'Редактировать задачу "{old_task}"')
            print('Введите новый текст задачи')
            new_task = input()
            tasks[index] = new_task + '\n'

            with open('tasks.txt', 'w', encoding='utf-8') as file:
                file.writelines(tasks)
            
            print(f'Задача изменена с "{old_task}" на "{new_task}"')
        else:
            print('Неверный номер задачи!')

     except ValueError:
         print('Пожалуйста, введите число!')
def menu():
     print('')
     print('1. П0смотреть задачи')
     print('2. Д0бавить задачу')
     print('3. Удалить задачу')
     print('4. Редактировать задачу')
     print('5. Удалить все задачи')
     print('6. Выйти\n')


while True:

    menu()

    choice = input('')
    print()

    if choice == '6':
         break

    elif choice == '1':
         read_tasks()

    elif choice == '2':
         print('Введите новую задачу:')
         new_task = input()
         add_task(new_task)
         print(f'Задача "{new_task}" добавлена!')

    elif choice == '3':
         print('Выберите задачу для удаления:')
         read_tasks()
         number = input()
         delete_task(number)

    elif choice == '4':
        edit_task()

    elif choice == '5':
         accept = input('Вы действительно хотите удалить все задачи?(да/нет)\n')
         if accept == 'да':
             delete_all_tasks()