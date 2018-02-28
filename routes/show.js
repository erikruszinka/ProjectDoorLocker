const express = require('express');
const router = express.Router();
const mongoose=require('mongoose');
const Employee= mongoose.model('Employee');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

//show all
router.get('/',ensureAuthenticated,(req,res,next)=>{
    Employee.find()
    .then(employees => {
        res.render('show', {
            employees:employees
        });
    });    
});
//Show one
router.get('/:id',ensureAuthenticated,(req,res)=>{
    Employee.findOne({
        _id: req.params.id
        })
    .then(employee=>{
        res.render('info',{
            employee:employee
        });
    });
});

//Edit one
router.get('/edit/:id',(req,res)=>{
    Employee.findOne({
        _id: req.params.id
        })
    .then(employee=>{
        res.render('edit',{
            employee:employee
        });
    });
});
// Access Control
function ensureAuthenticated(req, res, next){
    if(req.isAuthenticated()){
      return next();
    } else {
      req.flash('error_msg', 'You are not authorized to view that page');
      res.redirect('/login');
    }
  }

  module.exports=router;