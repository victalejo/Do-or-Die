import PySimpleGUI as sg


def login():
    sg.theme("Material2")

    layout = [[sg.Image(r'Logo fondo transparente.png')],
              [sg.Text('Bienvenido a Do or Die', justification="center", size=(26, 1), font=("Magistral Regular", 24))],
              [sg.Text('Inicio de Sesión', justification="center", size=(41, 2), font=("Magistral Regular", 16))],
              [sg.Input(tooltip="Correo IQ Option", key="correo", size=(27, 2), font=("Arial", 12)),
               sg.Input(tooltip="Contraseña IQ Option", key="contrasena", size=(27, 2), password_char="•",
                        font=("Arial", 12))],
              [sg.Button("Iniciar", button_color="green", key="iniciar_sesion", font=("Magistral Regular", 12),
                         size=(10, 1))]]

    window = sg.Window('Do or Die', layout, element_justification="c", icon=r"do_or_die.ico", no_titlebar=True)
    while True:
        event, values = window.read()
        print(event)
        print(values)
        if event == "iniciar_sesion":
            if values["correo"] == "" and values["contrasena"] == "":
                sg.popup("Por favor, ingrese correo y contraseña", no_titlebar=True, background_color="LightCyan")
            elif values["correo"] == "":
                sg.popup("Por favor, ingrese un correo.", no_titlebar=True, background_color="LightCyan")
            elif values["contrasena"] == "":
                sg.popup("Por favor, ingrese una contraseña.", no_titlebar=True, background_color="LightCyan")
            else:
                break
    window.close()


def principal():
    sg.theme("Material2")
    layout = [[sg.Image(r'Logo fondo transparente.png')],
              [sg.Text('Bienvenido Victor Alejandro Cano Jaramillo', justification="center", size=(35, 1),
                       font=("Magistral Regular", 15))],
              [sg.Text('Cuenta', justification="left", size=(7, 1), font=("Magistral Regular", 13)),
               sg.Radio(group_id="cuenta", text="Demo", font=("Magistral Regular", 13), size=(5, 1)),
               sg.Radio(group_id="cuenta", text="Real", font=("Magistral Regular", 13), size=(8, 1)),
               sg.Text("Saldo: $1000 GBP", font=("Magistral Regular", 13), size=(20, 1), justification="r")],
              [sg.Input(tooltip="Correo IQ Option", key="correo", size=(27, 2), font=("Arial", 12)),
               sg.Input(tooltip="Contraseña IQ Option", key="contrasena", size=(27, 2), password_char="•",
                        font=("Arial", 12))],
              [sg.Button("Iniciar", button_color="green", key="iniciar_sesion", font=("Magistral Regular", 12),
                         size=(10, 1))]]

    window = sg.Window('Do or Die', layout, element_justification="c", icon=r"do_or_die.ico", no_titlebar=False)
    while True:
        event, values = window.read()


if __name__ == '__main__':
    login()
    principal()
