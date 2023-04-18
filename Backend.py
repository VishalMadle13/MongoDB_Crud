from dotenv import load_dotenv , find_dotenv
import os
import pprint 

import pymongo
load_dotenv(find_dotenv())

username = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PWD") 

# connection_string = f"mongodb+srv://{username}:{password}@{cluster-name}.{-}.mongodb.net/?retryWrites=true&w=majority"
connection_string = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = pymongo.MongoClient(connection_string)

dbs = client.list_database_names()
college_db = client.College
college_collections = college_db.list_collection_names() 
student_collection = college_db.Students 
faculty_collection = college_db.Faculties
subject_collection = college_db.Subjects

printer = pprint.PrettyPrinter()
class Student_Crud:
    def get_all_student():
        list = []
        students = student_collection.find()
        for student in students:
            list.append(student)
        return list
    
    def get_student_by_key_value(key,value):
        student = student_collection.find_one({f"{key}" : f"{value}"})
        return student
    
    def post_student_add_one(query):
        try:
            student_collection.insert_one(query)
            return {"massage" : "successfully added student"}
        except Exception as e :
            return {"massage": e}

    def post_student_add_many(list):
        try:
            PrnList  = list[0]
            NameList = list[1]
            BranchList = list[2]

            student_docs = []
            for prn,name,branch in zip(PrnList,NameList,BranchList):
                doc = {"PRN" : prn,"name":name, "branch":branch}
                student_docs.append(doc)
            student_collection.insert_many(student_docs)
            return {"message":"successfully added multiple data"}
        except Exception as e :
            return {"Error" : e}
    
    def put_student_update_one_doccument(query,new_value):             
        try:                                                        
            new_value = {"$set":new_value}
            student_collection.update_one(query,new_value)
            return {"massage" : "successfully updated student data"}
        except Exception as e :
            return {"Error" : e}
        
    def put_student_update_many_doccuments(query,new_val):
        try:
            new_val = {"$set" : new_val}
            student_collection.update_many(query,new_val)
            return {"massage" : "successfully updated students data"}
        except Exception as e :
            return {"Error" : e}
    
    def delete_student_one(query):
        try: 
            student_collection.delete_one(query)
            return {"massage" : "successfully deleted student data"}
        except Exception as e :
            return {"Error" : e}
    
    def delete_students_many(query):
        try: 
            student_collection.delete_many(query)
            return {"massage" : "successfully deleted multiple student data"}
        except Exception as e :
            return {"Error" : e}
        



#**************************************************************************************************************************************************

#__________________________________________________POST:ADD ONE_______________________________________________

# query ={"PRN":"2020BTECS00092","name":"vishal","branch":"Computer Science and Engineering"}
# msg = Student_Crud.post_student_add_one(query)
# print(msg)


#__________________________________________________POST:ADD MANY______________________________________________

# lst = [
#     ["2020BTECS00093","2020BTECS00094","2020BTECS00095"],
#     ["akash","shivam","sai"],
#     ["Computer Science and Engineering","Computer Science and Engineering","Computer Science and Engineering"], 
# ]

# msg = Student_Crud.post_student_add_many(lst)
# print(msg)



#_________________________________________________PUT : UPDATE ONE_____________________________________________

# qry = {"PRN":"2020BTECS00092"}
# nwval = {"name":"aman"}
# msg = Student_Crud.put_student_update_one(qry,nwval)
# print(msg)


#______________________________________________PUT : UPDATE MANY________________________________________________

# # Update multiple documents
# query = { "name": "sudesh" }
# new_values = { "Branch": "Electrical" } 
# result = Student_Crud.put_student_update_many_doccuments(query,new_values)
# print(result)


#______________________________________________DELETE_ONE_________________________________________________________

# query = { "name": "sudesh" }
# result = Student_Crud.delete_student_one(query)
# print(result)

#______________________________________________DELETE_MANY_________________________________________________________

# query = { "name": "sudesh" }
# result = Student_Crud.delete_students_many(query)
# print(result)


#**************************************************************************************************************************************************
