import os
from pandas import read_csv
from dataframe_image import export
import streamlit as st
st.set_page_config(
    page_title="Conversion Report", 
    page_icon=None)

def table_styler(dataframe):
    return dataframe.style.set_table_styles(
        [{'selector' : 'th',
            'props' : [('background', '#40254c'),
                        ('color' , '#fff3ef'),
                        ('font-family', 'helvetica'),
                        ('text-align', 'left')]},
        {'selector' : 'td',
            'props' : [('text-align', 'left'),
                        ('font-family', 'helvetica')]
        },
        {'selector' : 'tr:nth-of-type(odd)',
            'props' : [('background', '#DCDCDC')]
        },
        {'selector' : 'tr:nth-of-type(even)',
            'props' : [('background', 'white')]
        }
        ]
    )

names = {
    "Safir S":"Safir S",
    "AKHIL C MOHAN MOHAN":"AKHIL C",
    "GijoDevasia":"Gijo Devasia",
    "NajeemN":"Najeem N",
    "Fousiya P":"Thansi",
    "Vishnu D":"Vishnu D",
    "Shihabudeen A":"Shihabudeen A",
    "Rajil RajR":"Rahul Raj",
    "Chandra Mohanan":"Riyas",
    "Nibin AhammedN":"Nahas",
    "Jimmy George":"Jimmy George",
    "PRANAV C":"Pranav C",
    "Ajith MA":"Ajith M A",
    "BibinB":"Bibin B",
    "SajinS":"Nesmal",
    "FaisalA":"Haris",
    "Bijo CBabu":"Bipin C Babu",
    "Paulson K Babu":"Paulson K Babu",
    "MujeebrahmanK":"Gireesh",
    "TRUEFLEX LCM ShafeekS":"Shafeek",
    "MuhammadNiyas R":"Edison",
    "Abdul Asif A N":"Abdul Asif",
    "Rahmathulla R":"Rahmathulla R",
    "Ajo James":"Ajo James",
    "VIPIN KJ":"Vipin K J",
    "Joji J":"Joji J",
    "Ronaldo Toms":"Ronaldo Toms",
    "Sojan PAbraham":"Sojan PAbraham",
    "AzeemA":"Azeem A",
    "PoornimaRenjan":"Vineetha",
    "Prince Job":"Rohith",
    "Rakesh KR":"Shanil",
    "AnsilA":"Aneesh",
    "Aneeshkumar S":"Anas Ansari",
    "SarathkumarH":"Sarath Kumar",
    "RajeevNair":"Rajeev Nair",
    "NiyasNisamudheen":"Niyas Nisamudheen",
    "Muhammad RoshanR":"Jackson",
    "AkashChandran":"Akhil Xavior",
    "Thasny N":"Sabir",
    "Unni M":"Unni M",
    "Niyas S":"Niyas S",
    "SUJITHS":"Sujith S",
    "AjithJames":"Ajith James",
    "Vineeth R":"Josmon",
    "RameesR":"Shaheer",
    "ReenaRishad":"Hafid"

    }

# path = os.getcwd()
# files = os.listdir(path)
# files_csv = [file for file in files if file[-3:] == "csv" ]

uploaded_file = st.file_uploader("""Upload CSV report""")

if uploaded_file:
    df = read_csv(uploaded_file)

    df.drop(['HubName','CasperFHRID','OFP','Pickup', 'Undel'], axis=1, inplace=True)

    df["conversion"] = df.Del / df.OFD * 100
    df.conversion = df.conversion.astype(float)
    # df.loc[:, "conversion"] = df["conversion"].map('{:.2f}'.format)

    df = df.replace({"AgentName":names})

    ordered_df = df.sort_values(by=['conversion','OFD'],
                                        ascending=[False, False])

    styled_df = table_styler(ordered_df)

    st.table(styled_df)
    # export(styled_df, 'conversion.png')

    # img = open('conversion.png', 'rb')
    # st.download_button(label="Download Report", data=img, file_name="conversion.png")
    # img.close()

