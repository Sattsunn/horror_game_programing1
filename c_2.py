# c_2 本の内容
# coding: utf -8
import PySimpleGUI as sg


sg.theme("black")

photo = sg.Image(size=(400,300),filename="./img/start.png")
text = sg.Text("「うわああああああああ！！！」\n突然目の前に現れた傷だらけの女の子に驚いて思わず俺は叫んだ。\n「はやく戻らないと帰れなくなっちゃうよ、、」\n「ここは時間の流れが遅いから、、」\n「あなたはいつから来たの？」\nそういって女の子は俺に時計を渡してきた。日付と時間がわかるものだ。")
square = sg.Canvas(size=(400,50))
button = sg.Button("A 近くの木材で女の子に殴りかかる",key="c2_a")
button2 = sg.Button("B 時計をさわる",key="c2_b")
button3 = sg.Button("C 走って逃げる",key="c2_c")

def make_c_2():
    # ------------ サブウィンドウ作成 ------------
    c_layout = [
                     [photo], 
                     [text],
                     [button],
                     [button2],
                     [button3]]
    
    return sg.Window("ホラーゲーム", c_layout,size=(500,600), finalize=True)