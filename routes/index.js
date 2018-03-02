const express = require('express');
const router = express.Router();
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
// const AccessHistory = require("../models/access-history");
const mongoose = require('mongoose');
const Employee = require('../models/employee');

let User = require('../models/admin');

// Home Page - Dashboard
router.get('/', (req, res, next) => {
  Employee.find()
  // .sort({AccessHistory: -1})
  .limit()
  .select()
  // .populate('Employee')
  .exec()
  .then(docs => {
    console.log(docs);
      res.render('index', {
        title: 'Form Validation',
        success: false,
        errors:req.session.errors,
      });

    })
       
  .catch(err => {
      console.log(err);
      read.status(500).json({
          error:err
      })
  })
  
});

// Login Form
router.get('/login', (req, res, next) => {
  res.render('login');
});

// Logout
router.get('/logout', (req, res, next) => {
  req.logout();
  req.flash('success_msg', 'You are logged out');
  res.redirect('/login');
});

// Local Strategy
passport.use(new LocalStrategy((username, password, done) => {
  User.getUserByUsername(username, (err, user) => {
    if(err) throw err;
    if(!user){
      return done(null, false, {message: 'No user found'});
    }

    User.comparePassword(password, user.password, (err, isMatch) => {
      if(err) throw err;
      if(isMatch){
        return done(null, user);
      } else {
        return done(null, false, {message: 'Wrong Password'});
      }
    });
  });
}));

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.getUserById(id, (err, user) => {
    done(err, user);
  });
});
 
// Login Processing
router.post('/login', (req, res, next) => {
  passport.authenticate('local', {
    successRedirect:'/',
    failureRedirect:'/login',
    failureFlash: true
  })(req, res, next);
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

module.exports = router;