from flask import Flask, render_template, request, jsonify
from database.db import connect2SQL, add_user, con_user
from controllers.admin_S3 import * 



def func_home_page():
    return render_template("home.html")


def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")


def func_register_user():
    message = "Id already in use"
    data_user = request.form
    id = data_user["id"]
    last_name = data_user["last_name"]
    first_name = data_user["first_name"]
    birthday = data_user["birthday"]
    confirm = add_user(id,first_name,last_name,birthday)
    if confirm:
        get_files()
        data_photo = request.files
        photo = data_photo["photo"]
        photo_path, photo_name = save_photo(photo, id)
        upload_photo(photo_path, photo_name)
        message = "User added"

    return message

def func_consult_user():
    result_data = con_user(request.get_json())
    obj_data = {
        'first_name':result_data[0][1],
        'last_name':result_data[0][2],
        'birthday':result_data[0][3],
    }
    return jsonify(obj_data)