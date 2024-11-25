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

def write_CV(df):
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

def create_urls():
    urls = [{"label":"https://www.linkedin.com/in/tarjei-sandsnes/", "url":True, "icon":"https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"},
            {"label":"https://github.com/Tarris1", "url":True, "icon":"https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"}, {"label":"https://www.goodreads.com/tarjei_sandsnes","url":True, "icon":"https://upload.wikimedia.org/wikipedia/commons/5/5a/Goodreads_logo_-_SuperTinyIcons.svg"}
            #,{"label":"tarjei_sandsnes@outlook.com","url":False}, {"label":"+47 483 95 603", "url":False}
            ]
    for url in urls:
        if url["url"]: text = f'<a href="{url["label"]}"><img style="max-height:30px;" src="{url["icon"]}"/></a>'
        else: text = url["label"]
        st.write('<p style="margin-bottom:0px;">'+text+"</p>", unsafe_allow_html=True)

def create_header():
    intro, picture, links = st.columns([8, 1, 1])
    with intro: 
        st.markdown('<p style = "font-size:40px;">Welcome!</p>', unsafe_allow_html=True)
    with picture: 
        st.image("TS.jpg", width=300)  # Adjust the width as needed
    with links: create_urls()

def main():
    st.set_page_config(layout="wide", page_title="Tarjei's Page")
    create_header()
    CV, projects, personal = st.tabs(["Curriculum Vitae", "Projects", "Personal"])
    with CV:
        df = read_excel("CV_sections/CV_main.xlsx")
        write_CV(df[0])
    #programming_projects()

if __name__ == "__main__":
    main()