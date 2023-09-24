Gender_encoding = {'Female': 0, 'Male': 1}
Married_encoding = {'No': 0, 'Yes': 1}
Dependents_encoding = {'1': 1, '0': 0, '2': 2, '3+' : 3}
Education_encoding = {'Graduate': 1, 'Not Graduate': 0}
Self_Employed_encoding = {'No': 1, 'Yes': 0}
Property_Area_encoding = {'Rural': 1, 'Urban': 0, 'Semiurban': 2}



LoanAmount_encoding = [i for i in range(0, 401)]
Total_Income_encoding = [i for i in range(0, 30001)]
Loan_Term_years_encoding = [3, 5, 7, 10, 15, 20, 25, 30, 40]

Credit_History_encoding = [0, 1]


# intro = '''
# Discover a game-changing solution for predicting Barcelona rent prices. 
# Our project combines state-of-the-art machine learning, a FastAPI-based 
# ML model, and a user-friendly Streamlit frontend to provide highly accurate 
# predictions with a 98% success rate. Whether you're a landlord seeking optimal 
# pricing or a tenant looking for fair deals, our platform revolutionizes real estate decision-making.
# '''