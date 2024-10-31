from typing import Union
from fastapi import APIRouter, Depends, HTTPException, status
from db_manager import get_db
from sqlalchemy.orm import Session
from db_model import GangnamguPopulatationDbModel
from schema import GangnamguPopulation

app = APIRouter(prefix="/v1/logic", tags=["Logic"])

#라우팅 테스트 용으로 작성된 코드
#db_api.py와 동일

# 전체 데이터 조회
@app.get(str())
async def read(db: Session = Depends(get_db)):  #종속성 주입
    try:
        items = db.query(GangnamguPopulatationDbModel).all()
        
        if items is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
        
        result = [
            {
                "id": item.id,
                "sex_ratio": item.sex_ratio,
                "male_pupulation": item.male_population,
                "female_pupulation": item.female_population,
                "number_of_households": item.number_of_households,
                "administrative_agency": item.administrative_agency,
                "number_of_people_per_household": item.number_of_people_per_household
            } for item in items
        ]
        
        return {
            "status" : status.HTTP_200_OK,
            "message" : "Read all items successfully",
            "items" : result
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise 

# 특정 데이터 조회
@app.get("/{id}")
async def read(id: int, db: Session = Depends(get_db)):  #종속성 주입
    item = db.query(GangnamguPopulatationDbModel).filter(GangnamguPopulatationDbModel.id == id).first()
    
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
        
    result = {
        "id": item.id,
        "sex_ratio": item.sex_ratio,
        "male_pupulation": item.male_population,
        "female_pupulation": item.female_population,
        "number_of_households": item.number_of_households,
        "administrative_agency": item.administrative_agency,
        "number_of_people_per_household": item.number_of_people_per_household
    }
    
    return {
        "status" : status.HTTP_200_OK,
        "message" : "Read item successfully",
        "items" : result
    }

# 데이터 생성
@app.post(str())
async def create(parameter: GangnamguPopulation, db: Session = Depends(get_db)):
    item = GangnamguPopulatationDbModel(
        administrative_agency = parameter.administrative_agency,
        total_population = parameter.total_population,
        male_population = parameter.male_population,
        female_population = parameter.female_population,
        sex_ratio = parameter.sex_ratio,
        number_of_households = parameter.number_of_households,
        number_of_people_per_household = parameter.number_of_people_per_household
    )
    
    db.add(item)
    db.commit()
    
    return {
        "status" : status.HTTP_200_OK,
        "message" : "Create item successfully"
    }
    

# 데이터 업데이트
@app.put("/{id}")
async def update(id: int, parameter: GangnamguPopulation, db: Session = Depends(get_db)):
    item = db.query(GangnamguPopulatationDbModel).filter(GangnamguPopulatationDbModel.id == id).first()
    
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
    
    item.administrative_agency = parameter.administrative_agency
    item.total_population = parameter.total_population
    item.male_population = parameter.male_population
    item.female_population = parameter.female_population
    item.sex_ratio = parameter.sex_ratio
    item.number_of_households = parameter.number_of_households
    item.number_of_people_per_household = parameter.number_of_people_per_household
    
    db.commit()
    
    return {
        "status" : status.HTTP_200_OK,
        "message" : "Update item successfully"
    }

# 데이터 삭제
@app.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    item = db.query(GangnamguPopulatationDbModel).filter(GangnamguPopulatationDbModel.id == id).first()
    
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
    
    db.delete(item)
    db.commit()
    
    return {
        "status" : status.HTTP_200_OK,
        "message" : "Delete item successfully"
    }