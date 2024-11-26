import streamlit as st
import pandas as pd
import os
import zipfile
import xmltodict
import numpy as np

def read_sheets(url):
    directory_to_extract_to = os.path.join(url.split("/")[0])
    zip_ref = zipfile.ZipFile(url, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
    path_to_workbook = os.path.join(directory_to_extract_to, 'xl', 'workbook.xml')
    with open(path_to_workbook, 'r') as f:
        xml = f.read()
        dictionary = xmltodict.parse(xml)
        return [i["@name"] for i in dictionary['workbook']['sheets']['sheet']]

def read_excel(url):
    sheet_names = read_sheets(url)
    return [pd.read_excel(url, sheet_name=i).replace(np.nan, None) for i in sheet_names]

def write_CV(main_data, skills_data):
    def main_section(df):
        education_format = "font-size:36px; font-weight:700; margin-bottom:0px; text-decoration: underline;"
        education_written = False
        header_format = "font-size:28px; font-weight:700; margin-bottom:0px; color:darkred;"
        subheader_format = "font-size:20px; margin-bottom:0px;"
        period_format = "margin-bottom:0px; font-style:italic;"
        st.write(f'<p style="{education_format}">Experience</p>',unsafe_allow_html=True)
        for index, row in df.iterrows():
            header = f'<p style="{header_format}">' + row["header"]
            if row["company"]: header += " - " + row["company"] + "</p>"
            else: header += "</p>"
            period_text = str(row["from"].month_name()) + " " + str(row["from"].year) + " - " + str(row["to"].month_name()) + " " + str(row["to"].year)
            period = f'<p style="{period_format}">{period_text}</p>'
            if row["subheader"]: 
                subheader = f'<p style="{subheader_format}">' + str(row["subheader"]) + "</p>"
            else: subheader = ""
            skills = "Key skills: " + row["skills"]
            if row["type"]=="education" and education_written == False:
                st.write(f'<p style="{education_format}">{"Education"}</p>',unsafe_allow_html=True)
                education_written = True
            st.write(header, unsafe_allow_html=True)
            if subheader: st.write(subheader, unsafe_allow_html=True)
            st.write(period, unsafe_allow_html=True)
            st.write(row["description"], unsafe_allow_html=True)
            st.write(skills)
    def skill_section(skills):
        labels = [{"label":"Technical Skills", "data":"technical_skills"}, {"label":"Languages", "data":"languages"},
                    {"label":"Personal Skills", "data":"personal_skills"}]#,{"label":"Other Experiences", "data":"other_experiences"}]
        label_format = '<p style="font-size:24px; font-weight:700; margin-bottom:0px; text-decoration: underline;">'
        row_format = '<p style="font-size:16px; margin-bottom:0px;">'
        for label in labels:
            st.write(label_format+label["label"]+"</p>", unsafe_allow_html=True)
            for row in skills[label["data"]]:
                if row is not None: st.write(row_format+row+"</p>", unsafe_allow_html=True)
    main, skills = st.columns([3,1])
    with main: main_section(main_data)
    with skills: skill_section(skills_data)


def create_urls():
    urls = [{"label":"https://www.linkedin.com/in/tarjei-sandsnes/", "url":True, "icon":"https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"},
            {"label":"https://github.com/Tarris1", "url":True, "icon":"https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"}
            , {"label":"https://www.goodreads.com/tarjei_sandsnes","url":True, "icon":"https://upload.wikimedia.org/wikipedia/commons/5/5a/Goodreads_logo_-_SuperTinyIcons.svg"}]
    links = ""
    for url in urls:
        if url["url"]: text = f'<a href="{url["label"]}"><img style="max-height:30px;" src="{url["icon"]}"/></a>'
        else: text = url["label"]
        links+=text
    return '<p style="margin-bottom:0px;">'+links+"</p>" #st.write('<p style="margin-bottom:0px;">'+links+"</p>", unsafe_allow_html=True)

def create_header():
    intro, picture = st.columns([9, 2])
    with intro: 
        st.markdown('<header style = "font-size:40px; text-align: center;">Welcome!</header>', unsafe_allow_html=True)
        header_text = read_excel("header_sections/header_text.xlsx")
        st.write(header_text[0].iloc[0]["title"])
    with picture: 
        st.image("TS.jpg", width=200)  # Adjust the width as needed
        st.markdown(create_urls(), unsafe_allow_html=True)
        st.write("tarjei_sandsnes@outlook.com")

def main():
    st.set_page_config(layout="wide", page_title="Tarjei's Page")
    create_header()
    CV, projects, personal = st.tabs(["Curriculum Vitae", "Projects", "Personal"])
    with CV:
        CV_main = read_excel("CV_sections/CV_main.xlsx")
        CV_skills = read_excel("CV_sections/CV_skills.xlsx")
        write_CV(CV_main[0], CV_skills[0])
    #programming_projects()
    #https://discuss.streamlit.io/t/customizing-the-appearance-of-tabs/48913 #tab formatting

if __name__ == "__main__":
    main()