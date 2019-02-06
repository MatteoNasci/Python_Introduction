'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''


def es3(lista, testo):
    common_words_dictionary = {}
    for string in lista:
        if string in testo:
            lista.remove(string)
            if string in common_words_dictionary:
                common_words_dictionary[string][0] += 1
            else:
                common_words_dictionary[string] = (1, testo.index(string))


    #utilizzo lista temporanea per leggibilità invece di fare tutto in una riga nel return
    ordered_list = list(common_words_dictionary.keys())

    ordered_list.sort(key=lambda word: (common_words_dictionary[word][0], word)) #ordino per occorrenze in testo e, secondariamente, per la parola
    most_common_word = ordered_list[0]

    ordered_list.sort(key=lambda word: (common_words_dictionary[word][1], word)) #ordino per apparizione in testo e, secondariamente, per la parola

    return (ordered_list, most_common_word)
