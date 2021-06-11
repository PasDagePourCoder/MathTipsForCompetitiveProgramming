"""
Demonstrations that mathematics is really useful when coding competiting.
"""
import string
import numpy as np


# 1. Somme géométrique
total_sum = 0
n = 20
q = 3

for k in range(0, n + 1):
    total_sum += 3 ** k








# 1. Formule Mathématique
result_somme_geometrique = (1 - q**(n+1)) / (1 - q)



# Mathematics, others formula

result = n * (n + 1) / 2

# Sum the number of square

result_square = n * (n + 1) * (2 * n + 1) / 6





#2. Congruence

# La planete Vegeta a une periode de revolution de 15 jours autour de la Terre, elle est visible seulement au 6ème jour de sa révolution
# La planete Namek a une periode de revolution de 7 jours autour de la Terre, elle est visible seulement au 5ème jour

# Quand les deux planetes seront-elles visibles ensemble ?

vegeta = range(1, 16)
namek = range(1, 8)

from itertools import cycle

cycle_vegeta = cycle(vegeta)  # Creation of a cycle
cycle_namek = cycle(namek)

condition_not_met = True
# Cycle
number_days = 1
while condition_not_met:
    day_vegeta = next(cycle_vegeta)
    day_namek = next(cycle_namek)

    if day_vegeta == 6 and day_namek == 5:
        break

    number_days += 1












# 3. Trouver ci deux couples sont dans le même ensemble
# Comment créer un nouvel ID, sans pour autant casser la mémoire
user_id_1 = 1234564
user_id_2 = 2356458

relation = {'user': user_id_1, 'follower': user_id_2}

3 + 4
5 + 2
id_relation = str(user_id_1) + str(user_id_2)








def bijection_n_2_to_n(i: int, j: int):
    return int((i + j) * (i + j + 1) * 0.5 + j)


number_biject = bijection_n_2_to_n(57, 86)
number_biject_2 = bijection_n_2_to_n(86, 57)








# 4. Coins flipped

# Imagine you throw multiple times a random coins n = 20, the probability of even is 0.3
# What is the exact number of times, we get the 10
import random

n = 20
p = 0.3
number_trials = 1000
list_result = []
for trial in range(number_trials):
    nb_times_even = 0
    for i in range(n):
        result_coin = random.randint(a=1, b=10)
        if result_coin <= 3:
            nb_times_even += 1
    list_result.append(nb_times_even)

probability_10 = list_result.count(10) / len(list_result)


# Mathematics
from scipy.stats import binom

exact_result = binom.pmf(k=10, n=n, p=p)


# 5. On cherche à montrer que deux phrases sont équivalentes

sentence_1 = "question sans reponsea "
sentence_2 = "enquetons sans espoir"

dict_letters = {l: 0 for l in 'abcdefghijklmnopqrstuvwxyz '}
for letter in sentence_1:
    if letter != ' ':
        score_letter = dict_letters[letter]
        dict_letters.update({letter: score_letter + 1})

for letter in sentence_2:
    if letter != ' ':
        score_letter = dict_letters[letter]
        dict_letters.update({letter: score_letter - 1})

for k, v in dict_letters.items():
    if v != 0:
        print('This is not an anagramme.')








# Solution avec le theoreme fondamental de l'arithmetique

nombre_premiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def compute_product_sentence(sentence: str):
    """
    Compute the sentence.
    :param sentence:
    :return:
    """
    result_product = 1
    for letter in sentence:
        if letter != ' ':
            position_alphabet = string.ascii_lowercase.index(letter)
            result_product *= nombre_premiers[position_alphabet]
    return result_product


result_product_1 = compute_product_sentence(sentence_1)
result_product_2 = compute_product_sentence(sentence_2)








# 6. Suite arithmetico-geometrique
# Quel est la valeur de u_100 sachant que
u_n = 1
u_n_plus_1 = u_n * 5 + 3
N = 100

u_k = 1
for k in range(10):
    u_k_plus_1 = u_k * 5 + 3
    u_k = u_k_plus_1









# Mathematics

# r = b / (1 - a)
r = 3 / (1 - 5)
# u_n = a ** n * (u_0 - r) + r

result_suite_arithmetico_geometrique = 5 ** 10 * (1 - r) + r












# 7. Piece truquee esperance
p = 0.15  # Obtenir face (piece truque)
r = 2  # Nombre succes
# On compte le nombre d'echecs avant d'obtenir le premier face, calculer le nombre
# En moyenne, au bout de lancer, il y aura-t-il le premier succes ?
nombre_lancers_liste = []

from scipy.stats import bernoulli
for i in range(100000):
    nombre_lancer = 0
    while True:
        tirage = random.randint(a=1, b=100)
        if tirage <= 15:
            break  # On obtient face

        nombre_lancer += 1

    nombre_lancers_liste.append(nombre_lancer)

result_proba_binomiale_negative = np.mean(nombre_lancers_liste)





# Mathematics
# E(X) = (1 - p) / p
result_formula_binomiale_negative = (1 - p) / p


# 8. Monty Hall
portes_initiales = ['chevre', 'chevre', 'ferrari']

number_trials_monty_python = 10000
counter_success = 0
counter_success_no_changing = 0


for _ in range(number_trials_monty_python):
    portes = random.sample(portes_initiales, 3)
    index_ferrari = portes.index('ferrari')

    index_portes = [0, 1, 2]
    choices_final = [0, 1, 2]

    index_porte_initial = random.randint(a=0, b=2)  # La personne selectionne une porte

    index_portes.remove(index_porte_initial)  #
    if index_ferrari in index_portes:
        index_portes.remove(index_ferrari)
    index_presentateur = random.sample(index_portes, 1)[0]  # The anchorman pick a door which is not
    # print("The presentateur display the door number {} which is a {}".format(index_presentateur, portes[index_presentateur]))
    choices_final.remove(index_presentateur)
    choices_final.remove(index_porte_initial)
    final_choice = choices_final[0]
    final_choice_no_changing = portes[index_porte_initial]
    # print('The result is the door number {} which is a {}'.format(final_choice, portes[final_choice]))

    if portes[final_choice] == 'ferrari':
        counter_success += 1
    if final_choice_no_changing == 'ferrari':
        counter_success_no_changing += 1

print('The probability when changing the strategy is: ', counter_success / number_trials_monty_python)
print('The probability when not changing the strategy is: ', counter_success_no_changing / number_trials_monty_python)


# Bayes Theorem

########

### 9. Suite de Fibonnacci
N = 8

f_0 = 1
f_1 = 1
a, b = f_0, f_1

for k in range(N):
    c = a + b
    a = b
    b = c

phi = (1 + np.sqrt(5)) / 2
phi_prime = (1 - np.sqrt(5)) / 2

result_formula = int((phi ** N - phi_prime ** N) / np.sqrt(5))
