import pymongo
from pymongo import *
Connection = MongoClient('mongodb://localhost:27017/')
from bson.code import Code
from bson.son import SON
db = Connection.test

#Creating Map function for data collection*/
map_function = Code("""
  function(){
  if(this.year == null) return;

  var key = {
       cancer_site:this.cancer_site };
  emit(key, {count:NumberInt(1)});
  }
""")
