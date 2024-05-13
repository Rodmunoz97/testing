# Functions


def get_input():
    """
    This function asks the user for a new password, which should be confirmed.
    :return:
    """
    ui = input("Please enter a new password: ")
    ui_confirm = input("Please confirm your new password: ")
    if ui == ui_confirm:
        return ui
    else:
        print("Passwords dont match.")
        return None


def check_strength(password):
    allowed_symbols = "!#$%&/()=?¡*-_+<>.:;"
    numbers = "01234567890"
    letters_caps = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    letters_low = "qwertyuiopasdfghjklñzxcvbnm"
    is_safe = [False, False, False, False, False]
    error_message = ["Password must be longer than 8 Characters.",
                     "Password must contain at least one of the following symbols: " + allowed_symbols,
                     "Password must contain at least one number.",
                     "Password must contain at least one uppercase letter.",
                     "Password must contain at least one lowercase letter."]
    if len(password) > 7:
        is_safe[0] = True
    for char in password:
        for symbol in allowed_symbols:
            if char == symbol:
                is_safe[1] = True
    for char in password:
        for symbol in numbers:
            if char == symbol:
                is_safe[2] = True
    for char in password:
        for symbol in letters_caps:
            if char == symbol:
                is_safe[3] = True
    for char in password:
        for symbol in letters_low:
            if char == symbol:
                is_safe[4] = True
    safeness = 0
    for item in is_safe:
        if item is True:
            safeness += 2
    print("Safety level: {}".format(safeness))
    if safeness == 0:
        safeness = "Password is stupidly unsafe."
    elif safeness == 2:
        safeness = "Cmon, you can do better than that."
    elif safeness == 4:
        safeness = "Password is a bit unsafe."
    elif safeness == 6:
        safeness = "Strong password, but not strong enough"
    elif safeness == 8:
        safeness = "Password looking real nice, just missing one component."
    elif safeness == 10:
        safeness = "PASSWORD PERFECTION!"
    print(safeness)

    for i in range(len(is_safe)):
        if is_safe[i] is False:
            print(error_message[i])

# Main


user_password = get_input()
if user_password:
    check_strength(user_password)
