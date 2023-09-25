# Libraries
import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stoggle import stoggle
from streamlit_extras.badges import badge

# Custom Files
from encoding import *
from  CustomData import * 

#URL = 'http://127.0.0.1:8000' for local
URL = 'https://home-loan-approval-api.onrender.com'


# Header 
st.set_page_config(
    page_title="Loan Approval",
    page_icon="💵",
    layout="wide"
)

badge(type="github", name="kinba09/Home_Loan_Approval")



# Intro 
st.markdown("<h1 style = 'text-align:center;'> Welcome to Loan Approval 💵 </h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

#here add github links like a small icon on top get it from community https://extras.streamlit.app/Badges
#add kaggle link here after uploading the notebook in kaggle

content = """
<div style="text-align: center;">
    <h5>Are you looking to secure a loan for your dreams?</h5>
    <p>At Loan Approval Predictor, we bring you a powerful machine learning model that can help you navigate the loan approval process with confidence.</p>
    <p>Our model takes into account a comprehensive set of parameters, including gender, marital status, dependents, education, employment status, loan amount, credit history, property area, total income, and loan term in years. With this wealth of information, we can provide you with a clear and accurate prediction of your loan eligibility.</p>
</div>
"""

st.markdown(content, unsafe_allow_html=True)


st.divider()




st.markdown("""
    <style>
        div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 29px;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
        div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 29px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
        div[class*="stSelectbox"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Data required for prediction

a, b, c = st.columns(3,gap="medium")

with a:
    
    min_LoanAmount_encoding = min(LoanAmount_encoding)
    max_LoanAmount_encoding = max(LoanAmount_encoding)
    loanAmount = int(st.slider('Loan Amount needed in thousands',min_value = min_LoanAmount_encoding,max_value = max_LoanAmount_encoding))
    

with b:

    min_Total_Income_encoding = min(Total_Income_encoding)
    max_Total_Income_encoding= max(Total_Income_encoding)
    total_Income = int(st.slider('Total household income',min_value = min_Total_Income_encoding, max_value = max_Total_Income_encoding))
    
with c:

    loan_Term_years = int(st.selectbox('Loan term years', Loan_Term_years_encoding))
    
st.markdown("<br><br>", unsafe_allow_html=True)

d,e,f,g = st.columns(4,gap="medium")

with d:
    credit_History = int(st.radio('Credit History', Credit_History_encoding, help="1 if you have credit history else 0"))

with e:
    gender = st.radio('Gender', Gender_encoding)

with f:
    married = st.radio('Married',Married_encoding, index=0)

with g:
    education = st.radio('Education', Education_encoding)

st.markdown("<br><br>", unsafe_allow_html=True)

h,i,j = st.columns(3, gap="medium")

with h:
    dependents = st.selectbox('Dependents', Dependents_encoding)

with i:
    self_Employed = st.selectbox('Self Employed',Self_Employed_encoding)

with j:
    property_Area = st.selectbox('Property Area', Property_Area_encoding)

st.markdown("<br><br>", unsafe_allow_html=True)


# Preparing the request Body 
request_body =     {
        "LoanAmount" : loanAmount,
        "Total_Income"  : total_Income,
        "Loan_Term_years" : loan_Term_years, 
        "Credit_History" : credit_History,
        "Gender" : gender,
        "Married" : married,
        "Education" :education,
        "Dependents" : dependents,
        "Self_Employed" : self_Employed,
        "Property_Area" :property_Area
        }


status_submit = st.button("Submit")
st.divider()

# Answer section 
k, l, m = st.columns([1,2,4])
ans_val = 'Click Submit!'

with k: 
    st.write('<h3>Prediction : </h3>', unsafe_allow_html=True) 
with l:
    ans = st.empty()
    ans.code(ans_val) #ans.code(ans_val)
with m:
    st.write(" ")

if status_submit:
    response = requests.get(URL, json = request_body).json()
    # ans.code(response['prediction'])  #ans.code(response['prediction'])
    ballon_check = response['Ballons']
    if ballon_check:
        #st.balloons()
        ans.success(response['prediction'],icon="✅")

        rain(
        emoji="🥳",
        font_size=100,
        falling_speed=8,
        animation_length="2s",
        )
    else:
        ans.error(response['prediction'],icon="🚫")


st.divider()

#n, o, p = st.columns([0.5,3,4])
#with n:
#    st.write('<h5> Note :  </h5>', unsafe_allow_html=True)

#with o:
#    st.write('<h8> Loan amount, total income, and credit history have a higher impact on this model, meaning that these factors are more predictive of whether or not a borrower will be able to repay a loan.</h8>', unsafe_allow_html=True)

n, o = st.columns([4,4])
with n:
    stoggle(
    "Note",
    """ Loan amount, Total income, and Credit history have a <span style='color: red;'> <u><b>higher impact</b></u></span> on this model, meaning that these factors are more predictive of whether or not a borrower will be able to repay a loan.""",
)

