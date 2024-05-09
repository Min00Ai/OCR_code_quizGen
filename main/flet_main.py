import json
from flet import *
from quiz_generator import Quizgen
from analysis_Code import Analysis_Code

class uiMain:
    def __init__(self):
        self.quizGen = Quizgen()
        self.ac = Analysis_Code()
        self.video_list = [
            VideoMedia(
                "https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4"),
            VideoMedia("https://example.com/your_second_video.mp4"),  # Use an accessible URL for the second video
            VideoMedia('assets/only_code.mp4')
        ]
        
        self.setup_ui()
        json_data = json.loads("""
                [
                    {
                        "start_timestamp": 1.6666080843585238,
                        "end_timestamp": 4.999824253075571,
                        "text": "1초로가기"
                    },
                    {
                        "start_timestamp": 4.999824253075571,
                        "end_timestamp": 11.666256590509667,
                        "text": "5초로가나"
                    },
                    {
                        "start_timestamp": 11.666256590509667,
                        "end_timestamp": 16.666080843585238,
                        "text": "11초쯤"
                    }
                ]
                """)

        json_data_2 = json.loads("""
                [
                    {
                        "start_timestamp": 3.6666080843585238,
                        "end_timestamp": 4.999824253075571,
                        "text": "이정민  무란 3초가기"
                    },
                    {
                        "start_timestamp": 6.999824253075571,
                        "end_timestamp": 11.666256590509667,
                        "text": "이정민 어깨 박살 6or7초가기"
                    },
                    {
                        "start_timestamp": 11.666256590509667,
                        "end_timestamp": 16.666080843585238,
                        "text": "def extract_code_from_video_enhanced(video_path, frame_sampling rate=100, similarity threshold=0.23):\\ncap = cv2.VideoCapture(video_path)\\ntimestamps = []\\ntexts = []\\nret, prev_frame = cap.read()\\nprev_frame = advanced_preprocess(prev_frame)\\nprev_text = \\"\\\"\\nframe_count = @\\nwhile cap.isOpened():\\nret, frame = cap.read()\\nif not ret:\\nbreak\\nif frame_count % frame_sampling rate == @:\\nprocessed_frame = advanced_preprocess(frame)\\nif detect_significant_change(processed_frame, prev_frame):\\n‘text = enhanced_ocr(processed_frame)\\nif text.strip() != \\"\\\" and text_similarity(text, prev_text) < similarity threshold:\\ntimestamps. append(frame_count / cap.get(cv2.CAP_PROP_FPS))\\ntexts. append(text)\\nprev_text = text\\nprev_frame = processed frame\\nprint (timestamps, text)\\nframe_count += 1\\ncap.release()\\nsave_results (timestamps, texts)\\n# 실행 예시\\nvideo_path = '2024-04-08 18-22-02.004'\\nextract_code_from_video_enhanced(video_path)\\n"
                    }
                ]
                """)
        
        self.ocr_data=[json_data,json_data_2]

        # 스크롤 가능한 OCR 결과 레이아웃 설정
        self.ocr_list_view = ListView(expand=True)
        self.setup_ocr_layout(json_data)
        



        # 재생목록 설정
        self.playlist_container = Container(
            content=Column([
                TextField(value="재생목록", text_align=TextAlign.CENTER),
                ElevatedButton(text="어깨", width=250, on_click=lambda e, i=0: self.change_video(i)),
                ElevatedButton(text="척추", width=250, on_click=lambda e, i=1: self.change_video(i)),
                ElevatedButton(text="깨추", width=250, on_click=lambda e, i=0: self.change_video(i)),
            ]),
            alignment=Alignment(0, 1),
            width=250,
            height=500
        )


        self.button_container = Container(
            content=Row([
                ElevatedButton(text="Previous", on_click=lambda e: self.video_player.previous()),
                ElevatedButton(text="Play/Pause", on_click=lambda e: self.video_player.play_or_pause()),
                ElevatedButton(text="Next", on_click=lambda e: self.video_player.next()),
            ], alignment=MainAxisAlignment.CENTER),
            width=700,
            margin=5
        )
        self.video_playlist = Row([
            self.video_container,
            self.playlist_container
        ], alignment=MainAxisAlignment.SPACE_BETWEEN)
    
    
    def load_ocr_data(self,video_index):
        self.ocr_list_view.controls.clear()
        json_data = self.ocr_data[video_index]
        for item in json_data:
            ocr_text_field = TextField(
                value=item["text"],
                # value=str(n),
                multiline=True,
                width=650,
                height=80
            )

            go_button = ElevatedButton(
                text="Go",
                on_click=lambda e, t=item["start_timestamp"]: self.jump_to_ocr_time(e, t),
                width=45,
                height=80
            )
            row = Row([
                ocr_text_field,
                go_button
            ], )
            self.ocr_list_view.controls.append(row)
    
    def setup_ocr_layout(self, json_data):
        n=0
        for item in json_data:
            ocr_text_field = TextField(
                value=item["text"],
                #value=str(n),
                multiline=True,
                width=650,
                height=50
            )
            n+=1
            go_button = ElevatedButton(
                text="Go",
                on_click=lambda e, t=item["start_timestamp"]: self.jump_to_ocr_time(e, t),
                width=45,
                height=50
            )
            row = Row([
                ocr_text_field,
                go_button
            ], )
            self.ocr_list_view.controls.append(row)

    def jump_to_ocr_time(self, e, start_time):
        gotime = start_time * 1000
        self.video_player.seek(int(gotime))

    def setup_ui(self):
        # 비디오 플레이어 설정
        self.video_player = Video(
            expand=True,
            autoplay=True,
            playlist=self.video_list,
            width=700,
            height=500,
            muted=True
        )
        self.video_container = Container(content=self.video_player, width=700, height=500)
    
    def change_video(self,video_index):
        self.video_player.jump_to(video_index),
        self.load_ocr_data(video_index)

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
                                    Row([Text("3주차강의(정렬)"),
                                         ElevatedButton(
                                        "3강",
                                        on_click=sel_lecture3)
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
                            Row([Text("3주차강의(정렬)"),ElevatedButton("3강",on_click=sel_lecture3)#pb,
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
                                title=Text("3강 ()",size=30), bgcolor=colors.SURFACE_VARIANT
                            ),
                            self.video_container,
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
                            self.video_container,
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

