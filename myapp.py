import streamlit as st
import pandas as pd
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from PIL.ImageFilter import *
import base64
import time
from streamlit_option_menu import option_menu
import graphviz as graphviz

st.set_page_config(page_title="Tobibui1904",page_icon=":basketball:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_fu0hgwse.json")


header= st.beta_container()
virtual=st.beta_container()
dataset= st.beta_container()
modelTraining=st.beta_container()
contact_form=st.beta_container()

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_data(filename):
    df=pd.read_csv(filename)
    return df

with header:
    st.markdown(""" <style> .font {
    font-size:50px ; font-family: 'Cooper Black'; color: #FF9633; style = "text-align:center;"} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<h1 class="font";>Stephen Curry</h1>',unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>Welcome to my first streamlit app</h1>", unsafe_allow_html=True)
    st.caption("<h1 style='text-align: center;'>A dynamic Python website coded by Tobi Bui</h1>",unsafe_allow_html=True)
    st.header("Intro about Stephen Curry")
    st.markdown("""
    Wardell Stephen "Steph" Curry II (born March 14, 1988) is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). 
    Widely regarded as one of the greatest point guards of all time, and as the greatest shooter in NBA history, Curry is credited with revolutionizing basketball by inspiring teams and players to routinely utilize the three-point shot.
    An eight-time NBA All-Star, he has been named the NBA Most Valuable Player (MVP) twice and has won three NBA championships.
    Curry is the son of former NBA player Dell Curry and the older brother of current NBA player Seth Curry. 
    He played college basketball for the Davidson Wildcats, where he set the all-time scoring record for Davidson and the Southern Conference, was twice named conference player of the year, and set the single-season NCAA record during his sophomore year for most three-pointers made. 
    Curry was selected by the Warriors with the seventh overall pick in the 2009 NBA Draft.
    """
    )
    st.write('##')
    if st.checkbox("Review Steph's milestones until 2018"):
        st.graphviz_chart('''
            digraph {
                bgcolor="#1D428A"
                width=1000
                1 [shape=circle label="Curry" color="#FDB927" fontcolor="#FDB927"]
                2 [shape=record label ="{2009 | Debut}" color="#FDB927" fontcolor="#FDB927"]
                1 -> 2 [arrowhead=olnormalornormal color= orange3]
                3 [shape=record label ="{2013 | 3-points records | 54 Points in MSG}" color="#FDB927" fontcolor="#FDB927"]
                2 -> 3 [arrowhead=olnormalornormal color= orange3]
                4 [shape=record label ="{2015 | 3-points records | 1st MVP |NBA Champs}" color="#FDB927" fontcolor="#FDB927"]
                4 -> 4 [arrowhead=olnormalornormal color= orange3]
                3 -> 4 [arrowhead=olnormalornormal color= orange3]
                5 [shape=record label ="{2016 | 3-points Most consecutive games | 2nd MVP}" color="#FDB927" fontcolor="#FDB927"]
                4 -> 5 [arrowhead=olnormalornormal color= orange3]
                5 -> 5 [arrowhead=olnormalornormal color= orange3]
                6 [shape=record label ="{2017 | NBA Champs }" color="#FDB927" fontcolor="#FDB927"]
                5 -> 6 [arrowhead=olnormalornormal color= orange3]
                7 [shape=record label ="{2018 | NBA Champs }" color="#FDB927" fontcolor="#FDB927"]
                6 -> 7 [arrowhead=olnormalornormal color= orange3]
            }   
        ''')

with virtual:
    st.write("---")
    st.header('Media')
    st.write('##')
    image = Image.open("Steph-Filty-Face-NBC.jpg")
    st.subheader("Let's have some fun with Steph")
    st.write('##')
    filters=st.selectbox("Choose your filter",options=["None","Blur","Contour","Emboss","Find Edges"])
    if filters=="None":
        pass
    elif filters=="Blur":
        image=image.filter(BLUR)
    elif filters=="Contour":
        image=image.filter(CONTOUR)
    elif filters=="Emboss":
        image=image.filter(EMBOSS)
    elif filters=="Find Edges":
        image=image.filter(FIND_EDGES)
    left_column,right_column=st.columns(2)
    with left_column:
        st.image(image)
    with right_column:
        st_lottie(lottie_coding,height=400,key="basketball")

    video_file = open("D:\Wondershare UniConverter\Downloaded\Stephen Curry's Ultimate Career Mixtape.mp4", 'rb')
    video_bytes = video_file.read()
    st.write('##')
    if st.button("Watch highlights"):
        st.subheader("Ready to see the BANG")
        st.video(video_bytes)

with dataset:
    st.write("---")
    st.header("Steph's overview stats analysis")

    df=get_data('Stephen Curry Stats.csv')
    df1 = df[['Dates', 'Minutes','Successful Shots','Total Shots','3 Points Succesful'
,'Total 3 Points', 'Successful FT','Total FT','REB','AST','BLK','STL','PF','TO','PTS','Type']]
    df1=df1.drop([0,1])
    df1.index=[i for i in range(1,875)]
    if st.checkbox("Preview overview data"):
       st.write(df1)

    st.subheader("This is a overview of Stephen Curry's performance from 2009 to 2018")
    d={'Minutes':[26256,29.904328018223236],
       'Successful Shots':[6151,7.005694760820045],
       'Total Shots':[12941,14.739179954441914],
       '3 Points Succesful':[2687,3.060364464692483],
       'Total 3 Points':[6198,7.0592255125284735],
       'Succesful FT':[2839,3.233485193621868],
       'Total FT':[2839,3.233485193621868],
       'REB':[3426,3.9020501138952164],
       'AST':[5075,5.780182232346242],
       'BLK':[168,0.19134396355353075],
       'STL':[1339,1.5250569476082005],
       'PF':[1886,2.1480637813211847],
       'TO':[2422,2.7585421412300684],
       'PTS':[17828,20.30523917995444]}
    overview = pd.DataFrame(data=d)
    overview.index = ['Sum','Mean']
    st.write(overview)
    st.write('From the table above, we can see Stephen Curry is definitely very efficient in scoring. His FG% is 47%, 3P% is 43% and FT% is 100%.')
    st.write('He is also a great defender with almost 1 block per game with his 6ft3 height. However his steals are not that high comparing to other PGs in the NBA with just almost 2 steals per game.')
    st.write('Curry is also a true shooting PG who not only can shoot well but also control the flow of the game pretty well. He does not turnover so much, only 2 per games.')
    st.write('As a very important player in the Warrior, Curry carries a very high responsibility of leading the team and try to be on court as much as possible, which leads to his only 2 personal fouls per game.')

with modelTraining:
    st.write("---")
    st.header('Detailed analysis')

    sel_col,disp_col=st.beta_columns(2)

    month=sel_col.slider('Which months do you want to choose',min_value=1,max_value=12,value=12,step=1)

    year=sel_col.selectbox('Which years do you want to choose?',options=[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],index=0)

    sel_col.text('Here is a list of stats in my data')
    stats_column=['Minutes','Shots','3 Points'
,'FT','REB','AST','BLK','STL','PF','TO','PTS']
    d={'Stats':[i for i in stats_column]}
    stats_table=pd.DataFrame(data=d)
    stats_table.index=[i for i in range(1,12)]
    sel_col.write(stats_table)

    stats=sel_col.text_input('Which stats should be choosen to analyze?')

    df['year'] = pd.DatetimeIndex(df['Dates']).year
    df['month'] = pd.DatetimeIndex(df['Dates']).month
    df['day'] = pd.DatetimeIndex(df['Dates']).day
    df['dates']=df['year'].astype(str)+"/"+df['month'].astype(str)
    df1['Dates']=df['dates']
    for i in range(1,11):
        if year==2009 and month==i:
            st.write("I'm so sorry but in 2009, there is no monthly stats from January to October")
    
    for i in stats_column:
        if stats==i:
            if stats=='Shots':
                df1=df1[['Dates','Successful Shots','Total Shots']]
            elif stats=='3 Points':
                df1=df1[['Dates','3 Points Succesful','Total 3 Points']]
            elif stats=='FT':
                df1=df1[['Dates','Successful FT','Total FT']]
            else:
                df1=df1[['Dates',stats]]

    df1=df1[(df1['Dates'] == str(year)+'/'+str(month))]
    st.write(df1)
    if stats=='':
        pass
    elif stats=='AST' or stats=='BLK' or stats=='REB' or stats=='STL' or stats=='PF' or stats=='TO' or stats=='TO' or stats=='PTS':
        st.line_chart(df1[stats],use_container_width=True)
    elif stats=='Shots':
        st.area_chart(df1['Successful Shots'],use_container_width=True)
        st.area_chart(df1['Total Shots'],use_container_width=True)
    elif stats=='3 Points':
        st.bar_chart(df1['3 Points Succesful'],use_container_width=True)
        st.bar_chart(df1['Total 3 Points'],use_container_width=True)
    elif stats=='FT':
        st.area_chart(df1['Successful FT'],use_container_width=True)
        st.area_chart(df1['Total FT'],use_container_width=True)
    else:
        pass

with contact_form:
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write('##')
    contact= """
    <form action="https://formsubmit.co/buituannghia1904@gmail.com" method="POST">
     <input type ="hidden" name="_capcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name= "message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    local_css(r"C:\Users\Admin\.streamlit\style.css")
    
with st.sidebar:
    selected = option_menu(
        menu_title="File used in the website",
        options=["Dataset", "Stephen Curry", "Highlight"],
        icons=["clipboard-data", "hand-thumbs-down", "camera-video"],
        menu_icon="cast",
        default_index=0, 
        styles={
                "container": {"padding": "0!important", "background-color": "#1D428A"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#26282A",
                },
                "nav-link-selected": {"background-color": "black"},
            },
    )
    if selected == 'Dataset':
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(df1)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )
    elif selected=="Stephen Curry":
        with open("Steph-Filty-Face-NBC.jpg","rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="Steph-Filty-Face-NBC.jpg",
                    mime="image/png"
                )
    elif selected=="Highlight":
        with open("D:\Wondershare UniConverter\Downloaded\Stephen Curry's Ultimate Career Mixtape.mp4", 'rb') as file:
            btn = st.download_button(
                    label="Download Video",
                    data=file,
                    file_name="Stephen Curry's Ultimate Career Mixtape.mp4",
                )
