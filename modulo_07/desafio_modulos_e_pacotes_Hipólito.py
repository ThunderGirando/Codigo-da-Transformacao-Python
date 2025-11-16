import json
import csv
import datetime
import math
import random
import os


class TaskManager:
    def __init__(self, storage_file='modulo_07/tasks.json'):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.tasks, f, indent=4, default=str)

    def add_task(self, title, description, due_date):
        task = {
            'id': random.randint(1000, 9999),
            'title': title,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, completed=None):
        if completed is None:
            return self.tasks
        return [t for t in self.tasks if t['completed'] == completed]

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                return True
        return False

    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()

    def get_stats(self):
        total = len(self.tasks)
        completed = len(self.list_tasks(completed=True))
        if total > 0:
            percentage = math.ceil((completed / total) * 100)
        else:
            percentage = 0
        return {'total': total, 'completed': completed, 'percentage': percentage}

# Módulo de relatórios
class ReportGenerator:
    def __init__(self, task_manager):
        self.tm = task_manager

    def export_to_csv(self, filename='tasks_report.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Título', 'Descrição', 'Data de Vencimento', 'Concluída'])
            for task in self.tm.tasks:
                writer.writerow([task['id'], task['title'], task['description'], task['due_date'], task['completed']])

# Interface de usuário simples
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    tm = TaskManager()
    rg = ReportGenerator(tm)

    while True:
        clear_screen()
        print("Gerenciador de Tarefas Pessoal")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas pendentes")
        print("3. Listar tarefas concluídas")
        print("4. Marcar tarefa como concluída")
        print("5. Remover tarefa")
        print("6. Ver estatísticas")
        print("7. Exportar relatório CSV")
        print("8. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            title = input("Título: ")
            description = input("Descrição: ")
            due_date_str = input("Data de vencimento (DD/MM/YYYY): ")
            try:
                due_date = datetime.datetime.strptime(due_date_str, '%d/%m/%Y').date()
                tm.add_task(title, description, due_date)
                print("Tarefa adicionada!")
            except ValueError:
                print("Data inválida!")
        elif choice == '2':
            tasks = tm.list_tasks(completed=False)
            if not tasks:
                print("Nenhuma tarefa pendente.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t['title']} - {t['due_date']}")
        elif choice == '3':
            tasks = tm.list_tasks(completed=True)
            if not tasks:
                print("Nenhuma tarefa concluída.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t['title']} - {t['due_date']}")
        elif choice == '4':
            tasks = tm.list_tasks(completed=False)
            if not tasks:
                print("Nenhuma tarefa pendente para marcar.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t['title']} - {t['due_date']}")
                num = int(input("Número da tarefa a marcar como concluída: "))
                if 1 <= num <= len(tasks):
                    task_id = tasks[num-1]['id']
                    tm.mark_completed(task_id)
                    print("Tarefa marcada como concluída!")
                else:
                    print("Número inválido!")
        elif choice == '5':
            tasks = tm.list_tasks()
            if not tasks:
                print("Nenhuma tarefa para remover.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "Concluída" if t['completed'] else "Pendente"
                    print(f"{i}. {t['title']} - {t['due_date']} ({status})")
                num = int(input("Número da tarefa a remover: "))
                if 1 <= num <= len(tasks):
                    task_id = tasks[num-1]['id']
                    tm.remove_task(task_id)
                    print("Tarefa removida!")
                else:
                    print("Número inválido!")
        elif choice == '6':
            stats = tm.get_stats()
            print(f"Total: {stats['total']}, Concluídas: {stats['completed']}, Porcentagem: {stats['percentage']}%")
        elif choice == '7':
            rg.export_to_csv()
            print("Relatório exportado para tasks_report.csv!")
        elif choice == '8':
            break
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
