# Генетический рюкзак

# Оптимизировать задачу о рюкзаке с использованием генетического алгоритма.
# 1) Инициализируйте популяцию случайными значениями.
# 2) Оцените каждое решение с помощью функции приспособленности, учитывая ограничения по весу.
# 3) Используйте турнирный отбор для выбора родителей.
# 4) Создавайте потомков через кроссовер и мутацию.
# 5) Повторите процесс для заданного числа поколений.

import random

# Условие задачи
weights = [2, 3, 4, 5, 9]
values = [3, 4, 8, 8, 10]
capacity = 20
population_size = 10
generations = 100
mutation_rate = 0.1
tournament_size = 3

# Генерация начальной популяции
def generate_individual(length):
# Напишите тут ваш код

def generate_population(size, length):
# Напишите тут ваш код

# Функция приспособленности
def fitness(individual):
# Напишите тут ваш код

# Турнирный отбор
def tournament_selection(population):
# Напишите тут ваш код

# Кроссовер
def crossover(parent1, parent2):
# Напишите тут ваш код

# Мутация
def mutate(individual):
# Напишите тут ваш код

# Главный цикл генетического алгоритма
def genetic_algorithm():
    population = generate_population(population_size, len(weights))
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
        best_individual = max(population, key=fitness)
        print(f"Generation {generation}: Best individual = {best_individual}, Fitness = {fitness(best_individual)}")
    return best_individual

best_solution = genetic_algorithm()
print("Best solution found:", best_solution)
print("Total value:", fitness(best_solution))
