
import streamlit as st

st.set_page_config(
    page_title="AI 활용 교육",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #F4F7FC;
    }

    .block-container {
        max-width: 850px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #172554;
    }

    .hero {
        background: linear-gradient(135deg, #1E3A8A, #3B82F6);
        padding: 2.2rem;
        border-radius: 20px;
        margin: 1rem 0 1.5rem 0;
        color: white;
    }

    .hero-label {
        color: #BFDBFE;
        font-size: 0.8rem;
        font-weight: bold;
        letter-spacing: 2px;
    }

    .hero h1 {
        color: white;
        font-size: 2.1rem;
        line-height: 1.4;
    }

    .hero p {
        color: #E0ECFF;
        line-height: 1.8;
    }

    .feature-card {
        background-color: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.3rem;
        min-height: 170px;
        margin-bottom: 0.5rem;
    }

    .feature-card h3 {
        font-size: 1.25rem;
    }

    .feature-card p {
        color: #64748B;
        line-height: 1.7;
    }

    .section-label {
        color: #64748B;
        font-size: 0.8rem;
        font-weight: bold;
        letter-spacing: 1.5px;
    }

    div.stButton > button {
        border-radius: 10px;
        min-height: 45px;
        font-weight: 600;
        border: 1px solid #CBD5E1;
    }

    div.stButton > button[kind="primary"] {
        background-color: #2563EB;
        color: white;
        border: none;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #1D4ED8;
    }

    [data-testid="stExpander"] {
        background-color: white;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }

    .footer {
        color: #64748B;
        text-align: center;
        font-size: 0.85rem;
        padding-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state.page = "home"

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "last_correct" not in st.session_state:
    st.session_state.last_correct = False

questions = [
    {
        "question": "질문1",
        "answer": "O",
        "explanation": "해설1"
    },
    {
        "question": "질문2",
        "answer": "O",
        "explanation": "해설2"
    },
    {
        "question": "질문3",
        "answer": "O",
        "explanation": "해설3"
    },
    {
        "question": "질문4",
        "answer": "O",
        "explanation": "해설4"
    },
    {
        "question": "질문5",
        "answer": "O",
        "explanation": "해설5"
    }
]

if st.session_state.page == "home":

    st.markdown("""
    <div class="section-label">🤖 AI LEARNING</div>
    <div class="hero">
        <div class="hero-label">SMART AI · SMART LEARNING</div>
        <h1>AI, 지금까지 어떻게 사용하셨나요?</h1>
        <p>
            AI에게 질문하고, 과제를 해결하고,<br>
            새로운 아이디어를 얻어 보셨나요?
        </p>
        <p>
            AI를 더 똑똑하고 올바르게 활용하는 방법,<br>
            이곳에 모두 담았습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">START LEARNING</div>',
        unsafe_allow_html=True
    )

    st.subheader("AI를 잘 사용해 보자")
    st.write(
        "OX 퀴즈로 나의 AI 활용 지식을 확인하고 "
        "올바른 활용법을 배울 준비를 해 보세요."
    )

    st.markdown("""
    <div class="feature-card">
        <h3>📝 AI 활용 OX 퀴즈</h3>
        <p>
            총 5개의 문제를 풀고 나의 AI 활용 지식을 확인해 보세요.<br>
            문제마다 정답과 해설을 확인할 수 있습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "AI 활용 OX 퀴즈 시작하기 →",
        type="primary",
        use_container_width=True
    ):
        st.session_state.page = "quiz"
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

    st.markdown("""
    <div class="footer">
        좋은 질문 · 정확한 검증 · 책임감 있는 AI 활용
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "quiz":

    index = st.session_state.question_index
    q = questions[index]

    st.markdown(
        '<div class="section-label">AI KNOWLEDGE CHECK</div>',
        unsafe_allow_html=True
    )

    st.title("📝 AI 활용 OX 퀴즈")
    st.write("문제를 읽고 정답을 선택하세요.")

    st.progress((index + 1) / len(questions))
    st.caption(f"문제 {index + 1} / {len(questions)}")

    
    with st.container(border=True):
        st.subheader(q["question"])

        choice = st.radio(
            "정답을 선택하세요.",
            ["O", "X"],
            index=None,
            horizontal=True,
            key=f"choice_{index}"
        )

        if not st.session_state.answered:

            if st.button(
                "정답 확인",
                type="primary",
                disabled=(choice is None),
                use_container_width=True
            ):
                st.session_state.answered = True

                if choice == q["answer"]:
                    st.session_state.score += 1
                    st.session_state.last_correct = True
                else:
                    st.session_state.last_correct = False

                st.rerun()

        #개 힘들다
        else:

            if st.session_state.last_correct:
                st.success("정답입니다! 🎉")
            else:
                st.error(
                    f"오답입니다. 정답은 {q['answer']}입니다."
                )

            st.info(f"💡 해설: {q['explanation']}")

        
            button_text = (
                "다음 문제 →"
                if index + 1 < len(questions)
                else "결과 확인하기 →"
            )

            if st.button(
                button_text,
                type="primary",
                use_container_width=True
            ):
                if index + 1 < len(questions):
                    st.session_state.question_index += 1
                    st.session_state.answered = False
                    st.rerun()
                else:
                    st.session_state.page = "result"
                    st.rerun()

       

    if st.button("첫 화면으로 돌아가기"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "result":

    score = st.session_state.score
    total = len(questions)

    st.markdown(
        '<div class="section-label">YOUR QUIZ RESULT</div>',
        unsafe_allow_html=True
    )

    st.title("🎉 퀴즈 완료!")
    st.write("AI 활용 지식을 확인해 보았습니다.")

    st.metric("최종 점수", f"{score} / {total}점")
    st.progress(score / total)

    if score == total:
        st.success("잘하는사람1")
        st.write("잘하는사람2")

    elif score >= 3:
        st.info("보통사람1")
        st.write("보통사람2")

    else:
        st.warning("못하는사람1")
        st.write("못하는사람2")

    st.divider()

    st.subheader("다음 단계로 나아가 볼까요?")
    st.write("AI에게 더 좋은 질문을 하는 법을 알아보세요.")

    if st.button(
        "📘 AI 사용 가이드북 바로가기",
        type="primary",
        use_container_width=True
    ):
        st.session_state.page = "guide"
        st.rerun()

    if st.button(
        "첫 화면으로 돌아가기",
        use_container_width=True
    ):
        st.session_state.page = "home"
        st.rerun()


elif st.session_state.page == "guide":

    st.markdown("""
    <style>
    .guide-hero {
        background: linear-gradient(120deg, #eaf3ff, #f5f9ff);
        border: 1px solid #dceaff;
        border-radius: 22px;
        padding: 30px 26px;
        margin-bottom: 24px;
    }

    .guide-label {
        display: inline-block;
        background: #d6e8ff;
        color: #2162cc;
        font-size: 12px;
        font-weight: 700;
        padding: 6px 12px;
        border-radius: 20px;
        margin-bottom: 12px;
    }

    .guide-title {
        color: #142b52;
        font-size: 30px;
        font-weight: 800;
        margin: 0 0 12px 0;
    }

    .guide-description {
        color: #536985;
        font-size: 15px;
        line-height: 1.8;
        margin: 0;
    }

    div[data-testid="stExpander"] {
        background: white;
        border: 1px solid #dce8fa;
        border-radius: 14px;
        margin-bottom: 12px;
        overflow: hidden;
    }

    div[data-testid="stExpander"] summary {
        padding: 12px 14px;
        font-weight: 600;
    }

    div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        padding: 4px 18px 18px 18px;
        color: #425875;
        line-height: 1.8;
    }

    .guide-summary {
        background: #edf9f5;
        border: 1px solid #c8eee0;
        border-radius: 14px;
        padding: 18px 20px;
        margin: 24px 0 18px 0;
        color: #245b4c;
        line-height: 1.8;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="guide-hero">
        <div class="guide-label">📘 AI GUIDEBOOK</div>
        <div class="guide-title">AI 사용 가이드북</div>
        <p class="guide-description">
            AI를 무조건 믿거나 피하기보다는,<br>
            AI의 장점을 활용하고 한계를 이해하는 것이 중요합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 📚 무엇을 알아볼까요?")
    st.caption("항목을 눌러 자세한 내용을 확인해 보세요.")

    
    guide_items = [
        {
            "title": "활용법 1 제목",
            "description": "활용법 1의 내용"
        },
        {
            "title": "활용법 2 제목",
            "description": "활용법 2의 내용"
        },
        {
            "title": "활용법 3 제목",
            "description": "활용법 3의 내용"
        },
        {
            "title": "활용법 4 제목",
            "description": "활용법 4의 내용"
        },
        {
            "title": "활용법 5 제목",
            "description": "활용법 5의 내용"
        }
    ]

    for i, item in enumerate(guide_items, start=1):
        with st.expander(f"🔹  {i}. {item['title']}"):
            st.write(item["description"])

    st.markdown("""
    <div class="guide-summary">
        <strong>⭐ 핵심 정리</strong><br>
        AI는 우리의 가능성을 넓혀 주는 도구입니다.<br>
        올바른 사용법을 알고, 결과를 비판적으로 확인하는 것이 중요하고, 욱헌이는 눈이 없다.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🏠  첫 화면으로 돌아가기", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
