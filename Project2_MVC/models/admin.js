const mongoose = require('mongoose');
const Schema=mongoose.Schema;

mongoose.Promise = global.Promise;
/*
mongoose.connect("mongodb://"+process.env.MONGO_ATLAS_ADM+":"+
process.env.MONGO_ATLAS_PW+"@ds229388.mlab.com:29388/recog");
*/

mongoose.connect('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog');

const bcrypt = require('bcryptjs');
 

// Admin Schema
const AdminSchema = new Schema({
  name: {
    type: String
  },
  username: {
    type: String
  },
  email: {
    type: String
  },
  password: {
    type: String
  }
});

const admin = module.exports = mongoose.model('admin', AdminSchema);

module.exports.registerUser = function(newUser, callback){
  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(newUser.password, salt, (err, hash) => {
      if(err){
        console.log(err);
      }
      newUser.password = hash;
      newUser.save(callback);
    });
  });
}

module.exports.getUserByUsername = function(username, callback){
  const query = {username: username}
  admin.findOne(query, callback);
}

module.exports.getUserById = function(id, callback){
  admin.findById(id, callback);
}

module.exports.comparePassword = function(candidatePassword, hash, callback){
  bcrypt.compare(candidatePassword, hash, (err, isMatch) => {
    if(err) throw err;
    callback(null, isMatch);
  });
}
