# coding: utf -8
import PySimpleGUI as sg

sg.theme("black")


text = sg.Text("テキスト",size=(400,50), key="text")
square = sg.Canvas(size=(400,50))
close_button = sg.Button("閉じる",key="close")
close_button2 = sg.Button("閉じる",key="close2")
button = sg.Button("大声で呼びかけてみる",key="a_a")
button2 = sg.Button("近くの民家を回ってみる",key="a_b")
button3 = sg.Button("乗る",key="ride")
button4 = sg.Button("断る",key="refuse")
button5 = sg.Button("このまま乗る",key="stay")
button6 = sg.Button("降りて逃げる",key="run")
button7 = sg.Button("さらに奥へ進む",key="go")
button8 = sg.Button("その場で少し休憩する",key="rest")
button9 = sg.Button("最後の力を振り絞って戦う",key="fight")
button10 = sg.Button("川へ飛び込む",key="river")
next_button = sg.Button("次へ",key="next")
next_button2 = sg.Button("次へ",key="next2")
next_button3 = sg.Button("次へ",key="next3")
next_button4 = sg.Button("次へ",key="next4")
next_button5 = sg.Button("次へ",key="next5")
next_button6 = sg.Button("次へ",key="next6")
next_button7 = sg.Button("次へ",key="next7")
next_button8 = sg.Button("次へ",key="next8")
next_button9 = sg.Button("次へ",key="next9")
next_button10 = sg.Button("次へ",key="next10")
next_button11 = sg.Button("次へ",key="next11")
next_button12 = sg.Button("次へ",key="next12")
next_button13 = sg.Button("次へ",key="next13")
next_button14 = sg.Button("次へ",key="next14")
next_button15 = sg.Button("次へ",key="next15")
next_button16 = sg.Button("次へ",key="next16")
next_button17 = sg.Button("次へ",key="next17")


def make_a_1():
    # ------------ サブウィンドウ作成 ------------
    a_layout = [ 
        [sg.Image(size=(650,500),filename="./img/re_town.png")],
        
                [sg.Text("必死に逃げた。\n(あれは一体何だったのだろう・・・早いところ家に帰らないと・・・)")],   
          [next_button]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_2():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/room.png")],
                [sg.Text("とりあえず人を見つけてここがどこなのか聞いてみよう")],   
          [button],[button2]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_3():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("???｢・・・・・・・！｣\n遠くから声が聞こえる。いろいろ聞けるかも。\n行ってみよう。")],   
          [next_button2]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_4():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("｢・・・ヨンダ？｣",size=(20, 1),text_color="red")],   
           [next_button3]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def gameover():
    a_layout = [ 
                [sg.Text("GAMEOVER",font=(16),text_color="red")],
                [close_button]   
            ]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_5():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("...しばらくいろいろな家を回ってみたが全く人の気配が感じられない。一体この町はどうなっているのだろうか。\n携帯も確認したが圏外で、もはや歩く以外どうすることもできなかった...")],   
           [next_button4]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_6():
    a_layout = [ 
        [sg.Image(size=(650,500),filename="./img/re_town.png")],          [sg.Text("大分歩いたがまだ俺が知っている町並みにはほど遠い。\nお腹も空いてきた。いつになったら帰れるのだろうか...\nそんなことを考えていたそのとき、正面から車が走ってきた。")],   
                 [next_button5]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_7():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("その車には若い男が乗っていた。\nどうやらこの男性も起きたときには既にここへ迷い込んでしまったらしい。\n男｢あんたも迷い込んだのか？とりあえずいい隠れ場所あるから乗っていってよ。｣\n...どうする？")],   
           [button3],
           [button4]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_8():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_car.png")],
                [sg.Text("車に乗った俺は男といろいろ話をした。\n男もこの場所は初めてで、人と出会ったのも俺が最初であるという。\n(俺は本当に帰ることができるのだろうか...)そんな不安を募らせながらどんどん車は進んでいくのであった")],   
           [next_button6]]
    
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_9():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_car.png")],
                [sg.Text("しばらく車に乗っているうちに違和感を覚えた。\n(...今日突然ここに迷い込んだと言っていたのにどうして車を持っているんだ...？)一度気になりだしたらどんどん疑問が沸いてくる...\n(初めて来た町なのにどうしてこんなにスムーズに運転できているんだ？？本当にこの人は迷い込んだ人...？)",auto_size_text=True)],   
           [next_button7]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(900,600), finalize=True)

def make_a_10():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_car.png")],
                [sg.Text("外を見ると、すでに町からは外れていて草木が生い茂る場所にまできていた。\nこのままついていって大丈夫か...？")],   
           [button5],[button6]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_11():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_house.png.png")],
                [sg.Text("そのまま車に乗ってしばらくしていると小さな民家があった。\n俺｢ここは安全なんだな？｣\n男｢ああ、もう心配することないヨ。｣")],   
           [next_button8]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_12():
    a_layout = [ 
                [sg.Text("｢ニドトネ？｣")],   
           [next_button9]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_13():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_car.png")],
                [sg.Text("(こいつは怪しい...とにかく何か理由をつけて逃げよう。)\n俺｢ちょっと酔ったから外の空気吸っていいか？｣男｢...ああ、行ってこい。｣\n俺は強烈な視線を感じながらも車を出て、死角にまわると一目散に森の中へ逃げた。")],   
           [next_button10]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_14():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("逃げてからしばらく経った。完全に山奥に入ってしまい、道も分からなくなってしまった。\nおまけに雨も降ってきて体力も厳しくなってきていた。\n(とりあえず撒けはしたけど、これからどうしようか...)")],   
           [button7],[button8]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_15():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("さらに奥へ行ってみたが森を抜ける気配は全くない。\n(水も食料もずっと口にしていない...もう...限界だ...)\n意識が遠のいていった.....")],   
           [next_button11]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(500,600), finalize=True)

def make_a_16():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("...休憩を始めて30分経った頃だろうか。遠くからわずかだが歩く音が聞こえてきた。\nすぐさま立ち上がって音のする方を見てみると、あいつがいた。と同時に俺のほうへ走ってきた。\n(まずいまずい...!!)俺は全速力で逃げ出した。")],   
           [next_button12]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_17():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("しばらく逃げていたが距離は開かない。\n後ろを振り返ってみると、あいつは例の運転手の服を着ていた。\n(やっぱあの運転手は...いや、それよりもまずいぞ！)俺の行く先は大きな川によって遮られていた。\n'(こうなったら...!!)")],   
           [button9],[button10]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_18():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("俺は逃げるのをやめて、あいつと向かい合った。\nそして渾身の一撃を食らわそうと大きく拳を振りかぶって...\nここで俺の意識は途絶えた。")],   
           [next_button13]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_19():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_forest.png")],
                [sg.Text("(もう、行くしかない...)俺は川に飛び込んだ。\nあいつはどうやら追いかけるのを諦めたようだ。\nしかし雨も相まって川は激流となっていた。俺は何もできずに流されていく...(意識が...)")],   
           [next_button14]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def make_a_20():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_river.png")],
                [sg.Text("...ふと目が覚めると見慣れた川辺で寝そべっていた。どうやら元の町に戻れたようだ。\n結局なんだったのだろうか。\nどうやらハロウィンの日に失踪する事件が毎年起こっているそうだ...")],   
           [next_button15]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(800,600), finalize=True)

def gameclear():
    a_layout = [ 
                [sg.Text("GAMECLEAR")],   
           [close_button2]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(500,600), finalize=True)

def make_a_21():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("俺はなんだかいやな予感がしたので断ることにした。\n男性｢そうか、乗らないか...だったら...｣")],   
           [next_button16]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(500,600), finalize=True)

def make_a_22():
    a_layout = [ [sg.Image(size=(650,500),filename="./img/re_town.png")],
                [sg.Text("｢ノッテモラウネ？｣",size=(20, 1),text_color="red")],   
           [next_button17]]
      
    return sg.Window("ホラーゲーム", a_layout,size=(500,600), finalize=True)

