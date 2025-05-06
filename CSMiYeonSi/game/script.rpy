# 이 파일에 게임 스크립트를 입력합니다.
init python:
    flash = Fade(0.1, 0.1, 0.1, color="#ffffff")

# image 문을 사용해 이미지를 정의합니다.
image cs101 default = "images/char/cs101_default.png"
image bg home = "images/bg/home.png"
image bg blue = "images/bg/blue.png"
image bg black = "images/bg/black.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define unknown = Character("???", color="#ffffff")
define cs101 = Character("프밍기", color="#00ff00", image="cs101", likeability=50)
define cs204 = Character("데이타구조", color="#ff0000", likeability=0)
define cs206 = Character("이산구조", color="#0000ff", likeability=0)

# 여기에서부터 게임이 시작합니다.
label start:
    $ heroine_list = []  # 히로인 목록 초기화
    $ player_name = ""  # 플레이어 이름 초기화
    # 플레이어 데이터 받기
    label player_name_input:
        scene bg blue
        $ player_name = renpy.input("이름을 입력하세요.")
        $ player_name = player_name.strip()  # 공백 제거
        if len(player_name) < 3 or len(player_name) > 10:
            # 이름이 3자 이상, 10자 이하인지 확인
            "이름은 3자 이상, 10자 이하로 입력해주세요."
            jump player_name_input
        "이름은 [player_name]이(가) 맞나요?"
        menu:
            "네!":
                pass
            "아니요!":
                jump player_name_input

    scene bg black with fade
    unknown "..."
    unknown "... [player_name]!"
    unknown "... [player_name], 일어나!"

    menu:
        "일어난다.":  
            jump tutorial

    label tutorial:
        scene bg home with flash
        show cs101 default
        cs101 "왜 이제야 일어나는거야! 입학식부터 늦으면 어쩌려구!"
        cs101 "이씨, 뛰어야 하게 생겼잖아..."
        menu:
            "\"미안해...\"":
                cs101 "됐어! 빨리 갈 준비나 해."
                hide cs101
                "아아, 알람이 울리지 않아서 프밍기가 깨워줄 때까지 일어나지 못했구나..."
                "빨리 준비하고 나가야겠다."
            "\"먼저 가지.\"":
                cs101 "...!"
                cs101 "무슨 소리야! 어떻게 나 혼자 가!"
                cs101 "빨리 갈 준비나 하고 나와!"
                hide cs101
                scene bg black 
                "- 쾅!"
                "... 흠."
        scene bg black
        "히로인 목록에 프밍기가 추가되었습니다."
        $ heroine_list.append(cs101)


    return
