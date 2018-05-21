import pymongo
from pymongo import *
Connection = MongoClient('mongodb://localhost:27017/')
from bson.code import Code
from bson.son import SON
import pprint, csv
db = Connection.test

#Reduce function*/
reduce_function = Code("""
  function (key, values) {

    var sum = 0;
    values.forEach(function(val)
    {
        sum += val['count'];
    });
    return {count:NumberInt(sum)};
  }
""")
