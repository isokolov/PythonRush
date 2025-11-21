# Генетический алгоритм

# Найдите оптимальное решение заданной функции с использованием генетического алгоритма.
# Подсказка:
# 1) Инициализируйте популяцию случайными значениями.
# 2) Оцените каждое решение с помощью функции приспособленности.
# 3) Используйте турнирный отбор для выбора родителей.
# 4) Создавайте потомков через кроссовер и мутацию.
# 5) Повторите процесс для заданного числа поколений.


import random
import numpy as np

# Параметры генетического алгоритма
POPULATION_SIZE = 100
NUM_GENERATIONS = 500
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.01

# Пример функции приспособленности (максимизация функции)
def fitness_function(individual):
    return sum(individual)

# Инициализация популяции
def initialize_population(pop_size, chromosome_length):
# Напишите тут ваш код

# Турнирный отбор
def tournament_selection(population, fitnesses):
# Напишите тут ваш код

# Однточечный кроссовер
def crossover(parent1, parent2):
# Напишите тут ваш код

# Мутация
def mutate(individual):
# Напишите тут ваш код

# Основной цикл генетического алгоритма
def genetic_algorithm():
    chromosome_length = 10
    population = initialize_population(POPULATION_SIZE, chromosome_length)

    for generation in range(NUM_GENERATIONS):
        fitnesses = [fitness_function(ind) for ind in population]
        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    # Оптимальное решение
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)

# Вызов алгоритма
best_individual, best_fitness = genetic_algorithm()
print("Лучший индивидуум:", best_individual)
print("Функция приспособленности:", best_fitness)
