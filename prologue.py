import PySimpleGUI as sg

def make_prologue():
    # ------------ サブウィンドウ作成 ------------
    prologue_layout = [[sg.Text("-PROLOGUE-")],
                       [sg.Text("20xx年11月1日")],
                       [sg.Text("学校からの帰り道突然激しい頭痛を感じ\n目が覚めると見知らぬ土地にいた.何が起こっ\nたのか理解できず不安に思っていると、遠くに黒い影\nが見えた。どうしてよいかわからなかったので俺はその影\nに近づいて行った。")],
                       [sg.Button("next" ,key = "prol")]]
    return sg.Window("ホラーゲーム", prologue_layout,size=(300,450), finalize=True)