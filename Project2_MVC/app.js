const express= require('express');
const mongo = require('mongodb'); 
const mongoose= require('mongoose');
const path = require('path'); 
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser'); 
const exphbs = require('express-handlebars'); 
const expressValidator = require('express-validator'); 
const flash = require('connect-flash'); 
const session = require('express-session'); 
const passport = require('passport'); 
const LocalStrategy = require('passport-local').strategy; 

/*
const multer=require('multer');
const upload = multer({storage: './public/uploads'});
*/

//routes
const index = require('./routes/index');
const admin = require('./routes/admin');
const employee = require('./routes/employee');


//Application init
const app=express();

//view engine
app.engine('handlebars',exphbs({defaultLayout: 'main'}));
app.set('view engine','handlebars');

//app.use(upload.single('profilephoto'))

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

//Ex session
app.use(session({
    secret:'secret_phrase',
    saveUninitialized:false,
    resave:false
}));

// Init passport
app.use(passport.initialize());
app.use(passport.session());

// Ex messages
app.use(flash());
app.use((req, res, next) => {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  res.locals.user = req.user || null;
  next();
});

//Ex validator
app.use(expressValidator({
    errorFormatter: (param, msg, value) => {
        let namespace = param.split('.')
        , root    = namespace.shift()
        , formParam = root;
  
      while(namespace.length) {
        formParam += '[' + namespace.shift() + ']';
      }
      return {
        param : formParam,
        msg   : msg,
        value : value
      };
    }
}));

app.use('/', index);
app.use('/registerAdmin', admin);
app.use('/registerEmployee', employee);



//Start Server
app.set('port',(process.env.PORT || 3000));

app.listen(app.get('port'),()=>{
    console.log('Server started on port '+app.get('port'));
});