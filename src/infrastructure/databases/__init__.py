from infrastructure.databases.mssql import init_mssql, close_session
from infrastructure.models import question_model, lesson_plan_model, course_register_model, role_model, todo_model, user_model, course_model, consultant_model, appointment_model, program_model, feedback_model,survey_model

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base, session