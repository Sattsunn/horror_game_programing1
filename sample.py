import PySimpleGUI as sg

sg.theme('DarkGrey5')

game_data = [
    {"image": "scene1.jpg", "text": "暗い部屋にいる。何かが動いている気がする。", "choices": ["開ける", "叫ぶ"], "next_scene": [1, 2]},
    {"image": "scene2.jpg", "text": "部屋が明るくなり、見知らぬ人が立っている。", "choices": ["話しかける", "逃げる"], "next_scene": [2, 3]},
    {"image": "scene3.jpg", "text": "人物から何かを受け取る。", "choices": ["受け取る", "拒否する"], "next_scene": [3, 4]},
    {"image": "scene4.jpg", "text": "あなたは...。", "choices": []},
]

current_scene = 0

layout = [
    [sg.Image(key='-IMAGE-')],
    [sg.Text("", size=(50, 3), key='-TEXT-')],
    [sg.Button(choice, key=f'-CHOICE-{i}-') for i, choice in enumerate(game_data[current_scene]["choices"])],
]

window = sg.Window("Horror Interactive Game", layout, finalize=True)
window['-IMAGE-'].update(filename=game_data[current_scene]["image"])
window['-TEXT-'].update(value=game_data[current_scene]["text"])

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event.startswith('-CHOICE-'):
        choice_index = int(event.split('-')[-2])
        current_scene = game_data[current_scene]["next_scene"][choice_index]

        if current_scene < len(game_data):
            window['-IMAGE-'].update(filename=game_data[current_scene]["image"])
            window['-TEXT-'].update(value=game_data[current_scene]["text"])
            window['-CHOICE-0-'].update(text=game_data[current_scene]["choices"][0])
            window['-CHOICE-1-'].update(text=game_data[current_scene]["choices"][1])
        else:
            sg.popup_ok('ゲーム終了')
            break

window.close()