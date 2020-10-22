from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/consumer_db?retryWrites=true&w=majority')
	db = con.consumer_db
	col = db.email_info2


def save_email_info(email_info):
	global col
	connect_db()
	col.insert(email_info)
	return "Saved Successfully"

def get_allMail():
	global col
	connect_db()
	mails_fromDB = col.find({})
	return mails_fromDB


