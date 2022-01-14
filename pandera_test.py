#importing libraries
import pandas as pd 
import pandera as pa
import numpy as np

#importing sub libraries
from pandera.typing import DataFrame, Series
from pandera.errors import SchemaError

#Input schema definition
class InputSchema(pa.SchemaModel):
    state: Series[str] = pa.Field(coerce=True)
    city: Series[str] = pa.Field(coerce=True)
    price: Series[int] = pa.Field(coerce=True)
    perc: Series[float] = pa.Field(coerce=True, nullable=True)

#Output schema definition
class OutputSchema(InputSchema):
    state: Series[str] = pa.Field(coerce=True)
    city: Series[str] = pa.Field(coerce=True)
    price: Series[str] = pa.Field(coerce=True)
    perc: Series[float] = pa.Field(coerce=True, nullable=True)


#Defined decorator for the transformation
@pa.check_types
def transform(df: DataFrame[InputSchema]) -> DataFrame[OutputSchema]:
    return df

#Valid dataframe for schema
df = pd.DataFrame(data={
        'state': ['NY','FL','GA','CA'],
        'city': ['New York', 'Miami', 'Atlanta', 'San Francisco'],
        'price': [8, 12, 10, 16],
        'perc': [0.8,0.7,0.4,np.nan]
    })
try:    
    df = transform(df)

except SchemaError as e:
    raise(e)

#Invalid dataframe for schema
invalid_df = pd.DataFrame(data={
        'state': ['NY','FL','GA','CA'],
        'city': ['New York', 'Miami', 'Atlanta', 'San Francisco'],
        'price': [8, 12, 10, np.nan],
        'perc': [0.8,0.7,0.4,np.nan]
    })
try:    
    invalid_df = transform(invalid_df)

except SchemaError as e:
    raise(e)
