import pymongo

client = pymongo.MongoClient("mongodb+srv://Ramakrishna978:Ramana978@ramakrishna.ggxbzl6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"ramakrishna",
    "email":"rk@978@gamil.com",
    "surname":"H"
}

db1 = client['mangotest']
coll = db1['test']
coll.insert_one(d)
