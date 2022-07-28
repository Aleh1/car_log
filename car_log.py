limit = 2000
TO_1 = 15000
TO_2 = 30000
TO=0


start = int(input('введите начальный спидометр '))
f = open("log.txt", "a")
f.write(str(start))
f.close()
while 1>0:
    #start = int(input('введите начальный спидометр '))
    km = input('введите растояние за сегодня ')#
    if km == '':
        stop = int(input('показания конечного спидометра '))#программа постоянно спашивает показания 
        if stop<start:#
            print('ERROR')#возникает ошибка в случае не коректного ввода спидометра
            break
    else:
        print(km)
        stop = int(km) + start#
        #km = stop - start
    print('1')       
    #tr = int(input('сколько проехал по трассе?')
    km =  stop - start #автомобиль проехал км
    print ('Растояние в км '+str(km))
    rh = km * 0.175 #расход топлива
    print('Расход в литрах '+str(rh))
    sp=km + start #показания спидометра
    start = sp
    print('значение спидометра ' + str(start))
    print('2')
    #
    #eo = input('введите работу которую вы выполнидли сегодня  ')
    #if eo != '': # запись в журнал работу которую выполнили 
       # print( str(start)+' '+ str(eo))
    #
    if start >=TO_1 - limit and start <=TO_1 and start<TO_2 and TO==0:
    #условие спидометра меньше и меньше то2 и метка ТО=0
        print('выполните ТО')
    elif start >TO_1 and start<TO_2 and TO==0:
        vo = input('вы провели ТО? если да наберите 1 ')
        if vo == str(1):
            print('счасливого пути')# в строку памяти вносится значение которое в дальнейшем запаминает
            la = input('введите какие работы вы провели ? ')
            print(str(stop)+la)
            TO=1 #метка что то пройден            

                
        elif vo == '':
            print('ВНИМАНИЕ! движение опасно на данном автомобиле 2')
        else:
            print('ВНИМАНИЕ! движение опасно на данном автомобиле ')
    # журнал ЕО
    eo = input('введите работу которую вы выполнили сегодня  ')
    if eo != '': # запись в журнал работу которую выполнили 
        print( str(start)+' '+ str(eo))
        f = open("log.txt", "a")
        f.write("\n" + str(start)+' '+ str(eo))
        f.close()

