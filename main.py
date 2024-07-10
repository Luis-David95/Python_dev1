import zipfile
import os
import xml.etree.ElementTree as ET

def extract_apk(apk_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with zipfile.ZipFile(apk_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def process_xml_files(xml_dir):
    for root, _, files in os.walk(xml_dir):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                print(f"Processing XML file: {xml_file}")
                tree = ET.parse(xml_file)
                root = tree.getroot()
                for child in root:
                    print(f"Element: {child.tag}, Text: {child.text}")

if __name__ == "__main__":
   # apk_file = '...' 
    output_directory = "D:\\snake\\work\\Py_2" 
   # extract_apk(apk_file, output_directory)
    xml_directory = os.path.join(output_directory) 
    process_xml_files(xml_directory)

    