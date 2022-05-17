import pandas as pd
import xml.etree.ElementTree as ET
# from os import listdir

my_list = []
my_dictionary = {}


# for files in listdir("my_Files"):
#     with open(files, "r", encoding="utf-8") as content:
my_tree = ET.parse("JAJA_MIRABEL.xml")
my_root = my_tree.getroot()

for elements in my_root[5]:
    my_dictionary.update({elements.tag: elements.text})
    for sub_elem in elements:
        for sub2_elem in sub_elem:
            # my_dictionary.update({sub2_elem.tag: sub2_elem.text})
            for sub3_elem in sub2_elem:
                for sub4_elem in sub3_elem:
                    for sub5_elem in sub4_elem:
                        for sub6_elem in sub5_elem:
                            my_dictionary.update({sub6_elem.tag: sub6_elem.text})
                            my_dictionary.pop("PERSON_NAME", None)
                            my_dictionary.pop("ISSUER_OF_PATIENT_ID", None)
                            my_dictionary.pop("OTHER_PATIENT_IDS", None)
                            my_dictionary.pop("CATEGORIES", None)
                            my_dictionary.pop("SPHERICAL_EQUIVALENT", None)
                            my_dictionary.pop("NORMATIVE_DATA", None)
                            my_dictionary.pop("VISITS", None)
                            my_list.append(my_dictionary)
print(my_dictionary)
df = pd.DataFrame(my_list)
df.drop_duplicates(keep="first", inplace=True)
df.reset_index(drop=True, inplace=True)
writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="sheet1")
writer.save()
print("xml file converted successfully")
