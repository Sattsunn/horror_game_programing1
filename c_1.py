# c_1 本を見つけた時の行動
# coding: utf -8
import PySimpleGUI as sg
sg.theme("black")

photo = sg.Image(size=(400,300),filename="./img/start.png")
text = sg.Text("本を見つけた", key="text",border_width=1)
text_book = sg.Text("本を見つけた", key="text",border_width=1)
square = sg.Canvas(size=(400,50))
button_backa = sg.Button("戻る",key="c1a")
button_backb = sg.Button("戻る",key="c1b")
button_book = sg.Button("読んでみる",key="c1c")

def make_c_1a():
    # 棚をあさる
    c_layout = [
                     [photo], 
                     [text],   
                     [button_backa]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)


def make_c_1b():
    # カレンダーを見る
    c_layout = [
                     [photo], 
                     [text] ,  
                     [button_backb]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)


def make_c_1c():
    # 机の下を見る⇒ほんを見る
    c_layout = [
                     [photo], 
                     [text_book] ,  
                     [button_book]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)
