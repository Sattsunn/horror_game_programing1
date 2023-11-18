import PySimpleGUI as sg

def make_prologue():
    # ------------ サブウィンドウ作成 ------------
    prologue_layout = [[sg.Text("-PROLOGUE-")],
                       [sg.Text("20xx年11月1日15時")],
                       [sg.Text("学校からの帰り道突然激しい頭痛を感じ\n目が覚めると見知らぬ土地にいた。何が起\nこったのか理解できず不安に思っていると\n遠くに黒い影が見えた。ひとまず\n俺はその影に近づくことにした。")],
                       [sg.Button("next" ,key = "prol")]]
    return sg.Window("ホラーゲーム", prologue_layout,size=(300,450), finalize=True)