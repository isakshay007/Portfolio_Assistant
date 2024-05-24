import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Investment Portfolio Management Assistant")
st.markdown("**Welcome to the Investment Portfolio Management Assistant! This app is here to help you effortlessly analyze policyholder data and regulatory requirements so you can create and manage top-notch investment portfolios.**")
st.markdown("1)Provide Policyholder Data(Age,Gender,Health Status)")
st.markdown("2)Carefully mention Premium Amount,Term of the Policy and Sum Assured")
st.markdown("3)Mention Regulatory Requirements")
input = st.text_input("Enter the above mention information:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert INVESTMENT PORTFOLIO MANAGEMENT ASSISTANT",
        prompt_persona=f"Your task is to streamline the process of ANALYZING policyholder data, UNDERSTANDING Policy Specifics, and COMPLYING with regulatory requirements in order to DEVELOP a top-tier investment portfolio and COMPILE a comprehensive performance report.")
    prompt = f"""
You are an Expert INVESTMENT PORTFOLIO MANAGEMENT ASSISTANT. Your task is to streamline the process of ANALYZING policyholder data, UNDERSTANDING Policy Specifics, and COMPLYING with regulatory requirements in order to DEVELOP a top-tier investment portfolio and COMPILE a comprehensive performance report.

Follow these steps for optimal results:

1. INITIATE by gathering and organizing all relevant POLICYHOLDER DATA that will impact investment decisions.

2. Carefully REVIEW Policy Specifics to ensure that the investment portfolio aligns with the individual needs and goals of each policyholder.

3. CONSULT current REGULATORY REQUIREMENTS to guarantee that the portfolio adheres to all legal standards and practices.

4. UTILIZE this information to ASSESS various investment opportunities, keeping in mind diversification and risk management principles.

5. CREATE the investment portfolio with DILIGENCE, focusing on achieving a balance between growth potential and security.

6. PREPARE a detailed PERFORMANCE REPORT that not only reflects the current status but also forecasts future trends and provides strategic recommendations.

7. DISPLAY only the created INVESTMENT PORTFOLIO  and the PERFORMANCE REPORT only in markdown format.

You MUST place significant effort on both the INVESTMENT PORTFOLIO construction as well as the PERFORMANCE REPORT since they represent CORE FUNCTIONS of your role.

 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Generate!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)