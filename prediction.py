import streamlit as st
import pandas as pd
import joblib

st.title('Student Dropout Prediction')

model = joblib.load('model/xgb.joblib')

st.subheader('Demographic')

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox('Gender', ['Female', 'Male'])
    nationality_map = {
        "Portuguese": 1,
        "German": 2,
        "Spanish": 6,
        "Italian": 11,
        "Dutch": 13,
        "English": 14,
        "Lithuanian": 17,
        "Angolan": 21,
        "Cape Verdean": 22,
        "Guinean": 24,
        "Mozambican": 25,
        "Santomean": 26,
        "Turkish": 32,
        "Brazilian": 41,
        "Romanian": 62,
        "Moldova (Republic of)": 100,
        "Mexican": 101,
        "Ukrainian": 103,
        "Russian": 105,
        "Cuban": 108,
        "Colombian": 109
    }
    nationality = st.selectbox("Nationality", list(nationality_map.keys()))
    nationality_val = nationality_map[nationality]

with col2:
    age = st.number_input('Age', 15, 70, 20)
    special_needs = st.selectbox('Special Needs', ['No', 'Yes'])

with col3:
    marital_status_map = {
        "Single": 1,
        "Married": 2,
        "Widower": 3,
        "Divorced": 4,
        "Facto Union": 5,
        "Legally Separated": 6
    }
    marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))
    marital_status_val = marital_status_map[marital_status]
    displaced = st.selectbox('Displaced', ['No', 'Yes'])

col1, col2 = st.columns(2)
with col1:
    mother_qual_map = {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equivalent": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equivalent": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    }
    mother_qual = st.selectbox("Mother Qualification", list(mother_qual_map.keys()))
    mother_qual_val = mother_qual_map[mother_qual]
    father_qual_map = {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equivalent": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equivalent": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    }
    father_qual = st.selectbox("Father Qualification", list(father_qual_map.keys()))
    father_qual_val = father_qual_map[father_qual]

with col2:
    mother_occupation_map = {
        "Student": 0,
        "Representatives of Legislative & Executive, Directors, Executive Managers": 1,
        "Specialists in Intellectual & Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security & Safety Workers and Sellers": 5,
        "Farmers & Skilled Workers in Agriculture, Fisheries & Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "Blank": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces personnel": 103,
        "Directors of administrative and commercial services": 112,
        "Hotel, catering, trade and other services directors": 114,
        "Specialists in physical sciences, mathematics, engineering & related techniques": 121,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in finance, accounting, admin, public & commercial relations": 124,
        "Intermediate level science & engineering technicians": 131,
        "Intermediate level health technicians & professionals": 132,
        "Intermediate level legal, social, sports, cultural services technicians": 134,
        "Information & communication technology technicians": 135,
        "Office workers, secretaries & data processing operators": 141,
        "Data, accounting, statistical, financial & registry operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers & the like": 153,
        "Protection & security services personnel": 154,
        "Market-oriented farmers & skilled agricultural/animal production workers": 161,
        "Farmers, livestock keepers, fishermen, hunters & gatherers, subsistence": 163,
        "Skilled construction workers": 171,
        "Skilled workers in metallurgy, metalworking & similar": 172,
        "Skilled workers in electricity & electronics": 174,
        "Workers in food processing, woodworking, clothing & other industries/crafts": 175,
        "Fixed plant & machine operators": 181,
        "Assembly workers": 182,
        "Vehicle drivers & mobile equipment operators": 183,
        "Unskilled workers in agriculture, animal production, fisheries & forestry": 192,
        "Unskilled workers in extractive industry, construction, manufacturing & transport": 193,
        "Meal preparation assistants": 194,
        "Street vendors & street service providers": 195
    }

    mother_occupation = st.selectbox("Mother's Occupation", list(mother_occupation_map.keys()))
    mother_occupation_val = mother_occupation_map[mother_occupation]
    father_occupation_map = {
        "Student": 0,
        "Representatives of Legislative & Executive, Directors, Executive Managers": 1,
        "Specialists in Intellectual & Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security & Safety Workers and Sellers": 5,
        "Farmers & Skilled Workers in Agriculture, Fisheries & Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "Blank": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces personnel": 103,
        "Directors of administrative and commercial services": 112,
        "Hotel, catering, trade and other services directors": 114,
        "Specialists in physical sciences, mathematics, engineering & related techniques": 121,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in finance, accounting, admin, public & commercial relations": 124,
        "Intermediate level science & engineering technicians": 131,
        "Intermediate level health technicians & professionals": 132,
        "Intermediate level legal, social, sports, cultural services technicians": 134,
        "Information & communication technology technicians": 135,
        "Office workers, secretaries & data processing operators": 141,
        "Data, accounting, statistical, financial & registry operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers & the like": 153,
        "Protection & security services personnel": 154,
        "Market-oriented farmers & skilled agricultural/animal production workers": 161,
        "Farmers, livestock keepers, fishermen, hunters & gatherers, subsistence": 163,
        "Skilled construction workers": 171,
        "Skilled workers in metallurgy, metalworking & similar": 172,
        "Skilled workers in electricity & electronics": 174,
        "Workers in food processing, woodworking, clothing & other industries/crafts": 175,
        "Fixed plant & machine operators": 181,
        "Assembly workers": 182,
        "Vehicle drivers & mobile equipment operators": 183,
        "Unskilled workers in agriculture, animal production, fisheries & forestry": 192,
        "Unskilled workers in extractive industry, construction, manufacturing & transport": 193,
        "Meal preparation assistants": 194,
        "Street vendors & street service providers": 195
    }
    father_occupation = st.selectbox("Father's Occupation", list(father_occupation_map.keys()))
    father_occupation_val = father_occupation_map[father_occupation]

st.subheader('Application')

col1, col2 = st.columns(2)

with col1:
    application_mode_map = {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2 (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    }
    application_mode = st.selectbox("Application Mode", list(application_mode_map.keys()))
    application_mode_val = application_mode_map[application_mode]
    international = st.selectbox('International', ['No', 'Yes'])
    application_order = st.number_input('Application Order', 0, 9, 1)
    prev_qual_map = {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equivalent": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equivalent": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43
    }
    prev_qual = st.selectbox("Previous Qualification", list(prev_qual_map.keys()))
    prev_qual_val = prev_qual_map[prev_qual]

with col2:
    course_map = {
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991
    }
    course = st.selectbox("Course", list(course_map.keys()))
    course_val = course_map[course]
    daytime = st.selectbox('Attendance', ['Evening', 'Daytime'])
    admission_grade = st.number_input('Admission Grade', 0, 200, 120)
    prev_grade = st.number_input('Previous Grade', 0, 200, 120)

st.subheader('Financial')

col1, col2, col3 = st.columns(3)

with col1:
    debtor = st.selectbox('Debtor', ['No', 'Yes'])

with col2:
    tuition = st.selectbox('Tuition Up To Date', ['No', 'Yes'])

with col3:
    scholarship = st.selectbox('Scholarship', ['No', 'Yes'])

st.subheader('Economic')

col1, col2, col3 = st.columns(3)

with col1:
    unemployment = st.number_input('Unemployment Rate', 0.0, 100.0, 10.0)

with col2:
    inflation = st.number_input('Inflation Rate', -10.0, 100.0, 2.0)

with col3:
    gdp = st.number_input('GDP', -10.0, 10.0, 1.0)

gender_val = 1 if gender == 'Male' else 0
daytime_val = 1 if daytime == 'Daytime' else 0

st.subheader('Academic')

st.markdown('#### Semester 1')
col1, col2, col3 = st.columns(3)

with col1:
    cu1_credited = st.number_input('Credited 1st', 0, 20, 0)
    cu1_enrolled = st.number_input('Enrolled 1st', 0, 20, 6)

with col2:
    cu1_eval = st.number_input('Evaluations 1st', 0, 20, 6)
    cu1_approved = st.number_input('Approved 1st', 0, 20, 5)

with col3:
    cu1_grade = st.number_input('Grade 1st', 0, 20, 12)
    cu1_no_eval = st.number_input('No Eval 1st', 0, 20, 0)

st.markdown('#### Semester 2')
col1, col2, col3 = st.columns(3)

with col1:
    cu2_credited = st.number_input('Credited 2nd', 0, 20, 0)
    cu2_enrolled = st.number_input('Enrolled 2nd', 0, 20, 6)

with col2:
    cu2_eval = st.number_input('Evaluations 2nd', 0, 20, 6)
    cu2_approved = st.number_input('Approved 2nd', 0, 20, 5)

with col3:
    cu2_grade = st.number_input('Grade 2nd', 0, 20, 12)
    cu2_no_eval = st.number_input('No Eval 2nd', 0, 20, 0)


def yn(x): return 1 if x == 'Yes' else 0


if st.button('Predict'):
    approval_rate_1st_sem = (
        cu1_approved / cu1_enrolled
        if cu1_enrolled > 0 else 0
    )
    approval_rate_2nd_sem = (
        cu2_approved / cu2_enrolled
        if cu2_enrolled > 0 else 0
    )
    total_approved = cu1_approved + cu2_approved
    approved_trend = cu2_approved - cu1_approved
    total_enrolled = cu1_enrolled + cu2_enrolled
    cumulative_approval_rate = total_approved / total_enrolled if total_enrolled > 0 else 0
    avg_grade = (cu1_grade + cu2_grade) / 2
    grade_trend = cu2_grade - cu1_grade
    parents_education_avg = (mother_qual_val + father_qual_val) / 2
    bad_economy = int((unemployment > pd.read_csv('data/students_performance.csv')['Unemployment_rate'].median()) & (gdp < 0))
    input_data = pd.DataFrame([{
        'Marital_status': marital_status_val,
        'Application_mode': application_mode_val,
        'Application_order': application_order,
        'Course': course_val,
        'Daytime_evening_attendance': daytime_val,
        'Previous_qualification': prev_qual_val,
        'Previous_qualification_grade': prev_grade,
        'Nacionality': nationality_val,
        'Mothers_qualification': mother_qual_val,
        'Fathers_qualification': father_qual_val,
        'Mothers_occupation': mother_occupation_val,
        'Fathers_occupation': father_occupation_val,
        'Admission_grade': admission_grade,
        'Displaced': yn(displaced),
        'Educational_special_needs': yn(special_needs),
        'Debtor': yn(debtor),
        'Tuition_fees_up_to_date': yn(tuition),
        'Gender': gender_val,
        'Scholarship_holder': yn(scholarship),
        'Age_at_enrollment': age,
        'International': yn(international),
        'Curricular_units_1st_sem_credited': cu1_credited,
        'Curricular_units_1st_sem_enrolled': cu1_enrolled,
        'Curricular_units_1st_sem_evaluations': cu1_eval,
        'Curricular_units_1st_sem_approved': cu1_approved,
        'Curricular_units_1st_sem_grade': cu1_grade,
        'Curricular_units_1st_sem_without_evaluations': cu1_no_eval,
        'Curricular_units_2nd_sem_credited': cu2_credited,
        'Curricular_units_2nd_sem_enrolled': cu2_enrolled,
        'Curricular_units_2nd_sem_evaluations': cu2_eval,
        'Curricular_units_2nd_sem_approved': cu2_approved,
        'Curricular_units_2nd_sem_grade': cu2_grade,
        'Curricular_units_2nd_sem_without_evaluations': cu2_no_eval,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp,
        'Approval_rate_1st_sem': approval_rate_1st_sem,
        'Approval_rate_2nd_sem': approval_rate_2nd_sem,
        'Total_approved': total_approved,
        'Approved_trend': approved_trend,
        'Total_enrolled': total_enrolled,
        'Cumulative_approval_rate': cumulative_approval_rate,
        'Avg_grade': avg_grade,
        'Grade_trend': grade_trend,
        'Parents_education_avg': parents_education_avg,
        'Bad_economy': bad_economy
    }])

    prediction = model.predict(input_data)[0]

    label_map = {
        0: 'Dropout',
        1: 'Graduate'
    }

    if prediction == 0:
        st.error('Dropout')
    else:
        st.success(label_map[prediction])
