import PySimpleGUI as sg

def epi():
    # ------------ サブウィンドウ作成 ------------
    prologue_layout = [[sg.Text("-PROLOGUE-")],
                       [sg.Text("20xx年11月1日15時")],
                       [sg.Text("目の前が真っ暗になり目が覚めると元の場所に戻っていた。\nあれは何だったのだろうか\n")],
                       [sg.Button("next" ,key = "epi")]]
    return sg.Window("ホラーゲーム", prologue_layout,size=(300,450), finalize=True)