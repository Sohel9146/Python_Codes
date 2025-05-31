import smtplib

try:
    hostname = "smtp.gmail.com"
    email = "suhailshaikh7866@gmail.com"
    password = "jxjhfwmikgdiugnt"

    with smtplib.SMTP(host=hostname) as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendmail(
            from_addr=email,
            to_addrs=email,
            msg= "Subject = This is Test Mail.. \n \n Helo My Name is Sohel Shaikh. I am from Solapur Maharashtra"
        )
except Exception as e:
    print(type(e))