# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv
import sys

data = open("data.csv")


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    return count_different_values_by_column_name('nationality')

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    return count_different_values_by_column_name('club')

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    names = []
    lines = csv.DictReader(data)
    i = 1
    for line in lines:
        if i > 20:
            break
        first_name = line['full_name'].split(' ')[0]
        names.append(first_name)
        i += 1
    return names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    return build_top_10_by_value('eur_wage')

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    return build_top_10_by_value('age')

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    count_age = {}
    lines = csv.DictReader(data)
    for line in lines:
        age = line['age']
        if age not in count_age:
            count_age[age] = 1
        count_age[age] += 1
    return count_age

def count_different_values_by_column_name(column_name:str):
    values = []
    lines = csv.DictReader(data)
    for line in lines:
        if line[column_name] not in values:
            values.append(line[column_name])
    return len(values)

def build_top_10_by_value(value: str):
    name_value = {}
    lines = csv.DictReader(data)
    for line in lines:
        name_value[line['full_name']] = float(line[value])

    top_10 = []
    i = 1
    for key, value in sorted(name_value.items(), key=lambda item: (item[1], item[0]), reverse=True):
        if i > 10:
            break
        top_10.append(key)
        i += 1

    return top_10


q_1()