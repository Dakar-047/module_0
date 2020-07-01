#!/usr/bin/env python
# coding: utf-8

# In[51]:


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    
    count_ls = []
    np.random.seed(1)  
    # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)


import numpy as np
def game_core_v3(number):
    '''В нашем алгоритме мы загадываем любое Random число в педелах границ интервала.
    
       Далее начинаем угадывать загаданное число начиная с середины интервала
       и каждый раз делим интервал на 2, уменьшая его границы в зависимости от того, 
       больше оно или меньше загаданного числа.
       
       Функция принимает загаданное число и возвращает число попыток.
       '''
    
    count = 0
    predict = np.random.randint(1,101)
    border_1 = 1
    border_2 = 100
    
    while True:
        count += 1
        number = (border_1+border_2)//2 
        if number==predict:
            break
        elif number<predict:
            border_1 = number + 1       
        else:
            border_2 = number - 1
               
    return(count) 


# In[52]:


score_game(game_core_v3)


# In[ ]:




