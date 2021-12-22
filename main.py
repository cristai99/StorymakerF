from tkinter import *
from tkinter import messagebox

def check1():
    if var1.get() == 1:
        if var2. get() == 1:
            c1 = 1
            return(c1)
        elif var2. get() == 2:
            c1 = 2
            return(c1)
        elif var2.get() == 3:
            c1 = 3
            return (c1)
        else:
            messagebox.showerror("Ошибка", "Выберите количество персонажей")
            c1 = 0
            return (c1)
    elif var1.get() == 2:
        if var2. get() == 1:
            c1 = 4
            return(c1)
        elif var2. get() == 2:
            c1 = 5
            return(c1)
        elif var2.get() == 3:
            c1 = 6
            return (c1)
        else:
            messagebox.showerror("Ошибка", "Выберите количество персонажей")
            c1 = 0
            return (c1)
    elif var1.get() == 3:
        if var2.get() == 1:
            c1 = 7
            return (c1)
        elif var2.get() == 2:
            c1 = 8
            return (c1)
        elif var2.get() == 3:
            c1 = 9
            return (c1)
        else:
            messagebox.showerror("Ошибка", "Выберите количество персонажей")
            c1 = 0
            return (c1)
    else:
        messagebox.showerror("Ошибка", "Выберите тему")
        c1 = 0
        return (c1)

def btn_print():
    text_to_save = text2.get('1.0', END)
    f = open('Рассказ.txt', 'w')
    f.write(text_to_save)
    f.close()

def Text_11(text):
    # О жизни одного человека
    T11 = text.rsplit(' ')
    T11 = list(map(str.rstrip, T11))
    result11 = T11[0] + ' ' + T11[1] + ' ' + 'по шоссе и ' + T11[2] + ' ' + 'сушку, а в школе ' + T11[0] + ' ' + T11[3]
    return(result11)

def Text_12(text):
    #О жизни двоих
    T12 = text.rsplit(' ')
    T12 = list(map(str.rstrip, T12))
    result12 = T12[2] + ' ' + T12[0] + ' и ' + T12[1] + ' на войну.  ' +\
               T12[0] + ' повредил бронежилет, а ' + T12[1] + ' потратил патроны. Они ' + T12[3] +\
               ' план. ' + T12[0] + ' проявил героизм и стал живым щитом для ' + T12[1] + '. И ' + T12[1] +\
               ' стал отстреливаться за ' + T12[0] + '. ' + T12[0] + ' и ' + T12[1] + ' ' + T12[4] + '.'
    return(result12)

def Text_13(text):
    #О жизни 3х персонажей
    T13 = text.rsplit(' ')
    T13 = list(map(str.rstrip, T13))
    result13 = 'Жили-были три китайца: ' + T13[0] + ', ' + T13[1] + ', ' + T13[2] + '.Все они  ' + T13[3] +\
               ', а потом женились: ' + T13[0] + ' на Цыпе, ' + T13[1] + ' на Цыпе-дрыпе, ' + T13[2] +\
               ' на Цыпе-дрыпе-дрымпампони. Потом, они ' + T13[4] + ' в горы, где ' + T13[5] +\
               'дом и нарожали деток. У ' + T13[0] + ' с Цыпой - Шах, у ' + T13[1] +\
               ' с Цыпой-дрыпой - Шах-шарах, у ' + T13[2] + ' с Цыпой-дрыпой-дрымпампони - Шах-шарах-шарах-широни.'
    return (result13)

def Text_21(text):
    #Страшилка с 1 персом
    T21 = text.rsplit(' ')
    T21 = list(map(str.rstrip, T21))
    result21 = 'В черный-черный город ' + T21[1] + ' ' + T21[0] + '. ' + 'Однажды, ' + T21[0] + ' ' + T21[2] +\
               ' гробик, в котором лежала записка "Этот код с костылями". ' + T21[0] + ' ' + T21[3]
    return (result21)

def Text_22(text):
    # Страшилка с 2 персами
    T22 = text.rsplit(' ')
    T22 = list(map(str.rstrip, T22))
    result22 = T22[0] + ' сожгла всех кукол, хотя ' + T22[1] + ' плакала и умоляла этого не делать. Они ' + T22[3] +\
               '. ' + T22[1] + ' не понимала ужаса  ' + T22[0] + ' и никак не хотела верить в то, что это не ' +\
               T22[0] + ' каждую ночь ' + T22[3] + ' кукол по квартире. Позднее, они ' +\
               T22[4] + 'и больше их никто не видел.'
    return(result22)

def Text_23(text):
    # Страшилка с 3 персами
    T23 = text.rsplit(' ')
    T23 = list(map(str.rstrip, T23))
    result23 = '- Ни в коем случае не ходите в дальнюю кладовку, - сказала ' + T23[0] + '\n ' + 'Конечно же, ' +\
               T23[1] + ' и ' + T23[2]+ ' немедленно ' + T23[3] + ' у нее ключ. В кладовке мы ' + T23[4] +\
               ' мёртвых детей, которые были похожи на нас. Их тела были изуродованы. ' + T23[0] +\
               ' уже стояла за нами с ножом. Мы не  ' + T23[5] + '.'
    return(result23)

def Text_31(text):
    # Сказка про 1 персонажа
    T31 = text.rsplit(' ')
    T31 = list(map(str.rstrip, T31))
    result31 = 'Жила-была снежинка ' + T31[0] + '. Однажды она попала на стекло и  ' + T31[1] + \
               '. Она увидела, что мама рассказывает ребенку сказку перед сном.  ' + T31[0] + \
               ' никогда раньше не ' + T31[2] + ' об этом. Снежинка была счастлива, что за свою недолгую жизнь успела  ' +\
               T31[3] + ' это.'
    return(result31)

def Text_32(text):
    # Сказка о 2 персонажах
    T32 = text.rsplit(' ')
    T32 = list(map(str.rstrip, T32))
    result32 = 'Жил-был зелёный кузнечик ' + T32[0] + '. У него был друг - сверчок ' + T32[1] +\
               '. И вот однажды ' + T32[0] + ' предложил пойти в Волшебный лес, ведь там, как он слышал, растут волшебные цветы. Они ' +\
               T32[2] + ' туда. На пути были препятствия, но друзья ' + T32[3] +\
               ' все трудности и добрались до леса, в котором решили ' + T32[4] + ' .'
    return(result32)

def Text_33(text):
    # Сказка о 3х персонажах
    T33 = text.rsplit(' ')
    T33 = list(map(str.rstrip, T33))
    result33 = 'Жила была губка для мытья посуды ' + T33[0] + ' в своей упаковочке, была у неё большая семья: розовая губка ' + \
               T33[1] + ' и жёлтая '+ T33[2] +\
               ', которая так гордилась, что выглядит как их любимый актер из известного сериала. Однажды, они ' +\
               T33[3] + ' в путешествие по квартире. Сначала, они ' + T33[4] + ' швабру Алису, а потом вместе ' + T33[5] +\
               ' всю квартиру. '
    return(result33)

def btn_click():
    text2.delete('1.0', END)
    text = text1.get('1.0', END)
    c1 = check1()
    try:
        if c1 == 1:
            result = Text_11(text)
        elif c1 == 2:
            result = Text_12(text)
        elif c1 == 3:
            result = Text_13(text)
        elif c1 == 4:
            result = Text_21(text)
        elif c1 == 5:
            result = Text_22(text)
        elif c1 == 6:
            result = Text_23(text)
        elif c1 == 7:
            result = Text_31(text)
        elif c1 == 8:
            result = Text_32(text)
        elif c1 == 9:
            result = Text_33(text)
    except IndexError:
        messagebox.showerror("Ошибка", "Некорректные данные")
        result = ''
    text2.insert(END, result + '\n')


root = Tk()
root['bg'] = '#E0FFFF' #Цвет фона
root.title('Создатель рассказов')
root.wm_attributes('-alpha', 0.9)
root.geometry('1100x550')
root.resizable(width = False,height = False) #Запрет на изменение размера

canvas = Canvas(root, height = 650, width = 1100)
canvas.pack()

frame = Frame(root, bg='#AFEEEE')
frame.place(relx = 0, rely =0, relwidth=0.5, relheight=1)

#Выбор темы рассказа
title1 = Label(frame, text = 'Темы', bg='#AFEEEE', font = 60)
title1.pack()

var1=IntVar()
var1.set(0)
rbutton1=Radiobutton(frame, text = 'Рассказ о жизни', variable=var1, value=1)
rbutton2=Radiobutton(frame, text = 'Жуткая история', variable=var1, value=2)
rbutton3=Radiobutton(frame, text = 'Сказка', variable=var1, value=3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()


#Выбор Количества персонажей
title2 = Label(frame, text = 'Количество персонажей', bg='#AFEEEE', font = 60)
title2.pack()


var2=IntVar()
var2.set(0)
rbutton4=Radiobutton(frame, text = '1', variable=var2, value=1)
rbutton5=Radiobutton(frame, text = '2', variable=var2, value=2)
rbutton6=Radiobutton(frame, text = '3', variable=var2, value=3)
rbutton4.pack()
rbutton5.pack()
rbutton6.pack()

title3 = Label(frame, text = 'Входные данные', bg='#AFEEEE', font = 60)
title3.pack()

title6 = Label(frame, text = 'Для корректного заполнения данных нужно:' + '\n' +' 1) Ввести имя каджого персонажа и 3 действия, которые он/они делали' + '\n' +'2) Действия - это глаголы в прошедшем совершенном времени)' + '\n' +'3) Записывать нужно через пробел.', bg='#FFFFFF', font = 50)
title6.pack()

text1=Text(frame,height=7,width=39,font='Arial 14',wrap=WORD)
text1.pack()

title5 = Label(frame, text = '', bg='#AFEEEE', font = 80)
title5.pack()

btn = Button(frame, text = 'Подтвердить', bg = '#20B2AA', command = btn_click)
btn.pack()

frame2 = Frame(root, bg='#AFEEEE', bd=5)
frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

title4 = Label(frame2, text = 'Результат', bg='#AFEEEE', font = 80)
title4.pack()

text2=Text(frame2,height=19.28,width=40, font='Arial 14',wrap=WORD)
text2.pack()

title7 = Label(frame2, text = '', bg='#AFEEEE', font = 60)
title7.pack()

btn_p = Button(frame2, text = 'Сохранить', bg = '#20B2AA', command = btn_print)
btn_p.pack()

root.mainloop()
