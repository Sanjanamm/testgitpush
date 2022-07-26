import pymongo
client = pymongo.MongoClient("mongodb+srv://Sanjana:mongodb123@cluster0.8a4ne.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"sanjana",
    "email": "sonusanjana2016@gmail.com",
    "surname":"kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)