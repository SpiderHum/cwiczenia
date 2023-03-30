#projekt numer 5 -- konwenter jednostkek
#Udajmy się do Trojej, ku spotkaniu ruin a pozostałości po straciu dziesięcioletnim tytanów
'''
km kwadratowy == 1 000 000 m2 == 100 ha == 10 000 ar
metr kwadratowy == 100 dm2 == 10 000 cm2 == 1 000 000 mm2
dm kwadratowy == 100 cm2 == 10 000 mm2
cm kwadratowy == 100 mm2
mm kwadratowy == 0,01 cm2
hektar = 100 ar
ar = 100 m2
'''
m=int(input())
km=0.001*m
dm=10*m
cm=100*m
mm=1000*m
print(f'Podales {m} metrow, jest to {km} kilometrow, {dm} decymetrow, {cm} centymetrów')

#cal=25,4*0,1cm
cal=2.54*cm #w centymetrach
stopa=12*cal #w centymetrach
jard=stopa*3
pret=5,5*jard
lancuch=4*pret
furlong=10*lancuch
mila=8*furlong
liga=3*mila
#nie wiedziec czemu out wyglądał tak, do jardów jest wszystko ok. Od nich zle sie dzieje. To tak jakby stala wartosc komputer powielał X razy. A ten X to wcześniejsza zmienna. 
print(f'{cm} centymetrow to: {cal} cali, {stopa} stop, {jard} jardow, {pret} pretow, {lancuch} lancuchow, {furlong} furlongow, {mila} mil i {liga} lig')
