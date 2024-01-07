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
    ERRED_PAGE = """Here is the translation:

"Manual Method to Obtain APP ID and API HASH:
1. Open my.telegram.org/auth
2. Log in to your Telegram account
3. Click on API Development in the menu
4. Fill in the data as follows:
   - App Title: tgbot
   - Short Name: tgbot
   - URL: (leave it blank)
   - Platform: desktop
5. Done

If you have successfully obtained the information manually, please try again on this bot."
"""
    
    CANCELLED_MESG = "<b>Bye! Silahkan /start kembali untuk mengulang</b>"
    IN_VALID_CODE_PVDED = "<b>Invalid confirmation code!</b>"
    IN_VALID_PHNO_PVDED = """<b>sorry, 
but the input does not seem to be 
a valid phone number</b>"""

