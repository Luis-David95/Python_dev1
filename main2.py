import zipfile
import os
import xml.etree.ElementTree as ET

def extract_apk(apk_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(apk_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def read_xml_files(xml_dir):
    for root, _, files in os.walk(xml_dir):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                print(f"Reading XML file: {xml_file}")
                f=open(xml_file,errors="ignore")
                xml_content = f.read()
                print(f"XML content:\n{xml_content}")
                # with open(xml_file, 'r',encoding="utf8") as f:
                #     xml_content = f.read()
                #     print(f"XML content:\n{xml_content}")

if __name__ == "__main__":
    apk_file = '///' 
    output_directory = "D:\\snake\\work\\Py_2"  
    #extract_apk(apk_file, output_directory)
    xml_directory = os.path.join(output_directory)  #
    read_xml_files(xml_directory)
