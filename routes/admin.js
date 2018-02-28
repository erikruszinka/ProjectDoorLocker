const express = require('express');
const router = express.Router();
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

let Admin = require('../models/admin');

// RegisterAdmin Form
router.get('/',ensureAuthenticated, (req, res, next) => {
    res.render('registerAdmin');
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
// Process Register
router.post('/', (req, res, next) => {
    const name = req.body.name;
    const username = req.body.username;
    const email = req.body.email;
    const password = req.body.password;
    const password2 = req.body.password2;
//Check validity
    req.checkBody('name', 'Name field is required').notEmpty();
    req.checkBody('email', 'Email field is required').notEmpty();
    req.checkBody('email', 'Email must be a valid email address').isEmail();
    req.checkBody('username', 'Username field is required').notEmpty();
    req.checkBody('password', 'Password field is required').notEmpty().isLength({min:4});
    req.checkBody('password2', 'Passwords do not match').equals(req.body.password);
//store errorss
    let errors = req.validationErrors();
  
    if(errors){
      res.render('registerAdmin', {
        errors: errors
      });
    } else {
      const newUser = new Admin({
        name: name,
        username: username,
        email: email,
        password: password
    });
  
    Admin.registerUser(newUser, (err, user) => {
        if(err) throw err;
        req.flash('success_msg', 'You are registered and can log in');
        res.redirect('/registerAdmin');
      });
    }
  });
  
module.exports = router;