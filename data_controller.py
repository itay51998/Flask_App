from flask import Flask , render_template , request 
from flask_pymongo import PyMongo 
from pymongo import MongoClient
import time

def password_hasher(password):
	password_hashed = 123
	return password_hashed

def register_controller(database , register_data):
	user = database.db.users
	user.insert({'email' : register_data['email'] , 'password' : register_data['password'] , 'user_name' : register_data['name'] , 
		'about' : register_data['about'] , 'gems' : register_data['gems'] , 'score' : register_data['score']})
	return ''

def register_check(register_data):
	if register_data['name'] == "Omer":
		return False	
	else:
		return True


