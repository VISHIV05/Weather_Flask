import pandas as pd
import xml.etree.ElementTree as ET
from config import csv_file,excel_File,XML_file

def convert_to_csv(df):
    df.to_csv(csv_file, index=False)
    return csv_file

def convert_to_excel(df):
    df.to_excel(excel_File, index=False)
    return excel_File

def convert_to_xml(df):
    root = ET.Element("weather_data")
    for index,row in df.iterrows():
        city_element=ET.SubElement(root,"city")
        ET.SubElement(city_element,"name").text = str(row['City'])
        ET.SubElement(city_element,"temperature").text  = str(row['Temperature'])
        ET.SubElement(city_element,"humidity").text  = str(row['Humidity'])
        ET.SubElement(city_element,"weather").text  = str(row['Weather'])
    tree =ET.ElementTree(root)
    tree.write(XML_file)
    return XML_file    