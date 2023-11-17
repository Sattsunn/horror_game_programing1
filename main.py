import PySimpleGUI as sg
import time
# ページの読み込み
import prologue,start1,a,b,c_0,c_1,c_2,c_3,c_4,epilogue
sg.theme("black")

def make_main():
    # ------------ メインウィンドウ作成 ------------
    main_layout = [[sg.Text("ハロウィンからの脱出",size=(450,200))],
            [sg.Button("GAMESTART")],
            [sg.Button("Close")]]
    return sg.Window("ホラーゲーム", main_layout, size=(500, 300),finalize=True)



# 最初に表示するウィンドウを指定する。
window = make_main()
print("hoge")

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # スタートボタンが押された場合
    elif event == "GAMESTART":
        # メインウィンドウを閉じて、プロローグ画面を作成して表示する
        window.close()
        window = prologue.make_prologue()

    # Closeボタンが押された場合
    elif event == "Close":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        break

    # prologue
    elif event == "prol":
        window.close()
        window = start1.make_start1()

    # start1

    # Aの処理
    elif event == "a":
        window.close()
        window_a = a.make_a_1()

    elif event == "next":
        window_a.close() 
        window_z = a.make_a_2()
        while True:
            event_z, values_z = window_z.read()
            if event_z == sg.WIN_CLOSED:
                break
            if event_z == "a":
                window_z.close()
                window_b = a.make_a_3()
                while True:
                    event_b, value_b = window_b.read()
                    if event_b == sg.WIN_CLOSED:
                        break
                    if event_b == "next2":
                        window_b.close()
                        window_c = a.make_a_4()
                        while True:
                            event_c, value_c = window_c.read()
                            if event_c == sg.WIN_CLOSED:
                                break
                            if event_c == "next3":
                                window_c.close()
                                window_d = a.gameover()
                                while True:
                                    event_d, value_d = window_d.read()
                                    if event_d == sg.WIN_CLOSED or "close":
                                        break
                                
            if event_z == "b":
                window_z.close()
                window_e = a.make_a_5()
                while True:
                    event_e, value_e = window_e.read()
                    if event_e == sg.WIN_CLOSED:
                        break
                    if event_e == "next4":
                        window_e.close()
                        window_f = a.make_a_6()
                        while True:
                            event_f, value_f = window_f.read()
                            if event_f == sg.WIN_CLOSED:
                                break
                            if event_f == "next5":
                                window_f.close()
                                window_g = a.make_a_7()
                                while True:
                                    event_g, value_g = window_g.read()
                                    if event_g == sg.WIN_CLOSED:
                                        break
                                    if event_g == "ride":
                                        window_g.close()
                                        window_h = a.make_a_8()
                                        while True:
                                            event_h, value_h = window_h.read()
                                            if event_h == sg.WIN_CLOSED:
                                                break
                                            if event_h == "next6":
                                                window_h.close()
                                                window_i = a.make_a_9()
                                                while True:
                                                    event_i, value_i = window_i.read()
                                                    if event_i == sg.WIN_CLOSED:
                                                        break
                                                    if event_i == "next7":
                                                        window_i.close()
                                                        window_j = a.make_a_10()
                                                        while True:
                                                            event_j, value_j = window_j.read() 
                                                            if event_j == sg.WIN_CLOSED:
                                                               break
                                                            if event_j == "stay":
                                                               window_j.close()
                                                               window_k = a.make_a_11()
                                                               while True:
                                                                   event_k, value_k = window_k.read()
                                                                   if event_k == sg.WIN_CLOSED:
                                                                       break
                                                                   if event_k == "next8":
                                                                       window_k.close()
                                                                       window_l = a.make_a_12()
                                                                       while True:
                                                                           event_l, value_l = window_l.read()
                                                                           if event_l == sg.WIN_CLOSED:
                                                                               break
                                                                           if event_l == "next9":
                                                                               window_l.close()
                                                                               window_m = a.gameover()
                                                                               while True:
                                                                                   event_m, value_m = window_m.read()
                                                                                   if event_m == sg.WIN_CLOSED or "close":
                                                                                       break

                                                            if event_j == "run":
                                                               window_j.close()
                                                               window_n = a.make_a_13()
                                                               while True:
                                                                   event_n, value_n = window_n.read()
                                                                   if event_n == sg.WIN_CLOSED:
                                                                       break
                                                                   if event_n == "next10":
                                                                       window_n.close()
                                                                       window_o = a.make_a_14()
                                                                       while True:
                                                                           event_o, value_o = window_o.read()
                                                                           if event_o == sg.WIN_CLOSED:
                                                                               break
                                                                           if event_o == "go":
                                                                               window_o.close()
                                                                               window_p = a.make_a_15()
                                                                               while True:
                                                                                   event_p, value_p = window_p.read()
                                                                                   if event_p == sg.WIN_CLOSED:
                                                                                       break
                                                                                   if event_p == "next11":
                                                                                       window_p.close()
                                                                                       window_q = a.gameover()
                                                                                       while True:
                                                                                           event_q, value_q = window_q.read()
                                                                                           if event_q == sg.WIN_CLOSED or "close":
                                                                                               break
                                                                           if event_o == "rest":
                                                                               window_o.close()
                                                                               window_r = a.make_a_16()
                                                                               while True:
                                                                                   event_r, value_r = window_r.read()
                                                                                   if event_r == sg.WIN_CLOSED:
                                                                                       break
                                                                                   if event_r == "next12":
                                                                                       window_r.close()
                                                                                       window_s = a.make_a_17()
                                                                                       while True:
                                                                                           event_s, value_s = window_s.read()
                                                                                           if event_s == sg.WIN_CLOSED:
                                                                                               break
                                                                                           if event_s == "fight":
                                                                                               window_s.close()
                                                                                               window_t = a.make_a_18()
                                                                                               while True:
                                                                                                   event_t, value_t = window_t.read()
                                                                                                   if event_t == sg.WIN_CLOSED:
                                                                                                       break
                                                                                                   if event_t == "next13":
                                                                                                       window_t.close()
                                                                                                       window_u = a.gameover()
                                                                                           if event_s == "river":
                                                                                               window_s.close()
                                                                                               window_v = a.make_a_19()
                                                                                               while True:
                                                                                                   event_v, value_v = window_v
                                                                                                   if event_v == sg.WIN_CLOSED:
                                                                                                       break
                                                                                                   if event_v == "next14":
                                                                                                       window_v.close()
                                                                                                       window_w = a.make_a_20()
                                                                                                       while True:
                                                                                                           event_w, value_w = window_w.read()
                                                                                                           if event_w == sg.WIN_CLOSED:
                                                                                                               break
                                                                                                           if event_w == "next15":
                                                                                                               window_w.close()
                                                                                                               window_x = a.gameclear()
                                                                                                               while True:
                                                                                                                   event_x, value_x = window_x.read()
                                                                                                                   if event_x == sg.WIN_CLOSED or "close2":
                                                                                                                       break

                                                                                    
                                    if event_g == "refuse":
                                        window_g.close()
                                        window_y = a.make_a_21()
                                        while True:
                                            event_y, value_y = window_y.read()
                                            if event_y == sg.WIN_CLOSED:
                                                break
                                            if event_y == "next16":
                                                window_y.close()
                                                window_a2 = a.make_a_22()
                                                while True:
                                                    event_a2, value_a2 = window_a2.read()
                                                    if event_a2 == sg.WIN_CLOSED:
                                                        break
                                                    if event_a2 == "next17":
                                                        window_a2.close()
                                                        window_b2 = a.gameover()
                                                        while True:
                                                            event_b2, value_b2 = window_b2.read()
                                                            if event_b2 == sg.WIN_CLOSED or "close":
                                                                break

    # Bの処理
    elif event == "b":
        window.close()
        window = b.make_b_1()
        window = b.make_b_1()


    #ba(隠れる、走って逃げる)
    if event == "a":
        window.close()
        window = b.make_b_a()
        while True:
            event, values = window.read()
            #baaそのまま走る
            if event == "baa":
                window.close()
                window = b.make_b_aa()
                while True:
                    event, values = window.read()
                    #baaa
                    if event == "baaa":
                        window.close()
                        window = b.clear()

                    #baab
                    elif event == "baab":
                        window.close()
                        window = b.GAMEOVER()

            #bab疲れたから休憩する
            elif event == "bab":
                window.close()
                window = b.GAMEOVER()

            #bac隠れる
            elif event == "bac":
                window.close()
                window = b.make_b_ac()
                while True:
                    event, values = window.read()
                    #baca
                    if event == "baca":
                        window.close()
                        window = b.make_b_aa()
                        while True:
                            event, values = window.read()
                            #baaa
                            if event == "baaa":
                                window.close()
                                window = b.clear()

                            #baab
                            elif event == "baab":
                                window.close()
                                window = b.GAMEOVER()


                    #bacb
                    elif event == "bacb":
                        window.close()
                        window = b.GAMEOVER()

                    window.close()




#b,b(隠れる、隠れる)
    elif event == "b":
        window.close()
        window = b.make_b_b()
        while True:
            event, values = window.read()
            #戦う
            if event == "bba":
                window.close()
                window = b.GAMEOVER()
            #建物探す
            elif event == "bbb":
                window.close()
                window = b.make_b_aa()
                while True:
                    event, values = window.read()
                    #baaa
                    if event == "baaa":
                        window.close()
                        window = b.clear()

                    #baab
                    elif event == "baab":
                        window.close()
                        window = b.GAMEOVER()


#b,c()
    elif event == "c":
        window.close()
        window = b.make_b_c()
        while True:
            event, values = window.read()
            #短い刀
            if event == "bca":
                window.close()
                window = b.GAMEOVER()
            #おの
            elif event == "bcb":
                window.close()
                window = b.clear()

            #戦いに挑む　#ゲームオーバー
            elif event == "bcc":
                window.close()
                window = b.clear()



            window.close()


    
    # Cの処理
    
    elif event == "c":
        # 近づく
        sg.popup("俺は化け物に近づいてみることにした、、、\n化け物が俺に気づいた瞬間激しい金切り声と思い出せないほどの恐怖を感じ俺の意識はなくなっていた、、、、")
        window.close()
        window = c_0.room()

    # c_0
    elif event == "c0_a":
        # 棚をあさる
        window.close()
        window = c_1.make_c_1a()

    elif event == "c0_b":
        # カレンダーを見る
        window.close()
        window = c_1.make_c_1b()

    elif event == "c0_c":
        # 机の下を見る
        window.close()
        window = c_1.make_c_1c()
        
    # c_1


    elif event == "c1c":
        window.close()
        sg.popup("ハロウィン\n")
        sg.popup('たすけて', text_color="red") 
        sg.popup('たすけて', text_color="red",) 
        sg.popup('たすけて', text_color="red") 
        window = c_2.make_c_2()
        
    elif event == "c2_b":
        window.close()
        window= c_3.clock()
    
    elif event == "done":
        if int(values["month"]) == 11 and int(values["date"])==1 and int(values["time"])== 15:
            sg.popup("なぁんだ、戻る場所があるのか、、、残念\n次来たらもう戻れないからね")
            window.close()
            window = epilogue.epi()

        else:
            window.close()
            sg.popup("どこから来たのかわからないんだ、、、")
            window = c_4.badend_girl()
            time.sleep(2)
            sg.popup("GAMEOVER....")


    elif event == "epi":
        window.close()
        sg.popup("GAMECLEAR!!")

   
window.close()