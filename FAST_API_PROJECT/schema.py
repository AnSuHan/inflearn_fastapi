from pydantic import BaseModel

class GangnamguPopulation(BaseModel):
    administrative_agency : str
    total_population : int
    male_population : int
    female_population : int
    sex_ratio : float
    number_of_households : int
    number_of_people_per_household : float