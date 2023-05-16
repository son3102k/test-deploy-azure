from fastapi import APIRouter, Depends, Body
from typing import Annotated
from service import classes as service_class
from sqlalchemy.orm import Session
from config.db import get_db
from schema import classes as schema_class
from schema import user as schema_user
from util.jwt import JWTBearer, JWTBearerForTeacher, JWTBearerForAdmin
from schema.request import RequestSchema, ResponseSchema, TokenResponse

API_Class_Teacher = APIRouter(prefix="/class/teacher", tags=["Class_Teacher"])

@API_Class_Teacher.get('/allclassesofteacher', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def get_all_classes_of_teacher(teacher_id: int, db: Session = Depends(get_db)):
    try:
        result = service_class.get_all_classes_of_teacher(teacher_id, db)
        return ResponseSchema[list[schema_class.ClassInfo]](
            code="200", status="Ok", message="thành công", result=result
        ).dict(exclude_none=True)
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", message="Lỗi hệ thống"
        ).dict(exclude_none=True)
    

@API_Class_Teacher.get('/allclassesteacherjoined', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def get_all_classes_teacher_joined(teacher_id: int, db: Session = Depends(get_db)):
    try:
        result = service_class.get_all_classes_user_joined(teacher_id, db)
        return ResponseSchema[list[schema_class.ClassInfo]](
            code="200", status="Ok", message="thành công", result=result
        ).dict(exclude_none=True)
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", message="Lỗi hệ thống"
        ).dict(exclude_none=True)
    
@API_Class_Teacher.post('/createclass', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def create_class(class_create: schema_class.ClassCreate, db: Session = Depends(get_db)):
    try:
        result = service_class.create_class(class_create, db)
        if result:
            return ResponseSchema(
                code="200", status="Ok", 
                message="Tạo mới lớp thành công"
            ).dict(exclude_none=True)
        
        return ResponseSchema(
            code="400", status="Bad Request", 
            message="Lỗi service"
        ).dict(exclude_none=True)

    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", 
            message="Lỗi hệ thống"
        ).dict(exclude_none=True)
    

@API_Class_Teacher.get('/allstudentsofclass', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def get_all_students_of_class(class_id: int, db: Session = Depends(get_db)):
    try:
        result = service_class.get_all_students_of_class(class_id, db)
        return ResponseSchema[list[schema_user.UserClassStatus]](
            code="200", status="Ok", message="thành công", result=result
        ).dict(exclude_none=True)
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", message="Lỗi hệ thống"
        ).dict(exclude_none=True)
    

@API_Class_Teacher.get('/allteachersofclass', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def get_all_teachers_of_class(class_id: int, db: Session = Depends(get_db)):
    try:
        result = service_class.get_all_teachers_of_class(class_id, db)
        return ResponseSchema[list[schema_user.UserInfo]](
            code="200", status="Ok", message="thành công", result=result
        ).dict(exclude_none=True)
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", message="Lỗi hệ thống"
        ).dict(exclude_none=True)
    
@API_Class_Teacher.post('/teacheradduser', response_model=ResponseSchema, dependencies=[Depends(JWTBearerForTeacher())])
async def teacher_add_user(user_id_list: Annotated[list[int], Body()], \
                            teacher_id: Annotated[int, Body()], class_id: Annotated[int, Body()], \
                            db: Session = Depends(get_db)):
    try:
        result = service_class.teacher_add_user(user_id_list, teacher_id, class_id, db)
        code = result[0]
        message = result[1]
        if code == "200":
            return ResponseSchema(
                code=code, status="Ok", message=message
            ).dict(exclude_none=True)
        return ResponseSchema(
            code = code, status="Bad request", message = message
        ).dict(exclude_none=True)
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code="500", status="Internal Server Error", message="Lỗi hệ thống"
        ).dict(exclude_none=True)