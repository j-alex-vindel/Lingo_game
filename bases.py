import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")],[sg.Button('4 Letter Lingo'),sg.Text('To play four letter words')],
          [sg.Text('Enter your guess'), sg.Input(),sg.Button('Play')]]

# Create the window
window = sg.Window("Demo", layout,margins=(100,50))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    elif event == '4 Letter Lingo':
        sg.popup("Let's play Lingo!")
    elif event == 'Play':
        sg.popup(values[0][0],'-',values[0][1],'-',values[0][2],'-',values[0][3])

window.close()
