# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:48:37 2021

@author: Someone
"""
import random
import datetime
import os

def sprawdz_plik(plik):
    if os.path.exists(plik):
        if os.stat(plik).st_size == 0:
            with open(plik, 'a') as f:
                f.write('Nowa gra')
        else:
            with open(plik, 'a') as f:
                f.write('\n\nNowa gra')
    else:
        with open(plik, 'a') as f:
            f.write('Nowa gra')

def graj():
    p1_score = 0
    p2_score = 0
    p1 = ""
    lista = ['papier', 'kamien', 'nozyce', 'jaszczurka', 'spock']
    sprawdz_plik('wyniki.txt')
                
    for x in count(0):
        print("Wybierz: papier - p, kamień - k, nożyce - n, jaszczurka - j, spock - s")
        wybor_gracza = input().lower()
        if wybor_gracza == "p":
            p1 = "papier"
        elif wybor_gracza == "k":
            p1 =  "kamien"
        elif wybor_gracza == "n":
            p1 = "nozyce"
        elif wybor_gracza == "j":
            p1 =  "jaszczurka"
        elif wybor_gracza == "s":
            p1 =  "spock"
        else:
            print("Błędny wybor")
        
        
        p2 = random.choice(lista)
        print(p2)
        
        if p1 == p2:
            print(f'Remis, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nRemis, wynik: {p1_score}:{p2_score}')
        elif p1 == 'papier' and p2 == 'nozyce' or p1 == 'papier' and p2 == 'spock':
            p2_score += 1
            if p2_score == 6:
                print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'\nPrzegrales {p1_score} do {p2_score}\nGra zakończona {datetime.datetime.now()}')
                break
            print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
        elif p1 == 'kamien' and p2 == 'papier' or p1 == 'kamien' and p2 == 'jaszczurka':
            p2_score += 1
            if p2_score == 6:
                print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}\nGra zakończona {datetime.datetime.now()}')
                break
            print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
        elif p1 == 'nozyce' and p2 == 'kamien' or p1 == 'nozyce' and p2 == 'spock':
            p2_score += 1
            if p2_score == 6:
                print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'Przegrales, wynik: {p1_score} do {p2_score}\nGra zakończona {datetime.datetime.now()}\n')
                break
            print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'b') as f:
                f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
        elif p1 == 'jaszczurka' and p2 == 'kamien' or p1 == 'jaszczurka' and p2 == 'nozyce':
            p2_score += 1
            if p2_score == 6:
                print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}\nGra zakończona {datetime.datetime.now()}\n')
                break
            print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
        elif p1 == 'spock' and p2 == 'jaszczurka' or p1 == 'spock' and p2 == 'papier':
            p2_score += 1
            if p2_score == 6:
                print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}\nGra zakończona {datetime.datetime.now()}\n')
                break
            print(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nPrzegrales, wynik: {p1_score}:{p2_score}')
        else:
            p1_score += 1
            if p1_score == 6:
                print(f'\nWygrales, wynik: {p1_score}:{p2_score}')
                with open('wyniki.txt', 'a') as f:
                    f.write(f'\nWygrales, wynik: {p1_score}:{p2_score}\nGra zakończona {datetime.datetime.now()}\n')
                break
            print(f'\nWygrales, wynik: {p1_score}:{p2_score}')
            with open('wyniki.txt', 'a') as f:
                f.write(f'\nWygrales, wynik: {p1_score}:{p2_score}')

graj()