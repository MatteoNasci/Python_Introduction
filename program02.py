'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche'
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''

import algorithms


def es2(N, ins):
    sorted_lamps = sorted(ins)
    # inserite qui il vostro codice
    return sorted([index for index in list(range(N, 0, -1)) if switch_lamps(sorted_lamps, index)])


def switch_lamps(ins, last_lamp_index):
    if algorithms.binary_sort(ins, last_lamp_index) == False: #non mi piacciono tutti questi binary sort per quanto efficienti
        list_to_add = [last_lamp_index]
        list_to_remove = []
        for index in list(range(1, last_lamp_index // 2 + 1)):
            if last_lamp_index % index == 0:
                if algorithms.binary_sort(ins,index):
                    list_to_remove.append(index)
                else:
                    list_to_add.append(index)

        for i in list(range(len(list_to_remove))):
            ins.remove(list_to_remove[i])

        for i in list(range(len(list_to_add))):
            ins.append(list_to_add[i])

        ins.sort() #è possibile evitare il sort?
        
        return True
    return False
