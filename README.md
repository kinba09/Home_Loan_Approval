# Home Loan Approval
Welcome to the Home Loan Approval project! This machine learning-based web application predicts whether an individual is eligible for a home loan. It combines the power of Streamlit for the front end, FastAPI for the API, and various Python libraries for data processing and machine learning.
- #### <a href = "https://home-loan-approval.streamlit.app/"> Home_Loan_Approval Streamlit </a>
- #### <a href = "https://home-loan-approval-api.onrender.com/docs"> Home_Loan_Approval API </a>
- #### <a href = "https://www.kaggle.com/code/kinbaa/home-loan-approval-eda-prediction"> Home_Loan_Approval Kaggle </a>

# Tech Stack

This project leverages a robust tech stack to deliver accurate and efficient loan predictions:

- **Frontend:** Streamlit
- **API:** FastAPI, Pydantic
- **API hosting:** Uvicorn (local), Render
- **Machine Learning:** Scikit-Learn
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Model Serialization:** Pickle

# Getting Started
## Prerequisites
Before diving into the project, ensure you have Python installed. You can download the latest version from python.org.
## Installation
Clone the repository to your local machine:
```
git clone https://github.com/kinba09/Home_Loan_Approval.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage
Start the FastAPI server:
```
uvicorn mlapi:app --reload
```
Host Streamlit:
```
streamlit run app.py
```
## To host it on render:
- Pushed only the API-required files to the repo first and hosted them on Render
- The start command in render is ```uvicorn mlapi:app --host 0.0.0.0 --port $PORT```
```
API
  |---- CustomData.py
  |---- encoding.py
  |---- mlapi.py
  |---- requirements.txt
``` 
- Then pushed the other files and hosted them on Streamlit
```
Streamlit
  |---- app.py
  |---- encoding.py
```
# Note
* The version of Scikit Learn on Render is only up to 1.0.2. Therefore, if your pickled model is from a later version of Scikit-Learn, you may need to use the **older** pickled model (```modelold.pkl```) instead of the ```modeltest.pkl``` file. If you are planning to use the latest of Scikit Learn then use ```modeltest.pkl``` 
* The prediction streamlit might not be fast for the first time use because render takes time to boot up for the first time.
* Since I am using a free plan of render, there are only 750 Free Instance Hours per month. If the traffic is high, the prediction might not work.
Please note that the free plan of render may not be suitable for high-traffic applications. If you need a more reliable solution, you may need to upgrade to a paid plan.

Please let me know if you have any questions or suggestions.
