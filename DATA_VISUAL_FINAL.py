#!/usr/bin/env python
# coding: utf-8

# In[380]:


import pandas as pd
import numpy as np
import plotly.express as px
pd.options.plotting.backend = "plotly"
import plotly.subplots as sp
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")


# In[381]:

main_path = "/Users/mino/Desktop/visualizing_data/"
AI_final= pd.read_csv(main_path+"Data_visualization_final.csv")

raw_data = pd.read_csv(main_path+"Media Representations of Artificial Intelligence (AI) - GM_April 10, 2020_09.26_cleaned.csv")
# In[382]:


AI_final['Living Area'] = AI_final['Living Area'].replace({
    'Urban (densely developed area within a city)': 'Urban', 
    'Rural (less developed area outside a city)': 'Rural', 
    'Suburban (well-developed, residential area outside a city)':'Suburban', 
    '-':'Missing'})


AI_final['How do you image AI'] = AI_final['How do you image AI'].replace({
    'Robots': 'Robot', 'robot':'Robot', 'robots':'Robot', 'Robotics':'Robot','Robotic':'Robot', 
    'compupter':'Computer','computers':'Computer','Computers':'Computer', '4':'Missing', 
    'computer sciences.':'Computer', 'computer actuated':'Computer', 'Computer automation':'Computer',
    'Computer games ':'Computer', 'computer generated':'Computer', 'Computer intelligence':'Computer', 
    'Computer knowledge':'Computer', 'computer robot':'Computer', 'computer science ':'Computer', 
    'computer software trained to minic humans':'Computer', 'Computer technology':'Computer', 
    'computer with thinking/problem solving capability':'Computer', 'Computer ':'Computer','Computer work':'Computer', 
    'Computerized':'Computer','Computers doing the work':'Computer', 'computers!!!':'Computer', 'control':'Control',
    'CREEPY':'Creepy','danger':'Dangerous', 'Danger':'Dangerous', 'data from star trek':'Data', 
    'depends on the situation':'Depends On The Situation', 'Dont no':'Do Not Know','I do not no ':'Do Not Know',
    'I don‚Äôt know ':'Do Not Know', 'i dont know':'Do Not Know', 'Ibm':'IBM',
    'draws a blank':'Blank','Idk':'Do Not Know', 'informatiom':'Information', 'information in the cloud':'Information',
    'innovative':'Innovation', 'Innovative':'Innovation', 'intelligence':'Intelligent', 
    'Intelligent robot or computer  n or both':'Intelligence', 'interesting':'Interesting', 'internet':'Internet', 
    'Intrigue ':'Intriguing ', 'intriguing ':'Intriguing ', 'Irobot':'Robot', 'It':'Missing', 'Its cool':'Cool', 
    'Knowledge that is not real or taught the right way ':'Knowledge', 'Learned intelligence':'Intelligence', 
    'learning':'Learning', 'machine':'Machine','MACHINE':'Machine ', 'Machine intelligence':'Machines',
    'Machine learning':'Machine', 'machine learning':'Machine', 'Machines':'Machines', 
    'machines and software with human intelligence':'Machine', 'mordern technology':'Techonology', 'movie':'Movie',
    'No':'Noen-human', 'No human':'None-human', 'non':'None-human', 'non human':'None-human', 
    'Non human robot':'None-human', 'none':'Non-human', 'Nonhuma':'None-human', 'not artificial':'None-artificial',
    'Not human':'None-human', 'not human':'Non-human', 'not real':'Not real', 'nothing':'Nothing', 
    'dread':'Dread', 'driving':'Driving','Effective':'Efficiency', 'emotions':'Emotions', 'et':'ET',
    'fake':'Fake','fade':'Fake', 'Fade':'Fake', 'Fake being smart ':'Fake', 'Fake humans':'Fake', 
    'Fake information about something ':'Fake', 'Fake knowledge ':'Fake', 'Fake smart':'Fake', 
    'Fake smarts':'Fake', 'Fale':'Fales', 'fascinating':'Fascinating', 'fbi':'FBI', 'Fbi':'FBI', 'food':'Food',
    'Fske':'Fake', 'Futeristic':'Future', 'future':'Futuristic', 'Futuristic':'Future', 'futurstic':'Future', 
    'GOOD':'Good', 'good thing':'Good', 'Google Assistant ':'Google', 'government':'Government', 'great':'Great',
    'Hal 3000':'Missing','Handy robot':'Robot', 'Helping ':'Helpful', 'High intelligent':'Intelligence', 
    'Human form robot':'Robot', 'human interaction':'Human Interaction',
    '-':'Missing', '–í–¥–¥–≤–ª–≤':'Missing', 'A robot':'Robot','Robots ':'Robot',
    'A robot you feed information to':'Robot','A sentient program created by man.':'Sentiment Program',
    'A.i.':'AI', 'Ai':'AI','ai':'AI','AI robot':'AI', 'AI the movie':'AI', 
    'Ability to perform many task':'Ability', 'advanced':'Advanced', 'Advanced technology':'Advanced',
    'Advancement':'Advanced', 'alaxa':'Alexa', 'Alea':'Alexa', 'ALEXA':'Alexa', 'Alexis': 'Alexa', 
    'Alien being':'Alien', 'Aliens':'Alien', 'ALIENS':'Alien', 'aliens':'Alien',
    'An intelligence that is not achieved through normal learning':'Intelligence', 'android':'Android', 
    'animatronics':'Animatronics', 'artificial':'Artificial', 'artificial superintelligence':'AI', 
    'Automated':'Automation', 'automation':'Automation', 'awesome':'Awesome', 'BEST':'Best', 
    'Book smart':'Smart', 'bot':'Robot', 'cia':'CIA', 'Cia':'CIA', 'Co!pitr':'Missing', 'coding':'Coding', 
    'cofused':'Confused','cold robots ':'Cold'})

AI_final['AI in media']= AI_final['AI in media'].replace({'mostly good.':'Mostly Good', 
                                                            'equal parts good and bad.':'Equal parts Good & Bad',
                                                            'mostly bad.':'Mostly Bad', 
                                                            'neither good nor bad.':'Neither Good Nor Bad'})
AI_final['Education']= AI_final['AI in media'].replace({'High school degree or Graduate Equivalent Degree (GED)':'High school degree'})


#columns_to_replace_use = ['Self-driving cars', 'Predictive text or search algorithms', 'Digital assistants ',
         #  'Digital recommendation systems', 'Roomba and other smart home devices', 'Big Data', 
        #   'Facial recognition', 'Wireless networks', 'Voice recognition', 'Virtual reality gaming',
        #                  'AI as caretaker or loved one', 'Affection for AI']

#replacement_rule_use = {col: {'-': 'Missing', 'Yes, daily or weekly user': 'Use daily', 
          #                    'Have used before':'Used Before'} for col in columns_to_replace_use}
#AI_final = AI_final.replace(replacement_rule_use, regex=True)

#columns_to_replace = ['AI in media_1', 'AI in media_2', 'AI in media_3', 'AI in media_4', 'AI in media_5',
          #            'AI in media_6', 'AI in media_7', 'AI Do_1','AI Do_2', 'AI Do_3', 'AI Do_4', 'AI Do_5', 'AI Do_6',
          #            'AI Do_7','AI Do_8','AI Do_9', 'AI Do_10']
#replacement_rule = {col: {'-': 'Missing', ' - ': 'Missing'} for col in columns_to_replace}

#AI_final = AI_final.replace(replacement_rule, regex=True)

# In[383]:


category_orders_dict = {'Confidence know AI': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                              'Strongly disagree'],
                        'Education': ['Less than a high school degree', 'High school degree',
                                      'Some college, no degree', 'Associates degree', "Bachelor's degree", 
                                      'Graduate or professional degree'],
                        'Age':['18-24', '25-34','35-44', '45-54','55-64', '65-74', '75+'],
                       'Optimistic or pessimistic':['Neither optimistic nor pessimistic', 'Optimistic', 
                                                    'Pessimistic', 'Very optimistic', 'Very pessimistic'],
                       'AI as caretaker or loved one': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                              'Strongly disagree','Missing'],
                       'Affection for AI': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                              'Strongly disagree','Missing'],
                       'Developers are ethical':['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                              'Strongly disagree','Missing']}

demographics = ['Age', 'Gender','Living Area', 'Education']

AI_final = AI_final.rename(columns={'AI in media_1': 'Killer robots or cyborgs', 
                                    'AI in media_2': 'Sentient or self-aware robots', 
                                    'AI in media_3':'Helpful robots or droids', 
                                    'AI in media_4':'Childlike robots', 
                                    'AI in media_5':'Emotional support system', 
                                    'AI in media_6':'Massive screens of data',
                                    'AI in media_7':'Disembodied voices following'})

AI_final = AI_final.rename(columns={'AI Do_1': 'Think logically and solve problems', 
                                    'AI Do_2': 'Replicate human interaction', 
                                    'AI Do_3': 'Interpret speech', 
                                    'AI Do_4': 'Learn new things', 
                                    'AI Do_5': 'Run surveillance on people', 
                                    'AI Do_6': 'Replace human jobs',
                                    'AI Do_7': 'Take over the world',
                                    'AI Do_8': 'Feel emotion',
                                    'AI Do_9': 'Develop relationships with humans', 
                                    'AI Do_10': 'Replace pets'})
#Perception of AI in media 



# In[384]:

with st.sidebar: 
    selected = option_menu(
        menu_title = 'Navigation Pane',
		options = ['Introduction', 'Data Cleaning','Analysis of Demographic', 'Exploratory Analysis', 'Conclusion', 'References'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['bookmark-check', 'book', 'box', 'map', 'boxes', 'bar-chart', 
		'check2-circle'],
		default_index = 0,
		)



if selected=='Introduction':
    st.title("Public Understanding of Artificial Intelligence")
    st.markdown("For the final project, and analysis from the dataframes, I conducted a thorough analysis of a dataset titled ''Public Understanding of Artificial Intelligence through Entertainment Media''using the pandas library in Python. This dataset includes responses from a survey that aimed to measure the American public's awareness, perception, and use of AI in their daily lives. Through this analysis, I aimed to gain a better understanding of the demographics of the survey respondents and their perceptions of AI, as well as explore any patterns or correlations in their responses. ")

    st.markdown("The purpose of my presentation is to provide an overview of the data and showcase the key findings of my analysis. I will present graphs and charts that highlight the demographics of respondents, their overall perception of AI, and their awareness of AI usings in their everyday lives. I will also explore what people think AI looks like and what they believe it can do, as well as their feelings towards AI, people's frequency of using AI in their daily life and its potential impact on society.Through my analysis, I aim to provide  insights into  publics' awareness and perception of AI and contribute to my own interest and future acadmic or design concerns about the development and use of AI technology. ")
    
    
    st.dataframe(AI_final)


    
if selected=="Data Cleaning":
    st.title('Data Cleaning')
    st.markdown("During the data cleaning process, I found out there were cells in columns that contain mutiple forms of the same words or similar menings of words, which are the variables that need to be cleaned up into a uniform form to efficiently run the functions for later analysis.  ")
    st.code('''AI_final['How do you image AI'] = AI_final['How do you image AI'].replace({
        'Robots': 'Robot', 'robot':'Robot', 'robots':'Robot', 'Robotics':'Robot','Robotic':'Robot', 
        'compupter':'Computer','computers':'Computer','Computers':'Computer', '4':'Missing', 
        'computer sciences.':'Computer', 'computer actuated':'Computer', 'Computer automation':'Computer',
        'Computer games ':'Computer', 'computer generated':'Computer', 'Computer intelligence':'Computer', 
        'Computer knowledge':'Computer', 'computer robot':'Computer', 'computer science ':'Computer', 
        'computer software trained to minic humans':'Computer', 'Computer technology':'Computer', ''')
        
    st.markdown("In the dataframes, there were also values of '-', which representing missing values. ")   
    st.code('''replacement_rule_use = {col: {'-': 'Missing', 'Yes, daily or weekly user': 'Use daily', 
                                  'Have used before':'Used Before'} for col in columns_to_replace_use}
    AI_final = AI_final.replace(replacement_rule_use, regex=True)''')
    
    st.markdown("Lastly, I also created a category dictionary. This is useful when the default order of the categories in the variable is not ideal for the purposes. By defining a custom order, I can ensure that the categories are displayed in a more meaningful or logical way.")
    st.code('''category_orders_dict = {'Confidence know AI': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                                  'Strongly disagree'],
                            'Education': ['Less than a high school degree', 'High school degree',
                                          'Some college, no degree', 'Associates degree', "Bachelor's degree", 
                                          'Graduate or professional degree'],
                            'Age':['18-24', '25-34','35-44', '45-54','55-64', '65-74', '75+'],
                           'Optimistic or pessimistic':['Neither optimistic nor pessimistic', 'Optimistic', 
                                                        'Pessimistic', 'Very optimistic', 'Very pessimistic'],
                           'AI as caretaker or loved one': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                                  'Strongly disagree','Missing'],
                           'Affection for AI': ['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                                  'Strongly disagree','Missing'],
                           'Developers are ethical':['Neither agree nor disagree', 'Agree', 'Disagree', 'Strongly agree',
                                                  'Strongly disagree','Missing']}''')
    
    
if selected=="Analysis of Demographic":
    st.title("Analysis of Demographics of Respondants")
    st.markdown("In this section, I will take a closer look at the demographics of the survey respondents in our dataset. By understanding the characteristics of the groups of people who took the survey, we can gain a better understanding of their perceptions of Artificial Intelligence (AI) and how those perceptions may differ among various demographics")
    
   #graph 1
    st.subheader('Overview of Respondents Demographics') 
    col1, col2 = st.columns([3, 5]) 
    category_col1 = col1.selectbox("Select One Category For Exploring Demographics",demographics, key=1)  
    if category_col1 in demographics:  
        fig1 = px.histogram(AI_final, x=category_col1, category_orders=category_orders_dict, barmode="group",
                         title=f"{category_col1} For Demographic Exploration")  
        fig1.update_traces(texttemplate='%{y:1f}') 
        col2.plotly_chart(fig1) 
    else:  
        st.warning("Please select a demographic column to explore.")
    
    col1.markdown("Referring to the graph would provide us with valuable insights into the demographics of the participants who took part in this survey. The graph displays data such as age, gender, education level, and living areas relevant characteristics of the respondents.")
    
    #graph 2
    st.subheader('Exploring Respondents Confidence of Knowing AI')
    
    col3,col4=st.columns([3,5])
    with st.form("Select One Category For Demographic"):      
        category_col2 = col3.selectbox("Select a Column", demographics, key=2)
        col3_checkbox= col3.checkbox("Check For a Normalized Bar Chart")
        submitted=st.form_submit_button("Submit to produce bar chart")
        Percent = None 
        if col3_checkbox:
            Percent = "percent"
        if submitted: 
            fig2 = px.histogram(AI_final, x="Confidence know AI", category_orders = category_orders_dict, barmode="group",title = f"{category_col2} Of Confidence Know AI",histnorm=Percent)	
            fig2.update_traces(texttemplate='%{y:.1f}') 
            col4.plotly_chart(fig2)
            
    #graph 3   
    st.subheader('Optimistic or Pessimistic Attitude Toward AI')
    col5,col6 =st.columns([3,5])
    with st.form("Select One Category Demographic"):      
        category_col3 = col5.selectbox("Select a Column", demographics, key=3)
        col5_checkbox= col5.checkbox("Check For a Normalized Histogram Chart")
        submitted=st.form_submit_button("Submit to produce bar chart")
        Percent = None 
        if col5_checkbox:
            Percent = "percent"
        if submitted: 
            fig3 = px.histogram(AI_final, x="Optimistic or pessimistic", category_orders = category_orders_dict, 
                                barmode="group",title = f"{category_col3} Of Optimistic or Pessimistic Attitude Toward AI", 
                                histnorm=Percent)	
            fig3.update_traces(texttemplate='%{y:.1f}') 
            col6.plotly_chart(fig3)
    
    
    
if selected=="Exploratory Analysis":   
    st.title("Analysis of Public Understanding of AI")
    
    st.header("How Do People Image And Understand AI From Media")
    st.markdown("In this section, we will explore the data to understand how people imagine and comprehend AI through the lens of the media.")
    st.markdown("Through this analysis, we will examine the extent to which media coverage of AI has shaped people's perceptions, attitudes, and beliefs about this emerging technology. We will investigate the sources of information people rely on to learn about AI, their level of trust in the media, and how these factors affect their understanding and image of AI. ")
    
    #1
    st.subheader("How Do People Image AI")
    col5,col6 = st.columns([1,1])
    col5.markdown("")
    col5.markdown("The sunburst graph provides a visual representation of how people image AI, based on age and gender. The graph shows that the majority of people (both male and female) imagine AI as a robot. This image of AI as a robot may be influenced by popular culture and media portrayals of AI as humanoid machines." )
    col5.markdown("However, the graph also reveals an interesting insight: among females aged 18-24, there is a considerable number of individuals who imagine AI as ''smart'' rather than a ''robot''. This finding suggests that younger women may have a more nuanced and diverse understanding of AI, possibly influenced by their exposure to technology and its applications in various fields.")

    fig_ana_1 = px.sunburst(AI_final,path=["Gender", "Age", "How do you image AI"],
                       values = "Count",color = "Gender", height = 600, width = 600)
    col6.plotly_chart(fig_ana_1)
    
    
    #2
    st.subheader("How Do People Think Of AI Characters From Medias ") 
    col7,col8=st.columns([1,1])
    col7.markdown("This histogram displays people's perceptions and feelings towards AI, particularly those based on AI characters portrayed in media such as movies, TV shows, and avatars created in social media. The histogram reveals that the majority of people perceive AI as equally good and bad, indicating that they do not see AI as a single-faced ''robot'', but rather as a technology with multiple personalities and functions that can make both positive and negative decisions.")
    col7.markdown("However, a significant portion of people believe that AI is mostly good, based on their understanding of AI from media portrayals. This finding suggests that media coverage and fictional representations of AI can shape people's perceptions and attitudes towards this technology. ")
 
    fig_ana_2 = px.histogram(AI_final, x='AI in media', y='Count', color='Gender',category_orders = category_orders_dict)

    col8.plotly_chart(fig_ana_2) 
    col7.markdown("")
    col7.markdown("")
    col7.markdown("")
    
   #3
    st.subheader("People's Perception of AI From Media ") 
    col9,col10=st.columns([1,1])
    col9.markdown("This histogram provides insight into people's perceptions of AI from various media sources, such as movies, TV shows, and other avatars created on social media. The X-axis represents the different types of AI characters that people have encountered in these media sources, such as killer robots or cyborgs, sentient or self-aware robots, helpful robots or droids, childlike robots, emotional support systems, massive screens of data, and disembodied voices following.")
    col9.markdown("A significant portion of the data has missing values, which can limit the accuracy of the analysis. Despite this, interestingly, people also perceive AI as often being imaged as killer robots or cyborgs, which may reflect the prevalence of dystopian or apocalyptic themes in popular media. ")
     
    main_cols = ['Age']
    factors = ['Killer robots or cyborgs', 'Sentient or self-aware robots', 'Helpful robots or droids', 
           'Childlike robots', 'Emotional support system', 'Massive screens of data', 'Disembodied voices following']

    AI_final_merged_melt = pd.melt(AI_final, id_vars=main_cols, value_vars=factors, value_name='AI in media is')

    AI_final_merged_melt = AI_final_merged_melt.replace('-', pd.NA)

    AI_final_merged_melt = AI_final_merged_melt.dropna()

    fig_ana_3 = px.histogram(AI_final_merged_melt, x='AI in media is', nbins=20, color='Age', histnorm='percent')

    fig_ana_3.update_layout(title='Perceptions of AI in Media by Gender', xaxis_title='AI Characters in Medias', yaxis_title='Percentage')

    col10.plotly_chart(fig_ana_3)
    
    col9.markdown("")
    col9.markdown("")
    col9.markdown("")
    
    #4
    st.subheader("People's Perception of AI Capability ") 
    col11,col12=st.columns([1,1])
    col11.markdown("The histogram reveals the frequency of responses about people's perceptions of AI's abilities. The graph shows that most people believe that AI has the ability to replace human jobs and is capable of logical thinking and problem-solving. This suggests that people have a perception of AI's ability to perform tasks that were traditionally reserved for humans. It also shows that the least amount of people believe that AI has the ability to feel emotions.")
    
    main_cols = ['Education']
    factors = ['Think logically and solve problems', 'Replicate human interaction', 'Interpret speech',       'Learn new things', 'Run surveillance on people', 'Replace human jobs', 'Take over the world',       'Feel emotion', 'Develop relationships with humans', 'Replace pets']


    AI_final_merged_melt = pd.melt(AI_final, id_vars=main_cols, value_vars=factors, value_name='AI Capabilities')

    AI_final_merged_melt = AI_final_merged_melt[AI_final_merged_melt['AI Capabilities'] != '-']

    fig_ana_4 = px.histogram(AI_final_merged_melt, x='AI Capabilities', nbins=20, color='Education', histnorm='percent')

    fig_ana_4.update_layout(title='AI Capabilities by Gender', xaxis_title='AI Capabilities', yaxis_title='Percentage')
    col12.plotly_chart(fig_ana_4)
    
    col11.markdown("")
    col11.markdown("")
    col11.markdown("")
    
    #5  
    st.subheader("Frequency Of Using Various Types Of AI In Real Lives") 
    
    col13,col14=st.columns([1,1])
    col13.markdown("Choose a category from the select box to ecplore the requency of people using various types of AI in their real lives. Explore the frequency of using different AIs with the colors of living area, and explore if there are patterns that people live in city would have more chances using AI techonologies comparing to suburban or rural area.")
   
    categories = ['Self-driving cars', 'Predictive text or search algorithms', 'Digital assistants ',
           'Digital recommendation systems', 'Roomba and other smart home devices', 'Big Data', 
           'Facial recognition', 'Wireless networks', 'Voice recognition', 'Virtual reality gaming']
    
    cat_option= col13.selectbox("Select items",categories,key =4)
    fig_ana_6 = px.histogram(AI_final, x=cat_option, color = "Living Area", category_orders =category_orders_dict, histfunc="avg", nbins=20, text_auto=True, barmode="group",title = f"Frequency of using {cat_option}")
    col14.plotly_chart(fig_ana_6 )
    
    col13.markdown("By looking at the graphs, it was found that the most commonly used AI technologies in people's daily lives are Predictive text or search algorithms, Digital recommendation systems, and Wireless networks. This is may due to the reasons that these technologies have become an integral part of people's daily routines.")

    col13.markdown("Furthermore, the histogram created by the code allows for an exploration of any patterns or correlations between living area and the frequency of AI technology usage. People iving in urban areas and a higher likelihood of using AI technologies. This could be due to greater access to advanced technologies in urban areas or a greater need for technology to navigate densely populated environments.")
    col13.markdown("")
    col13.markdown("")
    col13.markdown("")
    
    #6
    st.subheader("Think AI As Care Taker Or Have Affection To AI") 
    st.markdown(" It is interesting while exploring datafram, there are responses regarding to people's perepspetives toward perceptions of thinking Think AI As Care Taker and Have Affection To AI. The resulting graph shows that most people tend to show a disagree attitude towards both concepts.")
    col15, col16 = st.columns([1, 1])

    AI_final.replace("-", np.nan, inplace=True)
    AI_final.dropna(subset=['AI as caretaker or loved one', 'Affection for AI'], inplace=True)
 
    fig_ana_7 = sp.make_subplots(rows=1, cols=2, subplot_titles=['Think AI as Care Taker', 'Have Affection for AI'])

    fig_ana_7.add_trace(go.Histogram(x=AI_final['AI as caretaker or loved one'], nbinsx=10, name='AI as caretaker or loved one',
                          marker=dict(color='blue')), row=1, col=1)
    AI_final_sorted = AI_final.sort_values(by=['Affection for AI'])
    fig_ana_7.add_trace(go.Histogram(x=AI_final_sorted['Affection for AI'], nbinsx=10, name='Affection for AI',
                          marker=dict(color='pink')), row=1, col=2)
    fig_ana_7.update_xaxes(categoryorder='category ascending', col=1)

    col15.plotly_chart(fig_ana_7)
    
    st.markdown("This is an interesting finding as it reveals that, despite the advancements in AI technology, people still maintain a clear distinction between AI and human relationships. The data suggests that people are not yet ready to accept AI as a substitute for human interactions, care-taking or affection, however, there are more people agree AI as care taker than have affection with AI, indicating that for future AI develoment and use, people do have favoable attitude to use it as a care taker.")
    
    #7
    st.subheader("Do People Think AI Developers Are Ethical?") 

    col17, col18 = st.columns([1, 1])
    
    col17.markdown("The analysis of respondents' attitudes towards the ethics of AI developers reveals an interesting finding. While most respondents neither agree nor disagree with the ethical concerns of AI development, a larger number of people agree that AI developers are ethical compared to those who disagree. This result was unexpected and suggests that the general public may not perceive AI as a significant threat. Overall, these findings provide valuable insights into the perceptions and attitudes of the general public towards AI development, which can be useful in guiding the development and implementation of AI technologies in the future.")
   
    fig_ana_8 = px.histogram(AI_final, x='Developers are ethical', y='Count', color = 'Age',category_orders = category_orders_dict)
    col18.plotly_chart(fig_ana_8)



if selected=="Conclusion":  
        st.title("Conclusion")
        st.markdown("1. The majority of people perceive AI as a robot, which could be influenced by popular culture and media portrayals of AI as humanoid machines. Where younger women aged 18-24 tend to have a more nuanced and diverse understanding of AI, possibly influenced by their exposure to technology and its applications in various fields.")
        st.markdown("2. Media coverage and fictional portrayals of AI can shape people's perceptions and attitudes towards this technology. The findings suggest that there is a need for accurate and responsible reporting on AI to counterbalance dystopian or apocalyptic themes prevalent in popular media.")
        st.markdown("3. People believe that AI is capable of replacing human jobs and is capable of logical thinking and problem-solving, but not emotions. This indicates that people see AI as a technology with multiple personalities and functions that can make both positive and negative decisions.")
        st.markdown("4. The most commonly used AI technologies in people's daily lives are Predictive text or search algorithms, Digital recommendation systems, and Wireless networks. This may be due to the fact that these technologies have become an integral part of people's daily routines, where people use AI more often as search engines rather than actual tools of use, such as cars driving. ")
        st.markdown("5. The analysis of people's affection for AI and see AI as care taker suggests that people are not yet ready to accept AI as a substitute for human interactions, care-taking, or affection. But, there is a favorable attitude towards using AI as a care-taker. This finding indicates that AI developers and researchers should focus on developing AI systems that can provide care-taking and support functions in a way that aligns with people's values and beliefs.")
        st.markdown("6. Most respondents neither agree nor disagree with the ethical concerns of AI development, but a larger number of people agree that AI developers are ethical compared to those who disagree.")
    
    
if selected=="References":
    st.title("Data References")
    st.markdown("Baker, Samuel, Scott, Suzanne, and Toprac, Paul. Public Understanding of Artificial Intelligence through Entertainment Media: Media Representations of Artificial Intelligence  AI    GM_April 10  2020_09.26_cleaned.xlsx. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2021-10-15. https://doi.org/10.3886/E152542V1-128760.")
    st.dataframe(raw_data)
    
    


    
    

    
    
    
    

    
    
    



