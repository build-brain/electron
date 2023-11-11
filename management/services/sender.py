from utils.helpers import send_sms


def send_reset(phone_number, password):
    """ Сервис востановления пароля """
    text = f"""
        ПОПЫТКА ВХОДА!!!
        Ваш новый пароль: {password}
        Просим вас изменить пароль после входа!
    """
    return send_sms(phone_number, text)


def send_otp(phone_number, otp):
    """ Сервис востановления пароля """
    text = f"Ваш код верификации: {otp}!"
    return send_sms(phone_number, text)
