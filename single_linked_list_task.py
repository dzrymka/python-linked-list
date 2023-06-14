class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)

        if self.head is None:
            self.head = new_task
        else:
            current_task = self.head
            if current_task.priority < priority:
                new_task.next = current_task
                self.head = new_task
            else:
                while (
                    current_task.next is not None
                    and current_task.next.priority >= priority
                ):
                    current_task = current_task.next
                new_task.next = current_task.next
                current_task.next = new_task

        print(
            "Tugas '{}' dengan prioritas {} telah ditambahkan.".format(
                description, priority
            )
        )

    def remove_task(self, description):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        if self.head.description == description:
            self.head = self.head.next
            print("Tugas '{}' telah dihapus.".format(description))
            return

        current_task = self.head
        while (
            current_task.next is not None
            and current_task.next.description != description
        ):
            current_task = current_task.next

        if current_task.next is None:
            print("Tugas '{}' tidak ditemukan.".format(description))
        else:
            current_task.next = current_task.next.next
            print("Tugas '{}' telah dihapus.".format(description))

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
        else:
            current_task = self.head
            print("Daftar Tugas:")
            print("-------------")
            while current_task is not None:
                print(
                    "Deskripsi: {}, Prioritas: {}".format(
                        current_task.description, current_task.priority
                    )
                )
                current_task = current_task.next
            print("-------------")


task_list = TaskList()

task_list.add_task("Belajar Linked List", 2)
task_list.add_task("Mengerjakan Tugas", 1)
task_list.add_task("Membuat Akun Github", 3)

task_list.print_tasks()

task_list.remove_task("Mengerjakan Tugas")

task_list.print_tasks()
