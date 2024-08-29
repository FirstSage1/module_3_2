# ДЗ модуль 3_2.Способы вызова функций. Задача "рассылка писем".
# ===============================================================
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if '@' in recipient or sender or ".com" / ".ru" / ".net" in recipient[-4:] or sender[-4:]:
        print("Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com")
    if recipient == sender:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru")
    # if "55"==sender:
    #     print( "Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
    # else:
    #     print( "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')  # ,sender = "university.help@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', )
