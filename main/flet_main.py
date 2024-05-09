import json
from flet import *
from quiz_generator import Quizgen
from analysis_Code import Analysis_Code

class uiMain:
    def __init__(self):
        self.quizGen = Quizgen()
        self.ac = Analysis_Code()

    def main(self,page: Page):
        self.userCode = ''
        async def analCode(e):
            page.go("/analCode")
            self.userCode = user_code_input.value
            ac = await getac(user_code_input.value)
            page.update()
            return ac
        
        async def getAnalCode():
            return self.ac.getAC()
        
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        pb = PopupMenuButton(
            items=[
                PopupMenuItem(ElevatedButton("퀵 정렬")),
                PopupMenuItem(),
                PopupMenuItem(ElevatedButton("삽입 정렬")),
                PopupMenuItem(),
                PopupMenuItem(ElevatedButton("버블 정렬")),
                PopupMenuItem(),
            ]
        )
        
        page.title = "다해 PYTHON 인강"
        page.window_width =1500
        image = Image(src="/assets/image/main_page.png",width=400,height=400,fit=ImageFit.COVER)
        id_TF = TextField(label="아이디를 입력해주세요.")
        quiz = ''
        user_code_input=TextField(label="코드 입력 하세요",multiline=True,suffix=ElevatedButton("답안 제출 하기",on_click=analCode))
                        


        def login_btn(e):
            #로그인 시 강의 선택 화면으로 전환
            page.go("/login")
            page.update()

        def sel_lecture1(e):
            page.go(f"/lecture1")
            page.update()
        def sel_lecture2(e):
            page.go(f"/lecture2")
            page.update()
        def sel_lecture3(e):
            page.go(f"/lecture3")
            page.update()
        def sel_lecture4(e):
            page.go(f"/lecture4")
            page.update()
        def sel_lecture5(e):
            page.go(f"/lecture5")
            page.update()
        def sel_lecture6(e):
            page.go(f"/lecture6")
            page.update()

        async def quizGen(e):
            page.go("/quizGen")
            page.update()
            print("코드 가져오는중")
            quiz = await self.quizGen.getQuiz()
            return quiz
            
        def getQu():
            return self.quizGen.getQ()
        
        async def getac(user_code):
            quiz = getQu()
            return await self.ac.run(quiz=quiz,user_code=user_code)


        page.add(
            Row([
                Image(src = "./assets/image/main_page.png",width=400,height=400,fit=ImageFit.CONTAIN),            
                Text("로그인 화면", size = 20, color=colors.WHITE,bgcolor=colors.BLUE_400,weight=FontWeight.BOLD)
            ]),
            id_TF,
            ElevatedButton("로그인",on_click=login_btn)
            
        )

        #페이지 전환 코드
        async def route_change(e):
            print("Route change:", e.route)
            page.views.clear()
            page.add(
                Container(
                    expand=True,
                    content = Stack(
                        controls= [
                            View(
                                "/settings",
                                [
                                    AppBar(title=Text("파이썬 기초 강의"), bgcolor=colors.SURFACE_VARIANT,),
                                    Text("쉽고 간편하게 배우자 다해 코딩 과외", style="bodyMedium",size=20),
                                    Text("\n\n기초 파이썬 프로그래밍 강의\n기초부터 심화 학습까지"),
                                    #강의 리스트
                                    Row([Text("1주차강의(조건문)"),ElevatedButton(
                                        "1강",
                                        on_click=sel_lecture1
                                    )]),
                                    Row([Text("2주차강의(반복문)"),ElevatedButton(
                                        "2강",
                                        on_click=sel_lecture2
                                    )]),
                                    Row([Text("3주차강의(정렬)"),ElevatedButton(
                                        "3강",
                                        on_click=sel_lecture3
                                    )]),
                                    Row([Text("4주차강의(몰랑)"),ElevatedButton(
                                        "4강",
                                        on_click=sel_lecture4
                                    )]),
                                    Row([Text("5주차강의(하기)"),ElevatedButton(
                                        "5강",
                                        on_click=sel_lecture5
                                    )]),
                                    Row([Text("6주차강의(싫어)"),ElevatedButton(
                                        "6강",
                                        on_click=sel_lecture6
                                    )]),
                                ],
                            )
                        ])
                    )
                )
            if page.route == "/login":
                page.views.append(
                    View(
                        "/",
                        [
                            AppBar(title=Text("파이썬 기초 강의"), bgcolor=colors.SURFACE_VARIANT),
                            Text("쉽고 간편하게 배우자 다해 코딩 과외", style="bodyMedium",size=20),
                            Text("\n\n기초 파이썬 프로그래밍 강의\n기초부터 심화 학습까지"),
                            #강의 리스트
                            Row([Text("1주차강의(변수)"),ElevatedButton(
                                "1강",
                                on_click=sel_lecture1
                            )]),
                            Row([Text("2주차강의(상수)"),ElevatedButton(
                                "2강",
                                on_click=sel_lecture2
                            )]),
                            Row([Text("3주차강의(정렬)"),pb,
                            ]),
                            Row([Text("4주차강의(몰랑)"),ElevatedButton(
                                "4강",
                                on_click=sel_lecture4
                            )]),
                            Row([Text("5주차강의(하기)"),ElevatedButton(
                                "5강",
                                on_click=sel_lecture5
                            )]),
                            Row([Text("6주차강의(싫어)"),ElevatedButton(
                                "6강",
                                on_click=sel_lecture6
                            )]),
                        ],
                    )
                )
            if page.route == "/lecture1":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("1강 변수",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                        ],
                    )
                )
            if page.route == "/lecture2":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("2강 상수",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                        ],
                    )
                )
                
            if page.route == "/lecture3":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("3강 몰수",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                        ],
                    )
                )
                
            if page.route == "/lecture4":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("4강 ",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                        ],
                    )
                )
                
            if page.route == "/lecture5":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("5강 ",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                        ],
                    )
                )
                
            if page.route == "/lecture6":
                page.views.append(
                    View(
                        "/lecture1",
                        [
                            AppBar(
                                title=Text("6강 ",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("여기에 비디오 플레이어 넣으셈"),
                            ElevatedButton("강의 복습 및 퀴즈 풀기", on_click= quizGen)
                        ],
                    )
                )
            
            if page.route == "/quizGen":
                page.views.append(
                    View(
                        "/quizGen",
                        [
                            AppBar(
                                title=Text("강의 복습 및 퀴즈 풀기 ",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text(getQu()),
                            user_code_input,
                        ],
                    )
                )
            if page.route == "/analCode":
                page.views.append(
                    View(
                        "/analCode",
                        [
                            AppBar(
                                title=Text("사용자 코드 분석 결과 ",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            Text("*사용자가 입력한 코드*",size= 22),
                            Text(user_code_input.value),
                            Text("\n*분석 결과*",size= 22),
                            Text(await getAnalCode()),
                        ],
                    )
                )
                
                
            page.update()


        def view_pop(e):
            print("View pop:", e.view)
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)    
        
        page.on_route_change = route_change
        page.on_view_pop = view_pop

if __name__ =="__main__":
    ui = uiMain()
    app(target=ui.main, view=AppView.WEB_BROWSER,assets_dir="assets")


# import json
# from flet import *


# def main(page: Page):
#     page.window_width =800
#     video_list = [VideoMedia("https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4"),
#                   VideoMedia("https://youtu.be/NfULoj5j9Zw"),
#                   VideoMedia('assets/only_code.mp4')]
#     json_data = {
#         "start_timestamp": 1.6666080843585238,
#         "end_timestamp": 4.999824253075571,
#         "text": "이정민\n 깨추\n불구"
#     }


#     # 비디오 컨테이너
#     video_container = Container(
#         content=Video(
#             playlist=video_list,
#             aspect_ratio=16/9,
#             filter_quality=FilterQuality.HIGH,
#             autoplay=False,
#             on_loaded=lambda e: print("Video loaded")
#         ),
#         width="70%",
#         height="100%"

#     )
#     # 재생 목록 컨테이너
#     playlist_container = Container(
#         content=Column([
#             TextField(value="재생목록", text_align=TextAlign.CENTER),
#             ElevatedButton(text="어깨"),
#             ElevatedButton(text="척추"),
#             ElevatedButton(text="깨추"),
#         ]),
#         width="30%",
#         height="100%"

#     )

#     # 버튼 컨테이너
#     button_container = Container(
#         content=Row([
#             ElevatedButton(text="이전 강의", width=200),
#             TextField(value="시청하기", text_align=TextAlign.CENTER),
#             ElevatedButton(text="다음 강의", width=200),
#         ]),
#         width="70%",  # 페이지의 70%를 차지하도록 설정
#         height="20%",  # 페이지의 20%를 차지하도록 설정
#         alignment=MainAxisAlignment.CENTER
#     )

#     # 텍스트 컨테이너
#     text_container = Container(
#         content=Text(json_data, text_align=TextAlign.CENTER),
#         width="30%",  # 텍스트 컨테이너의 너비를 화면 너비에 맞게 설정
#         height="30%"   # 페이지의 절반 높이를 차지하도록 설정
#     )

#     # 페이지에 컨테이너 추가
#     page.add(
#         Row([
#             Text("이학진 병신새끼 뒤져라"),
#             playlist_container  # 비디오 아래에 텍스트 컨테이너 추가
#         ])
#     )


# app(main, assets_dir="assets")