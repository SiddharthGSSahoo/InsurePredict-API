from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Literal
import pandas as pd

class InsuranceClaimInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    claim_reason: Annotated[Literal["Travel", "Medical", "Phone", "Other"], 
                           Field(..., alias="Claim Reason", title="Claim Reason", 
                                 description="Reason for the insurance claim (Travel, Medical, Phone, or Other)...", 
                                 examples=["Medical"])]

    
    data_confidentiality: Annotated[Literal["Low","High","Medium","Very low"], 
                                   Field(...,alias="Data confidentiality",title="Data Confidentiality", 
                                         description="Level of data confidentiality (Low, High, Medium, Very low)...", 
                                         examples=["Medium"])]
    
    claim_amount: Annotated[float, 
                           Field(...,alias="Claim Amount",gt=0,title="Claim Amount", 
                                 description="Total amount of the claim in currency units...", 
                                 examples=[1200.50])]
    
    premium_amount_ratio: Annotated[float, 
                                   Field(...,alias="Premium/Amount Ratio",gt=0,lt=1,title="Premium/Amount Ratio", 
                                         description="Ratio of premium to claim amount (between 0 and 1)...", 
                                         examples=[0.05])]

    def to_dataframe(self): # Returns a dataframe with the exact column names the model expects
        return pd.DataFrame([self.model_dump(by_alias=True)])
