# coding: utf -8
import PySimpleGUI as sg

sg.theme("black")

photo = sg.Image(size=(400,300),filename="./img/start.png")
start1_text = sg.Text("「なんだ、あれ、、、」\n俺は見たこともない異形の生物に出会った。恐怖で体が震えていた、\n（怖い怖い怖い、何だあれ、、）")
square = sg.Canvas(size=(400,50))
button = sg.Button("A 走って逃げる",key="a")
button2 = sg.Button("B 物陰に隠れる",key="b")
button3 = sg.Button("C 近づく",key="c0")

def make_start1():
    start1_layout = [
          [photo], 
          [start1_text],  
          [button],
          [button2],
          [button3]]
    
    return sg.Window("ホラーゲーム", start1_layout,size=(500,600), finalize=True)

