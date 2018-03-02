const mongoose=require('mongoose');
const Schema=mongoose.Schema;
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog');

//Employee schema
const EmployeeSchema=new Schema({
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
        type:String
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
    phonenumber:{
        type:String
    },
    profilephoto:{
        type:String        
    },
    cardId: {
        type: String
    },

    Logs: {
        type:[String]
    }
      
});

const Employee= module.exports= mongoose.model('Employee', EmployeeSchema);

module.exports.createUser= function(newUser, callback){
    newUser.save(callback);
}