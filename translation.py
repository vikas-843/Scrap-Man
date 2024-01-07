class Translation(object):
    START_TEXT = """<b>Hai TANJIRO •ＲＤＪᵀᴹ ✨️,
i am Api ID & Hash Scrapper

Enter your Telegram Phone Number, eg: +91xxxxxxxx
to get the APP-ID from my.telegram.org

/start at any stage to re-enter your details</b>
"""
    AFTER_RECVD_CODE_TEXT = """<b>I see!
now please send the Telegram code that 
you received from Telegram!

this code is only used for the purpose of 
getting the APP ID from my.telegram.org

/start at any stage to re-enter your details</b>
"""
    BEFORE_SUCC_LOGIN = "<code>recieved code. Scarpping web page ...</code>"
    ERRED_PAGE = """Hadeh Error. Coba dengan Cara Manual

Cara Ambil APP ID dan API HASH Secara Manual:
1. Buka my.telegram.org/auth
2. Loginkan akun telegram kalian
3. klik menu API Development
4. isi data seperti dibawah ini :
• App Title : tgbot
• Short Name : tgbot
• URL : (kosongin)
• Platform : desktop
5. Selesai

Bila Berhasil Ambil Manual Silahkan Coba Lagi di Bot ini"""
    CANCELLED_MESG = "<b>Bye! Silahkan /start kembali untuk mengulang</b>"
    IN_VALID_CODE_PVDED = "<b>Invalid confirmation code!</b>"
    IN_VALID_PHNO_PVDED = """<b>sorry, 
but the input does not seem to be 
a valid phone number</b>"""
    
