class task:
    def __init__(self, task_id, title, description, status):
        self.id = task_id
        self.title = title
        self.desc = description
        self.status = status

    def __str__(self):
        return f'{self.id}, {self.title}, {self.desc}, {self.status}'
    

class task_manager:

    file_path = r'python_homeworks\lesson-7\homework\to_do.txt'

    def __init__(self):
        self.lines = []

    '''Add a New Task'''
    def add_task(self):
        task_id = max([int(line.id) for line in self.lines]) + 1 if self.lines else 101
        task_title = input('Enter title: ')
        task_desc = input('Enter description: ')
        task_status = input('Enter status(Pending/In Progress/Completed): ')

        self.lines.append(task(str(task_id), task_title, task_desc, task_status))

        print('Added successfully!')
    
    '''View All Tasks'''
    def view_all_tasks(self):
        if not self.lines:
            print('No task found.')
            return
        for line in self.lines:
            print(f'ID: {line.id}; Title: {line.title}; Description: {line.desc}; Status: {line.status}.')
    
    '''Update a Task'''
    def update(self):
        updated_id = input('Enter ID: ')
        for line in self.lines:
            if updated_id == line.id:
                line.title = input(f'Enter Title (current: {line.title}, leave blank to keep unchanged): ') or line.title
                line.desc = input(f'Enter Description (current: {line.desc}, leave blank to keep unchanged): ') or line.desc
                line.status = input(f'Enter Status (current: {line.status}, leave blank to keep unchanged): ') or line.status

                print('Updated successfully!')
                return
        print('Task not found.')

    '''Delete a Task'''
    def delete(self):
        deleted_id = input('Enter ID: ')
        self.lines = [line for line in self.lines if line.id != deleted_id]

        print('Deleted successfully!')
    
    '''Filter by Status'''
    def filter(self):
        filter_by = input('Enter Status to filter tasks by: ')
        if filter_by not in ['Pending', 'In Progress', 'Completed']:
            print('Invalid Status.')
        else:
            for line in self.lines:
                if line.status == filter_by:
                      print(f'ID: {line.id}; Title: {line.title}; Description: {line.desc}; Status: {line.status}.')

    '''Save tasks to a file'''
    def save(self):
        with open(self.file_path, 'w') as file:
             file.writelines(f'{line}\n' for line in self.lines)
    print('Saved successfully!')

    '''Load tasks from a file'''
    def load(self):
        try:
            with open(self.file_path) as file:
                self.lines = [task(*line.strip().split(', ')) for line in file.readlines()]
                print('Loaded successfully!')
        except FileNotFoundError:
            print('File not found. You can create one by typing.')

    def menu(self):
        while True:
            option = input('''You have the following options:
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
Your option: ''')
            if option == '1':
                self.add_task()
            elif option == '2':
                self.view_all_tasks()
            elif option == '3':
                self.update()
            elif option == '4':
                self.delete()
            elif option == '5':
                self.filter()
            elif option == '6':
                self.save()
            elif option == '7':
                self.load()
            elif option == '8':
                print('Good bye!')
                break
            else: print('Invalid option')

'''Run the Program'''
print('Welcome to the To-Do Application!')
program = task_manager()
program.menu()