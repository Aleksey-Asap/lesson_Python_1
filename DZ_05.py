# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# print(' '.join(filter(lambda X: not 'абв' in X,'Иногда домашнееабв задание сложноеабв'.split())))


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# import random
# totalSweets=2021

# def CheckEnteredNumber(number):
#     try:
#         int(number)
#         return True
#     except ValueError:
#         return False

# def GetScore(candiesAmount,turn):
#     while True:
#         if CheckEnteredNumber(candiesAmount):
#             candiesAmount=int(candiesAmount)
#             if 0<candiesAmount<=28:
#                 return candiesAmount
#             else:
#                 print("Check your input, it must be integer [1...28].")
#                 candiesAmount=input(f"Player {turn} turn. Enter number of candies. It should be in range [1...28]: ")
#         else:
#             print("Check your input, it must be integer [1...28].")
#             candiesAmount=input(f"Player {turn} turn. Enter number of candies. It should be in range [1...28]: ")

# def Lottery():
#     print("Now you will have lotery to identify who will be the first!")
#     player1Num=input("The first player please enter your number from 0 to 100: ")
#     player2Num=input("The second player please enter your number from 0 to 100: ")
#     if CheckEnteredNumber(player1Num) and CheckEnteredNumber(player2Num):
#         player1Num=int(player1Num)
#         player2Num=int(player2Num)
#         if (0<=player1Num<=100) and (0<=player2Num<=100):
#             botNum=random.randint(0,100)
#             print(f"The reference number is {botNum}.")
#             dif1=abs(player1Num-botNum)
#             dif2=abs(player2Num-botNum)
#             if dif1>dif2:
#                 return False
#             else:
#                 return True
#         else:
#              print("Check your input, it must be integer [0...100].")
#              Lottery()
#     else:
#         print("Check your input, it must be integer [0...100].")
#         Lottery()

# def Game(candiesNum):
#     if Lottery():
#         print("Player 1 the first.")
#         turnFlag=1
#     else:
#         print("Player 2 the first.")
#         turnFlag=2
#     while candiesNum>0:
#         print(f"{candiesNum} candies left.")
#         if turnFlag==1:
#             candiesAmount=GetScore(input(f"Player {turnFlag} turn. Enter number of candies. It should be in range [1...28]: "),turnFlag)
#             turnFlag=2
#         else:
#             candiesAmount=GetScore(input(f"Player {turnFlag} turn. Enter number of candies. It should be in range [1...28]: "),turnFlag)
#             turnFlag=1
#         candiesNum=candiesNum-candiesAmount
#     return turnFlag  

# winName=Game(totalSweets)
# if winName==2:
#         print("Player 1 is winner!") 
# else:
#         print("Player 2 is winner!")  



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def encode(s):
 
#     encoding = "" # сохраняет выходную строку
 
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1
 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
 
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding
 
# s = 'AAAAAAABBCCCD'
# print(encode(s))