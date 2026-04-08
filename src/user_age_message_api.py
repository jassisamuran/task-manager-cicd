def send_age_message(age):
    if age < 18:
        return "User is not eligible."
    else:
        return "User is eligible."