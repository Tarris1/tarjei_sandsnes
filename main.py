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
    st.write('<p style="font-size:36px; font-weight:700; margin-bottom:0px; text-decoration: underline;">Experience</p>',unsafe_allow_html=True)
    education_written = False
    for index, row in df.iterrows():
        header = '<p style="font-size:28px; font-weight:700; margin-bottom:0px; color:darkred;">' + row["header"]
        if row["company"]: header += " - " + row["company"] + "</p>"
        else: header += "</p>"
        period = str(row["from"].month_name()) + " " + str(row["from"].year) + " - " + str(row["to"].month_name()) + " " + str(row["to"].year)
        if row["subheader"]: 
            subheader = '<p style="font-size:20px; margin-bottom:0px;">' + str(row["subheader"]) + "</p>"
        else: subheader = ""
        skills = "Key skills: " + row["skills"]
        if row["type"]=="education" and education_written == False:
            st.write('<p style="font-size:36px; font-weight:700; margin-bottom:0px; text-decoration: underline;">Education</p>',unsafe_allow_html=True)
            education_written = True
        st.write(header, unsafe_allow_html=True)
        if subheader: st.write(subheader, unsafe_allow_html=True)
        st.write(period)
        st.write(row["description"], unsafe_allow_html=True)
        st.write(skills)

def main():
    st.write('<p>Welcome! <img src="TS.jpg"></p>', unsafe_allow_html=True)
    CV, projects, personal = st.tabs(["Curriculum Vitae", "Projects", "Personal"])
    with CV:
        df = read_excel("CV_sections/CV_main.xlsx")
        write_CV(df[0])
    #programming_projects()

if __name__ == "__main__":
    main()