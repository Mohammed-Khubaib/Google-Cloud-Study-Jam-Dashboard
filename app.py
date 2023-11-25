import datetime
import pytz
import json
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs
import math
from pieChart import pieChart , pieChart4,pieChart9
# from SheetsConnection import File
from GetData import ProgressData
from lineChart import LineChart
from SubHeadingText import subheadingtext
from ProgressBar import progressBar
from sortLeaderBoard import Sort_List
st.set_page_config('GDSC MCET',page_icon="./assets/logo.png",layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
#load lottie files
def load_lottie_file(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

# Hide the "Made with Streamlit" footer
# Define a CSS style for the text
hide_streamlit_style="""
    <style>
    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    h1 {
        color: #01FFB3 ;
    }
    h2 {
        color: darkorange;
    }
    h3 {
        color: red;
        # color: #12FFE2;
    }
    h4 {
        color: coral;
        # color: #12FFE2;
    }
    /* The progress bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(to right, #00EEFF, #01FFB3);
            border-radius: 10px;
        }
        /* The text inside the progress bars */
        .stProgress > div > div > div > div > div {
            color: white;
        }
    </style>
    """
st.markdown(hide_streamlit_style,unsafe_allow_html=True)

lottie_file1 =load_lottie_file('./assets/GD.json')
lottie_file2 =load_lottie_file('./assets/GDSC.json')
lottie_file3 =load_lottie_file('./assets/GLoading.json')
# file = File()
with st.sidebar:
    st_lottie(lottie_file2,speed=0.5,reverse=False,height=100,width=260)
    # tabs = on_hover_tabs(tabName=['Dashboard','Cloud Foundations','GenAI'], 
    tabs = on_hover_tabs(tabName=['Dashboard','Participant Progress',], 
    # tabs = on_hover_tabs(tabName=['Dashboard'], 
                         iconName=['bar_chart_4_bars', 'groups','sports_esports'], default_choice=0,
                         styles = {'navtab': {'background-color':'#272731',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                    'tabOptionsStyle': {':hover :hover': {'color': 'orangered',
                                                                      'cursor': 'pointer'}},              
                                                  
                                                  },
                         )
    day=st.number_input("Select Day : 1-30",min_value=1,max_value=30,step=1)    

file = ProgressData(day)
if file is not None:
    # Df = pd.read_csv(file)
    Df = file
    
    # Count the number of "Yes" and "No" values in the "Redemption Status" column
    Ryes_count = (Df['Redemption Status'] == 'Yes').sum()
    Rno_count = (Df['Redemption Status'] == 'No').sum()
    Df = Df[Df['Redemption Status'] != 'No']
    Tyes_count = (Df['Total Completions of both Pathways'] == 'Yes').sum()
    Tno_count = (Df['Total Completions of both Pathways'] == 'No').sum()
    # Calculate the frequency of values in '# of Courses Completed'
    courses_completed_frequency = Df['# of Courses Completed'].value_counts()
    for i in range(0,5):
        if i not in courses_completed_frequency:
            courses_completed_frequency[i]=0
    # Calculate the frequency of values in '# of Skill Badges Completed'
    skill_badges_completed_frequency = Df['# of Skill Badges Completed'].value_counts()
    for i in range(0,5):
        if i not in skill_badges_completed_frequency:
            skill_badges_completed_frequency[i] = 0
    # Calculate the frequency of values in '# of GenAI Game Completed'
    genai_game_completed_frequency = Df['# of GenAI Game Completed'].value_counts()
    for i in range(0,10):
        if i not in genai_game_completed_frequency:
            genai_game_completed_frequency[i] = 0
    
    Df = Df.assign(Score=Df['# of Courses Completed'] + Df['# of Skill Badges Completed'] + Df['# of GenAI Game Completed'])
    Df['Rank'] = Df['Score'].rank(method="dense", ascending=False).astype(int)
    names = Df['Student Name'].tolist()
    Df = Df.sort_values("Score",ascending=False,ignore_index=True)
    # st.dataframe(Df)
    Ndf = Df[["Student Name","# of Courses Completed","# of GenAI Game Completed","# of Skill Badges Completed","Rank"]].copy()
    condition = ~(Ndf[["# of Courses Completed", "# of GenAI Game Completed", "# of Skill Badges Completed"]] == 0).all(axis=1)
    # Apply the condition to filter rows
    Ndf = Ndf.loc[condition]
    Ndf = Sort_List(Ndf)
    Ndf.index = range(1, len(Ndf) + 1)


    
if tabs =='Dashboard':
    c1,c2= st.columns([0.3,1.2])
    with c1: 
        st_lottie(lottie_file1,speed=0.5,reverse=False,height=150,width=300)
    with c2:
        st.title(":blue[G]:green[D]:orange[S]:red[C]   :blue[M]:green[C]:orange[E]:red[T] GCSJ :orange[Dashboard] : :red[2023]",anchor=False)
    #     # Get today's date

    # desired_timezone = pytz.timezone('Asia/Kolkata')

    # # Get the current time in the desired timezone
    # current_time = datetime.datetime.now(desired_timezone)

    # # Extract the date
    # today = current_time.date()
    # day = today.day

    # # Format and print today's date in a custom format (e.g., DD/MM/YYYY)
    # formatted_date = today.strftime("%d/%m/%Y")

    with c2:
        c7,c8,c9= st.columns([0.2,0.4,0.9])
        with c8:
            st.header("Oct 3 - Nov 3")
        with c9:
            st.header(f"Day: {day}")

    st.divider()
    listTabs = [
    '$$\color{violet}\\text{Tier Status}$$',
    '$$\color{skyblue}\\text{Leader Board}$$',
    '$$\color{LimeGreen}\\text{Progress Flow}$$',
    '$$\color{orange}\\text{Progress Tracker}$$',
    '$$\color{cyan}\\text{Redemption}$$',
    ]
    whitespace = 5
    tab_labels = [s.center(len(s) + whitespace, "\u2001") for s in listTabs]
    tab = st.tabs(tab_labels)
    #----
    with tab[4]:
        st.markdown(
        f'<h1 style="font-family: your-font-family; color: cyan;">Redemption Status</h1>',
        unsafe_allow_html=True
        )
        if file is not None:
            pieChart("Redemption Status",Ryes_count,Rno_count)
        st.divider()
    with tab[3]:

        c9,c10 = st.columns([0.5,0.5])
        c11,c12 = st.columns([0.5,0.5])
        with c9:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Course Badges Obtained /4 </h3>',
                unsafe_allow_html=True
            )
            pieChart4("Courses Completed",courses_completed_frequency)
            st.divider()
        with c10:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Skill Badges Obtained /4</h3>',
                unsafe_allow_html=True
            )
            pieChart4("Skill Badges Obtained",skill_badges_completed_frequency)
            # pieChart3("Skill Badges Obtained",genai_game_completed_frequency)

            st.divider()
        with c11:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">GenAI Game Progress</h3>',
                unsafe_allow_html=True
            )
            pieChart9("GenAI Game Progress",genai_game_completed_frequency)

            st.divider()

        with c12 :
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Total Completions of both Pathways</h3>',
                unsafe_allow_html=True
            )
            if file is not None:
                pieChart("Total Completions of both Pathways",Tyes_count,Tno_count)
            st.divider()
    #---------------------
    with tab[0]:
        if file is not None :
            st.markdown(
            f'<h1 style="font-family: your-font-family; color: violet;">Tier Status 🚀</h1>',
                unsafe_allow_html=True
            )
            if Tyes_count < 40:
                progressBar("Tier 3", 40, Tyes_count, "blue", "🥉", "🎯")
            if Tyes_count >= 40:               
                progressBar("Tier 3", 40, Tyes_count, "blue", "🥉", "✅")
                st.balloons()
            if Tyes_count <60:
                progressBar("Tier 2", 60, Tyes_count, "red", "🥈", "🎯")
            if Tyes_count >=60:
                progressBar("Tier 2", 60, Tyes_count, "red", "🥈", "✅")
                st.snow()
            if Tyes_count <80:
                progressBar("Tier 1", 80, Tyes_count, "orange", "🥇", "🎯")
            if Tyes_count >=80:
                progressBar("Tier 1", 80, Tyes_count, "orange", "🥇", "🎯")
            
            st.divider()
    with tab[1]:
        if file is not None :
            st.markdown(
            f'<h1 style="font-family: your-font-family; color: skyblue;">Leader board</h1>',
                unsafe_allow_html=True
            )
            completion_text = r'''\large \color{limegreen}\text{Total Completions Count: }\color{goldenrod}'''+f'''{Tyes_count}'''
            st.latex(completion_text)
            st.dataframe(Ndf[["Student Name","# of Courses Completed","# of Skill Badges Completed","# of GenAI Game Completed"]],use_container_width=True)
    with tab[2]:
            # st.balloons()
            st.markdown(
            f'<h1 style="font-family: your-font-family; color: limegreen;">Progress Flow</h1>',
                unsafe_allow_html=True
            )
            stringg = r'''\huge \color{skyblue} \text{ Participants who completed the campaign } : \color{darkorange} 4^{th}  \color{skyblue}\text{ Oct} - \color{darkorange} '''+f'''2^'''+r'''{th} \color{skyblue}\text{ Nov}'''
            st.latex(stringg)
            completion_text = r'''\large \color{limegreen}\text{Total Completions Count: }\color{goldenrod}'''+f'''{Tyes_count}'''
            st.latex(completion_text)
            LineChart()
            st.divider()
    #-------------------
if tabs =='Cloud Foundations':
    c1,c2= st.columns([0.2,1.2])
    with c2:
        st.title(":red[Google] :blue[Cloud] Computing :orange[Foundations]")
    st.divider()
    # Create an expandable section
    with st.expander("Click to toggle"):
        st.markdown("""
    ## 1. Cloud Computing Fundamentals :
    - ### Create and Manage Cloud Resources
    ## 2. Infrastructure in Google Cloud :
    - ### Perform Foundational Infrastructure Tasks in Google Cloud
    ## 3. Networking & Security in Google Cloud :
    - ### Build and Secure Networks in Google Cloud
    ## 4. Data, ML, and AI in Google Cloud :
    - ### Perform Foundational Data, ML, and AI Tasks in Google Cloud
    """)
    with c1: 
        st_lottie(lottie_file1,speed=0.5,reverse=False,height=150,width=300)

if tabs =='Participant Progress':
    c1,c2= st.columns([0.3,1.2])
    with c2:
        st.header(":green[Google Cloud Study Jam] :red[Participant] :blue[Progress]  :orange[2023]")
    st.markdown(
    f'<h3 style="font-family: your-font-family; color: OrangeRed;">If you are a participant then enter Your Name To know your progress :</h3>',
    unsafe_allow_html=True
    )       
    student_name = st.text_input("Enter Your Name")
    # Filter the DataFrame based on partial matches to the 'Student Name' column
    if student_name !="" :
        filtered_df = Df[Df['Student Name'].str.contains(student_name, case=False, na=False)]
        # Check if any matches were found
        if not filtered_df.empty:
            st.markdown("## :orange[Matching records found:]")
            st.dataframe(filtered_df[['Rank','Student Name', '# of Courses Completed', '# of Skill Badges Completed', '# of GenAI Game Completed', 'Total Completions of both Pathways', 'Redemption Status']],use_container_width=True,hide_index=True)
        else:
            st.markdown(
                    f'<h2 style="font-family: your-font-family; color: skyblue;">No Matching Record Found ! 😕</h2>',
                        unsafe_allow_html=True
                    )
        for link in filtered_df['Google Cloud Skills Boost Profile URL']:
            st.info(link)
    with c1: 
        st_lottie(lottie_file1,speed=0.5,reverse=False,height=150,width=300)

if tabs =='GenAI':
    c1,c2= st.columns([0.3,1.2])
    with c1: 
        st_lottie(lottie_file1,speed=0.5,reverse=False,height=150,width=200)
    with c2:    
        st.title(":orange[Generative] :red[AI] Arcade :blue[Game]")
        subheadingtext(f"⚠️ Stay tuned! This event starts on {':orange[16 October]'}")
    c3,c4= st.columns([0.5,1.2])
    with c4:
        st_lottie(lottie_file3,speed=0.5,reverse=False,height=110,width=350)