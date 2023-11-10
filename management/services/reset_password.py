from utils.helpers import send_sms


def send_otp(phone_number, otp):
    """ Сервис востановления пароля """
    text = f"""
        ПОПЫТКА ВХОДА!!!
        Ваш новый пароль: {otp}
        Просим вас изменить пароль после входа!
    """
    return send_sms(phone_number, text)
