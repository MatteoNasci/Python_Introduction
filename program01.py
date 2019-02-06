'''
Sono stati appena corretti i compiti di N studenti ed in una lista sono riportati
i voti ottenuti dai vari studenti.
Sia C il voto massimo assegnato (questo significa che i voti sono interi da 0 a C compresi).
Bisona stabilire una soglia tra 0 e C a partire dalla quale gli studenti verranno ammessi all'orale.
(ovvero vengono ammessi tutti quelli con voti maggiori o uguali alla soglia)

Non volendo essere ne' troppo severo ne' troppo generoso nella valutazione, il docente, prima di scegliere la soglia,
decide di generare per ognuna delle possibili C+1 soglie (da 0 a C compreso)
il numero di studenti che verrebbero ammessi all'orale per quella soglia.

Definire una funzione es1(voti) che, data lista non vuota 'voti' con i voti degli studenti,
restituisce la lista di C+1 interi dove in posizione i si trova  il numero di studenti ammessi
all'orale nel caso la soglia venga fissata al valore i.
ATTENZIONE: la lista ls dei voti al termine della funzione NON DEVE risultare modificata.
Ad esempio per voti=[7,5,8,3,7,2,9] la funzione es2 restituisce la lista
[7, 7, 7, 6, 5, 5, 4, 4, 2, 1]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''
import algorithms


def es1(voti):
    # inserite qui il vostro codice
    ordered_voti = sorted(voti[:])
    last_value = len(ordered_voti)
    max_value = ordered_voti[last_value - 1]
    return [get_passed_students(ordered_voti,vote, last_value) for vote in list(range(max_value + 1))]

def get_passed_students(ordered_voti,vote, last_value):
    index = 0
    while vote > ordered_voti[index]:
        index +=1
    if index > 0:
        ordered_voti = ordered_voti[index:]
        last_value -= index
    return last_value
    
