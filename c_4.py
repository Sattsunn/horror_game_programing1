# c_2 本の内容
# coding: utf -8
import PySimpleGUI as sg


sg.theme("black")

photo = sg.Image(size=(400,300),filename="./img/start.png")
text = sg.Text("コレカラズットイッショダネ")
square = sg.Canvas(size=(400,50))

def badend_girl():
    # ------------ サブウィンドウ作成 ------------
    c_layout = [
                     [photo], 
                     [text],
                     ]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)