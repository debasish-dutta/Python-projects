import win10toast
import schedule 
import time 


noti = win10toast.ToastNotifier()

#def manga():
noti.show_toast('Remainder!!!!', 'Catch up on the lastest Mangas.', duration=15)
'''def LN():
    noti.show_toast('Remainder!!!!', 'Catch up on the lastest Light Novels.', duration=15)
def BB99():
    noti.show_toast('Remainder!!!!', 'Catch up on the lastest episode of BB99.', duration=15)

schedule.every().friday.at("17:00").do(manga) 
schedule.every().day.at("16:00").do(LN) 
schedule.every().thursday.at("08:00").do(BB99) 
'''