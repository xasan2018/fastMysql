import shutil
from fastapi import FastAPI,UploadFile,File
import cv2
import mysql.connector


app = FastAPI()

@app.post('/')
async def root(file: UploadFile = File(...),q: str = None):
    path = file.filename
    img = cv2.imread(path)
    q=img.shape

    mydb = mysql.connector.connect(
        host="localhost",
        user="olotilmz_test",
        password="+998973004959rammi",
        database="olotilmz_test"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO test_javoblari (rasm, uzunligi,boyi,rangi) VALUES (%s, %s, %s, %s)"
    rasm=file.filename
  
    uzunligi=q[0]
    boyi=q[1]
    rangi=q[2]
    val = (rasm,uzunligi,boyi,rangi)
    mycursor.execute(sql, val)

    mydb.commit()

    return {"file_name": file.filename,"q": q}
