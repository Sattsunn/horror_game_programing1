# c_3 日時の入力
# coding: utf -8
import PySimpleGUI as sg


sg.theme("black")

time = sg.Input(key= "time",size=(3))
month = sg.Input(key= "month",size=(3))
date = sg.Input(key= "date",size=(3))
button = sg.Button("決定",key="done")

def clock():
    # ------------ サブウィンドウ作成 ------------
    c_layout = [   
                   [month,sg.Text("月"),date,sg.Text("日"),time,sg.Text("時")],
                   [button]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(400,300), finalize=True)