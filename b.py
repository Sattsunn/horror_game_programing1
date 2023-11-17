#別世界に、お化けが出たから物陰に隠れた
#b (物陰に隠れる)
#隠れる
# coding: utf -8
import PySimpleGUI as sg


sg.theme("black")

#b(物陰に隠れる)
photo = sg.Image(size=(500,500),filename="./img/1monokage.png")
button = sg.Button("走って逃げる",key="a")
button2 = sg.Button("このまま隠れる",key="b")
button3 = sg.Button("武器を探す",key="c")

#a(走って逃げる)b(このまま隠れる)c(武器を探す)
def make_b_1():
    # ------------ サブウィンドウ作成 ------------
    b_layout = [[photo],
          [sg.Text("ここではお化けに見つかってしまいそう！")],   
          [button],
          [button2],
          [button3]]
    
    return sg.Window("ホラーゲーム", b_layout,size=(500,800), finalize=True)




#ba(隠れる、走って逃げる)
photo_ba = sg.Image(size=(500,500),filename="./img/2oikakeru.png")
button_baa = sg.Button("そのまま走る",key="baa")
button_bab = sg.Button("疲れたから休む",key="bab")
button_bac= sg.Button("隠れる",key="bac")

#a(そのまま走る)b(疲れたから休む)c(隠れる)
def make_b_a():
    # ------------ サブウィンドウ作成 ------------
    ba_layout = [[photo_ba],
          [sg.Text("お化けが追いかけてきた！")],   
          [button_baa],
          [button_bab],
          [button_bac]]
    
    return sg.Window("ホラーゲーム", ba_layout,size=(700,700), finalize=True)



#bb(隠れる、このまま隠れる)
photo_bb = sg.Image(size=(500,500),filename="./img/2oikakeru.png")
button_bba = sg.Button("戦う",key="bba")
button_bbb = sg.Button("建物を探す",key="bbb")


#a(戦う)b(建物を探す)
def make_b_b():
    # ------------ サブウィンドウ作成 ------------
    bb_layout = [[photo_bb],
          [sg.Text("お化けに見つかった！")],   
          [button_bba],
          [button_bbb]]
    
    return sg.Window("ホラーゲーム", bb_layout,size=(700,700), finalize=True)


#bc(隠れる、武器を探す)
photo_bc = sg.Image(size=(400,300),filename="./img/4buki.png")
button_bca = sg.Button("短いナイフで戦う",key="bca")
button_bcb = sg.Button("おので戦う",key="bcb")
button_bcc= sg.Button("長い刀で戦う",key="bcc")

#a(ナイフ)b(おの)c(刀)
def make_b_c():
    # ------------ サブウィンドウ作成 ------------
    bc_layout = [[photo_bc],
          [sg.Text("")],   
          [button_bca],
          [button_bcb],
          [button_bcc]]
    
    return sg.Window("ホラーゲーム", bc_layout,size=(700,700), finalize=True)

#baa(隠れる、走って逃げる、そのまま走る)
photo_baa = sg.Image(size=(500,500),filename="./img/3tatemono.png")
button_baaa = sg.Button("建物に入る",key="baaa")
button_baab = sg.Button("まだ走る",key="baab")

#baa(建物に入る、まだ走る)
def make_b_aa():
    # ------------ サブウィンドウ作成 ------------
    baa_layout = [[photo_baa],
          [sg.Text("建物を発見！")],   
          [button_baaa],
          [button_baab]]
    
    return sg.Window("ホラーゲーム", baa_layout,size=(700,700), finalize=True)

#bac(隠れる、走って逃げる、隠れる)
photo_bac = sg.Image(size=(500,500),filename="./img/4buki.png")
button_baca = sg.Button("拾って逃げる",key="baca")
button_bacb = sg.Button("その場で戦う",key="bacb")

#bac(拾って逃げる、その場で戦う)
def make_b_ac():
    # ------------ サブウィンドウ作成 ------------
    bac_layout = [[photo_bac],
          [sg.Text("武器を発見！")],   
          [button_baaa],
          [button_baab]]
    
    return sg.Window("ホラーゲーム", bac_layout,size=(700,700), finalize=True)

#bbb(隠れる、このまま隠れる、建物を探す)
photo_bbb = sg.Image(size=(500,500),filename="./img/2oikakeru.png")
button_bbba= sg.Button("入る",key="bbba")
button_bbbb = sg.Button("入らない",key="bbbb")

def make_b_bb():
        # ------------ サブウィンドウ作成 ------------
    bbb_layout = [[photo_bac],
          [sg.Text("入れそうな建物を発見！")],   
          [button_bbba],
          [button_bbbb]]

    return sg.Window("ホラーゲーム", bbb_layout,size=(700,700), finalize=True)







photo_clear = sg.Image(size=(500,500),filename="./img/10door.png")
button_c = sg.Button("入る！",key="clear")

def clear():
    
    clear_layout = [[photo_clear],
                    [sg.Text("扉があらわれた！✨")],
                    [button_c]]
      
    return sg.Window ("ホラーゲーム", clear_layout,size=(700,700), finalize=True)


photo_gameover = sg.Image(size=(1000,1000),filename="./img/gameover.png")

def GAMEOVER():
    gameover_layout = [[sg.Text("ゲームオーバー!")]
                       [photo_gameover]]

    return sg.Window ("ホラーゲーム", gameover_layout, size=(800,600), finalize=True)












