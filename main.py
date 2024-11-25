import streamlit as st
import pandas as pd
import json
import requests
import os
import zipfile
import xmltodict
import numpy as np

def process_API(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.DataFrame.from_dict(json.loads(response.content))
        if len(data)==0: return []
        return data
    else: return []

def programming_projects():
    git_repos = process_API("https://api.github.com/users/tarris1/repos")
    commits =  [len(process_API(f"https://api.github.com/repos/Tarris1/{i}/commits")) for i in git_repos["name"]]
    git_repos["commit_count"] = commits
    git_org = process_API("https://api.github.com/orgs/lecturaorg/repos")
    commits = [len(process_API(f"https://api.github.com/repos/Lecturaorg/{i}/commits")) for i in git_org["name"]]
    git_org["commit_count"] = commits
    repos = pd.concat([git_repos,git_org],ignore_index=True)
    st.write("Below you will find my different programming projects")
    st.table(repos[["name", "description", "created_at", "updated_at", "size","commit_count"]].sort_values("size", ascending=False))

def read_json(url):
    with open(url) as l: return json.load(l) 

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

def write_section(data):
    sub_sections = ["header","sub-header","description","location"]
    for i in sub_sections:
        text = data[i]
        st.write(text)

def write_CV(df):
    for index, row in df.iterrows():
        header = '<p style="font-size:16px; font-weight:700; margin-bottom:5px;">' + row["header"]
        if row["company"]: header += " - " + row["company"] + "</p>"
        else: header += "</p>"
        if row["subheader"]: 
            subheader = '<p style="font-size:12px";>' + str(row["subheader"]) + "</p>"
        else: subheader = ""
        st.write(header, unsafe_allow_html=True)
        if subheader: st.write(subheader, unsafe_allow_html=True)
        st.write(row["description"], unsafe_allow_html=True)

def main():
    st.write("# Welcome to my home page! ")
    CV, projects, personal = st.tabs(["Curriculum Vitae", "Projects", "Personal"])
    with CV:
        st.header("Tarjei Sandsnes")
        #write_section(read_json("CV_sections/masters.json"))
        df = read_excel("CV_sections/CV_main.xlsx")
        write_CV(df[0])
    #programming_projects()

if __name__ == "__main__":
    main()