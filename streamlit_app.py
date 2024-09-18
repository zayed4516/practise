import streamlit as st
import pandas as pd

# عنوان التطبيق
st.header('File Upload')

# تحميل الملف
file = st.file_uploader('Upload dataset', type=['csv'])

# تحقق مما إذا تم تحميل ملف
if file is not None:
    # قراءة البيانات من الملف
    df = pd.read_csv(file)
    # عرض البيانات
    st.write(df)

    # إضافة شريط لاختيار عدد الصفوف
    num_row = st.slider('Choose num rows', min_value=1, max_value=len(df))

    # إضافة اختيار للأعمدة
    names_col = st.multiselect('Choose columns', df.columns.to_list())

    # عرض البيانات بناءً على الأعمدة المختارة
    if names_col:
        st.write(df.loc[:num_row, names_col])
    else:
        st.write(df.head(num_row))
    else:
        st.write("Please upload a CSV file.")

