import pygame as pyg

#Algne menüü
#AKTIIVNE: 0 - menüü, 1 - laud, 2 - mäng läbi
def menyy():
    
    global ekraan
    global aktiivne
    global konstant
    global aknax
    global aknay
    global taust
    global must
    global tiim
    global tiim1
    global tiim2
    global ristmikud
    global manginupp
    global vaikemang
    global keskmang
    global suurmang
    
    pyg.init()
    
    aktiivne = 0
    
    tiim = 0

    #Standartsed konstandid
    suurus = aknax, aknay = 1500, 750
    
    konstant = 100
    
    #Värvid
    taust = pyg.Color(171, 171, 171)
    
    must = pyg.Color(0,0,0)
    
    #Mäng on ehitatud järjenditel
    tiim1 = []
    tiim2 = []
    ristmikud = []
    
    #Akna ehitamine
    ekraan = pyg.display.set_mode(suurus)
    ekraan.fill(taust)

    #Nupud menüüs
    manginupp = pyg.Rect(((aknax-2*konstant)/2, konstant/2, 2*konstant, konstant/2))
    vaikemang = pyg.Rect(5*aknax/6-konstant/2, aknay/3, konstant/2, konstant/2)
    keskmang = pyg.Rect((2*aknax/3, aknay/3, konstant, konstant))
    suurmang = pyg.Rect((aknax/2, aknay/3, 1.5*konstant, 1.5*konstant))

    pyg.draw.rect(ekraan, (50, 50, 50), manginupp)
    pyg.draw.rect(ekraan, (50, 50, 50), vaikemang)
    pyg.draw.rect(ekraan, (50, 250, 50), keskmang)
    pyg.draw.rect(ekraan, (50, 50, 50), suurmang)
    

#Mängulaud
def laud():
    global vahed
    
    #Oleme laual
    aktiivne = 1
    
    #Menüü värvitakse üle
    ekraan.fill(taust)
    
    #Standard konstant
    vahed = konstant/2
    
    #Ruudustik
    for i in range(int(aknax/vahed)):
        pyg.draw.line(ekraan, must, (vahed*i, 0), (vahed*i, aknay))
        
    for j in range(int(aknay/vahed)):
        pyg.draw.line(ekraan, must, (0, vahed*j), (aknax, vahed*j))
    
    #Ruudustiku ristumiskohad e. n.n. mänguväljad
    #Pane tähele! Kui ekraani koordinaatidega oleksid ristumis kohad reas näiteks [(10, 10),(20, 10),(30, 10)...],
    #siis see sama rida välja koordinaatidega oleks [(1,1), (2,1), (3,1)...]
    for i in range(1, int(aknax/vahed)):
        for j in range(1, int(aknay/vahed)):
            ristmikud.append([i, j])


#Hiireklõpsu korral
def klops():
    #Hiire koordinaadid
    hiir = pyg.mouse.get_pos()
    hiirx = hiir[0]
    hiiry = hiir[1]
    
    #Defineerime värvid
    punane = (210, 50, 20)
    sinine = (20, 20, 210)
    
    global aktiivne
    global konstant
    global tiim
    
    #Kui menüü on ees
    #TAGASTUS: 0 - Eesmärk täidetud
    if aktiivne == 0:
        #Mängunupp
        if manginupp.x < hiirx < manginupp.x+manginupp.w and manginupp.y < hiiry < manginupp.y+manginupp.h:
            aktiivne = 1
            laud()
            return 0
        #Suurem plats
        elif suurmang.x < hiirx < suurmang.x+suurmang.w and suurmang.y < hiiry < suurmang.y+suurmang.h:
            konstant = 75
            pyg.draw.rect(ekraan, (50, 50, 50), vaikemang)
            pyg.draw.rect(ekraan, (50, 50, 50), keskmang)
            pyg.draw.rect(ekraan, (50, 250, 50), suurmang)
            return 0
        
        #Tavaline plats
        elif keskmang.x < hiirx < keskmang.x+keskmang.w and keskmang.y < hiiry < keskmang.y+keskmang.h:
            konstant = 100
            pyg.draw.rect(ekraan, (50, 50, 50), vaikemang)
            pyg.draw.rect(ekraan, (50, 250, 50), keskmang)
            pyg.draw.rect(ekraan, (50, 50, 50), suurmang)
            return 0
        
        #Väikseim plats
        elif vaikemang.x < hiirx < vaikemang.x+vaikemang.w and vaikemang.y < hiiry < vaikemang.y+vaikemang.h:
            konstant = 150
            pyg.draw.rect(ekraan, (50, 250, 50), vaikemang)
            pyg.draw.rect(ekraan, (50, 50, 50), keskmang)
            pyg.draw.rect(ekraan, (50, 50, 50), suurmang)
            return 0
        
        
        
        
    #Kui laud on ees
    #TIIM: 0 - Tiim1, 1 - Tiim2
    #TAGASTUS: 1- Võitis Tiim1, 2- Võitis Tiim2, 3 - Läheb edasi
    if aktiivne == 1:
        
        #Teisendame ekraani koordinaadid välja koordinaatideks ning normaliseerin nad, sedasi,
        #et valitaks vajutuskohale lähim ristumiskoht
        klopsx = int((hiirx+vahed/2)/vahed)
        klopsy = int((hiiry+vahed/2)/vahed)
        
        #Kas vajutatud väli on vaba
        if [klopsx, klopsy] in ristmikud:
            #Tiim1
            if tiim == 0:
                #Joonistab nupu
                pyg.draw.circle(ekraan, punane, (vahed*klopsx, vahed*klopsy), 2*vahed/5)
                
                #Eemaldab välja vabade väljade hulgast, lisab tiimi nuppude hulka
                ristmikud.pop(ristmikud.index([klopsx, klopsy]))
                tiim1.append([klopsx, klopsy])
                
                #Olgu Tiim2 kord
                tiim = 1
                #Võidu kontroll
                if kontroll(tiim1):
                    return 1
                return 3
            
            #Tiim2
            #Joonistab nupu
            pyg.draw.circle(ekraan, sinine, (vahed*klopsx, vahed*klopsy), 2*vahed/5)
            
            #Eemaldab välja vabade väljade hulgast, lisab tiimi nuppude hulka
            ristmikud.pop(ristmikud.index([klopsx, klopsy]))
            tiim2.append([klopsx, klopsy])
            
            #Olgu Tiim1 Kord
            tiim = 0
            #Võidu kontroll
            if kontroll(tiim2):
                return 2
            return 3
    
    
    
    #Kui on selgunud Võitja
    #TAGASTUS: -1 - Peatada mäng
    if aktiivne == 2:
        #Paneb mängu kinni
        if quitnupp.x < hiirx < quitnupp.x+quitnupp.w and quitnupp.y < hiiry < quitnupp.y+quitnupp.h:
            pyg.quit()
            return -1
        #Viibt tagasi menüüsse
        elif menyynupp.x < hiirx < menyynupp.x+menyynupp.w and menyynupp.y < hiiry < menyynupp.y+menyynupp.h:
            menyy()

#Võidukontroll
#SISEND: Tiimi nupud
#VÄLJUND: 0 - Tiim pole Võitnud, 1 - Tiim on võitnud
def kontroll(arr):
    #Sisend
    for i in arr:
        x = i[0]
        y = i[1]
        #Veerud
        if [x, y+1] in arr and [x, y+2] in arr and [x, y+3] in arr and [x, y+4] in arr:
            pyg.draw.line(ekraan, must, (x*vahed, y*vahed), (x*vahed, (y+4)*vahed), 5)
            return 1
        
        #Read
        if [x+1, y] in arr and [x+2, y] in arr and [x+3, y] in arr and [x+4, y] in arr:
            pyg.draw.line(ekraan, must, (x*vahed, y*vahed), ((x+4)*vahed, y*vahed), 5)
            return 1
        
        #Peadiagonaalid
        if [x+1, y+1] in arr and [x+2, y+2] in arr and [x+3, y+3] in arr and [x+4, y+4] in arr:
            pyg.draw.line(ekraan, must, (x*vahed, y*vahed), ((x+4)*vahed, (y+4)*vahed), 5)
            return 1
        
        #Kõrvaldiagonaalid
        if [x+1, y-1] in arr and [x+2, y-2] in arr and [x+3, y-3] in arr and [x+4, y-4] in arr:
            pyg.draw.line(ekraan, must, (x*vahed, y*vahed), ((x+4)*vahed, (y-4)*vahed), 5)
            return 1
    return 0

#Võitja selgumise korral
def manglabi():
    global menyynupp
    global quitnupp
    
    #Joonistab akna tausta
    labitaust = pyg.Rect((aknax/4, 5/8*aknay, aknax/2, aknay/4))
    labitaustaar = pyg.Rect((aknax/4-2, 5/8*aknay-2, aknax/2+4, aknay/4+4))
    
    pyg.draw.rect(ekraan, (50, 50, 50), labitaustaar)
    pyg.draw.rect(ekraan, (171, 171, 171), labitaust)
    
    #Joonistab nupud
    menyynupp = pyg.Rect((aknax/4+aknax/16, 11/16*aknay, aknax/8, aknay/8))
    quitnupp = pyg.Rect((aknax/2+aknax/16, 11/16*aknay, aknax/8, aknay/8))
    
    pyg.draw.rect(ekraan, (50, 50, 50), menyynupp)
    pyg.draw.rect(ekraan, (250, 50, 50), quitnupp)
    
    
#Initsialiseerib mängu
menyy()
#Mängu "Main loop"
while True:
    #Uuendab akent, n.n. frame
    pyg.display.flip()
    #Ootab käsku
    e = pyg.event.wait()
    #Välub mängust, kui panna ristist kinni
    if e.type == pyg.QUIT:
        pyg.quit()
        break
    #Hiire vajutuse korral
    if e.type == pyg.MOUSEBUTTONDOWN:
        #Vaatab mida teha
        voitja = klops()
        if voitja == -1:
            break
        if voitja in [1, 2]:
            #Keegi on võitnud, seega tema võit väljastatakse konsooli ning mäng läheb "mäng läbi" reziimi
            print(f"{'Tiim 1' if voitja == 1 else 'Tiim 2'} võitis")
            manglabi()
            aktiivne = 2