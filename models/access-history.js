const mongoose=require('mongoose');
const Schema=mongoose.Schema;
mongoose.Promise = global.Promise;

mongoose.connect('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog');

const accessHistorySchema = new Schema({
    Access_time: {
        type:Date,
        default: Date.now
    },

    CardId: {
        type: String,ref: 'Employee'
    },

    Success: {
        type:Boolean
    }

});

module.exports = mongoose.model('AccesHistory',accessHistorySchema);