const mongoose=require('mongoose');
const Schema=mongoose.Schema;

mongoose.connect('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog');

//Employee schema
const EmployeeSchema=mongoose.Schema({
    First_Name: {
        type: String
    },
    Last_Name:{
        type:String
    },
    Gender:{
        type:String
    },
    Date_of_birth:{
        type:Date
    },
    City:{
        type:String
    },
    Address:{
        type:String
    },
    Code:{
        type:String
    },
    email:{
        type:String
    },
    number:{
        type:Number
    },
    profilephoto:{
        type:String
    }    
});

const Employee= module.exports= mongoose.model('Employee', EmployeeSchema);

module.exports.createUser= function(newUser, callback){
    newUser.save(callback);
}