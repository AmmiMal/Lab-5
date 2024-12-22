import re
import csv

FILE1 = 'task1-ru.txt'
FILE2 = 'task2.html'
FILE3 = 'task3.txt'
ADD_FILE = 'task_add.txt'


def task1():
    with open(FILE1, 'r', encoding='utf-8') as file:
        read_file = file.read()
        print(re.findall(r'рис. [0-9]+—[0-9]+|рис. [0-9]+', read_file))
        print(re.findall(r'\b[А-Яа-я]{4}\b', read_file))
        print()


def task2():
    with open(FILE2, 'r', encoding='utf-8') as html_file:
        read_file = html_file.read()
        res = re.findall(r'(font-style: \w+;)(\s*font-size: \w+)', read_file)
        for i in res:
            print(f"{i[0]} {i[1].lstrip()}")
        print()


def task3():
    with open(FILE3, 'r', encoding='utf-8') as file:
        read_file = file.read().replace('\n', ' ')

        surnames = re.findall(r'[A-Z][a-z]+', read_file)
        emails = re.findall(r'\w*@[0-9a-z-]+\.[a-z]{2,}', read_file)
        date = re.findall(r'\d{4}-\d{2}-\d{2}', read_file)
        site = re.findall(r'https?://[A-Za-z0-9.-]+/', read_file)

    with open('task3.csv', 'w', newline='') as f:
        file = csv.writer(f, delimiter=';')
        file.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Site'])
        for i in range(len(surnames)):
            file.writerow([i, surnames[i], emails[i], date[i], site[i]])


def extra_task():
    with open(ADD_FILE, 'r', encoding='utf-8') as html_file:
        read_file = html_file.read()
        dates = re.findall(r'\d{2,4}[-/.]\d{2,4}[-/.]\d{2,4}', read_file)
        emails = re.findall(r'\s[\w.-_]+@[0-9a-z-]+\.[a-z]{2,}', read_file)
        sites = re.findall(r'\shttps?://[A-Za-z0-9.-]+', read_file)
        print('\t'.join(dates), ' '.join(emails), ' '.join(sites), sep='\n')


if __name__ == '__main__':
    task1()
    task2()
    task3()
    extra_task()