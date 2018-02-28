const express = require('express');
const router = express.Router();
const LocalStrategy = require('passport-local').Strategy;
/*
const multer = require('multer');
const upload = multer({storage: './public/uploads'});
*/
let Employee = require('../models/employee');

router.get('/',ensureAuthenticated,(req,res,next)=>{
    res.render('registerEmployee');
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
//  router.post('/',upload.single('profilephote'),(req,res,next)=>
router.post('/',ensureAuthenticated,(req,res,next)=>{
     const fname=req.body.fname;
     const lname=req.body.lname;
     const gender=req.body.gender;
     const dob=req.body.birth;
     const city=req.body.city;
     const address=req.body.address;
     const code=req.body.zipcode;
     const mail=req.body.email;
     const phonenumber=req.body.phoneNumber;

//check img field
/*
if(req.file.profilephoto){
    //file info
    const profilephotoOriginalName  =req.files.profilephoto.originalname;
    const profilephotoName          =req.files.profilephoto.name;
    const profilephotoMime          =req.files.profilephoto.mimetype;
    const profilephotoPath          =req.files.profilephoto.path;
    const profilephotoExt           =req.files.profilephoto.extension;
    const profilephotoSize          =req.files.profilephoto.size;
}else{
    //if not img, set deffault
    const profilephotoName='noimg.png';
}
*/
//validation
req.checkBody('fname','First name field is required').notEmpty();
req.checkBody('lname','Last name field is required').notEmpty();
req.checkBody('gender','Gender field is required').notEmpty();
req.checkBody('dob','Date of birth field is required');
req.checkBody('city','City field is required').notEmpty();
req.checkBody('address','Address field is required').notEmpty();
req.checkBody('code','ZIP code field is required');
req.checkBody('mail','Email field is required');
req.checkBody('phonenumber','Phone number field is required');

let errors=req.validationErrors();

if (errors){
    res.render('registerEmployee', {
        errors: errors  
    });
}else{
    const newUser= new Employee({
        First_Name: fname,
        Last_Name:lname,
        Gender:gender,
        Date_of_birth:dob,
        City:city,
        Address:address,
        Code:code,
        email:mail,
        phonenumber:phonenumber
        //profilephoto:profilephotoName
    });

    //create user
    Employee.createUser(newUser, (err, user) => {
        if(err) throw err;
        req.flash('success_msg', 'Employee registered');
        res.redirect('/registerEmployee');
        console.log(newUser);
      });
    }
});

//Edit
router.put('/:id',(req,res)=>{
    Employee.findOne({
        _id: req.params.id
        })
    .then(employee=>{
        
        //edit
        employee.First_Name=req.body.fname;
        employee.Last_Name=req.body.lname;
        employee.Gender=req.body.gender;
        employee.Date_of_birth=req.body.birth;
        employee.City=req.body.city;
        employee.Address=req.body.address;
        employee.Code=req.body.zipcode;
        employee.email=req.body.email;
        employee.phonenumber=req.body.phoneNumber;

        employee.save()
        .then(employee=>{
            req.flash('success_msg', 'Employee upgraded');
            res.redirect('/');
            console.log(employee);
            
        });
        });
    });

//Delete
router.delete('/:id',ensureAuthenticated,(req,res)=>{
    Employee.remove({_id:req.params.id})
    .then(() =>{
        res.redirect('/show');
    });
});


module.exports=router;