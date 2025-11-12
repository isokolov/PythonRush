# Использование многопроцессорности

# Напишите программу, которая создает 4 параллельных процесса.
# Каждый процесс должен печатать свое имя и текущий идентификатор процесса.
# Используйте модуль multiprocessing.

# Напишите тут ваш код
import multiprocessing as mp
import os

def worker(num):
    proc = mp.current_process()
    print(f"Worker arg: {num} | name: {proc.name} | pid: {os.getpid()}")

def main():
    processes = []
    for i in range(4):
        p = mp.Process(target=worker, args=(i,), name=f"Worker-{i}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()

