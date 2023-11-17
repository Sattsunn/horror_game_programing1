# c_0 知らない部屋での行動
# coding: utf -8
import PySimpleGUI as sg


sg.theme("black")

photo = sg.Image(size=(400,300),filename="./img/room.png")
text = sg.Text("目が覚めると知らない部屋の中にいた、、\nうす暗い部屋だ。何かが動いている気がする。\nなんとも言えない気持ち悪さをずっと感じている。\n俺は部屋を探索してみることにした。")
square = sg.Canvas(size=(400,50))
button = sg.Button("A 棚をあさる",key="c0_a")
button2 = sg.Button("B カレンダーをみる",key="c0_b")
button3 = sg.Button("C 机の下を見る",key="c0_c")

def room():
    # ------------ サブウィンドウ作成 ------------
    c_layout = [   [photo], 
                   [text],
                   [button],
                   [button2],
                   [button3]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)