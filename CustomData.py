from pydantic import BaseModel

class InputData(BaseModel):
    Gender : str
    Married: str    
    Dependents: str 
    Education : str
    Self_Employed: str
    LoanAmount	: int
    Credit_History: int
    Property_Area: str
    Total_Income: int
    Loan_Term_years: int

class EncodedData(BaseModel):
    Gender : int
    Married: int    
    Dependents: int 
    Education : int
    Self_Employed: int
    LoanAmount	: int
    Credit_History: int
    Property_Area: int
    Total_Income: int
    Loan_Term_years: int

