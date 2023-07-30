import smtplib
from quotes import quote_oftheday
import datetime as dt
last_sent_date = None
day = [0,1,2,3,4,5,6]
now = dt.datetime.now()
day_of_theweek= now.weekday()
current_date = now.strftime("%Y-%m-%d")

while day_of_theweek == 6:
    if last_sent_date != current_date:
        my_email = "shristytest@gmail.com"
        my_pw = "xcdrncopbmctdnkp"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pw)
            message = quote_oftheday()

            # Convert the message to bytes using utf-8 encoding
            msg = message.encode("utf-8")

            connection.sendmail(
                from_addr=my_email,
                to_addrs="shristytest@yahoo.com",
                msg=msg
            )

    last_sent_date = current_date