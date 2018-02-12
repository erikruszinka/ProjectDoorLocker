const mongoose = require('mongoose');
mongoose.Promise = global.Promise;
/*
mongoose.connect("mongodb://"+process.env.MONGO_ATLAS_ADM+":"+
process.env.MONGO_ATLAS_PW+"@ds229388.mlab.com:29388/recog");
*/

mongoose.connect('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog');

const bcrypt = require('bcryptjs');


// User Schema
const UserSchema = mongoose.Schema({
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

const User = module.exports = mongoose.model('User', UserSchema);

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
  User.findOne(query, callback);
}

module.exports.getUserById = function(id, callback){
  User.findById(id, callback);
}

module.exports.comparePassword = function(candidatePassword, hash, callback){
  bcrypt.compare(candidatePassword, hash, (err, isMatch) => {
    if(err) throw err;
    callback(null, isMatch);
  });
}
