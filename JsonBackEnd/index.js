/**
 * Created by David on 11/01/2016.
 *
 * */

var express = require('express');
var bodyParser = require("body-parser");
var fs = require("fs");


var app = express();
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

//Dealing with Get requests for the Json
app.get("/json", function(req, res) {
    try {
        //Sending Json to the client
        jsonTxt = JSON.parse(fs.readFileSync(__dirname + "/db.json"));
        //Logging the Connection
        console.log("Connection");
        res.send(jsonTxt);

    }
    catch (e) {
        console.error('error whilst getting: '+ e.msg);
        res.writeHead(400);
        res.end('error getting json');
    }
});

//Dealing with post requests to update the json
app.post("/json",function(req,res){
    try {
        //Getting the json from the message that has been sent
        req.body.payload = JSON.parse(req.body.payload);
    }
    catch(e){
    }

    if(req.body.payload != undefined && req.body.payload.edit != undefined) {

        if(req.body.payload.edit == 'override' && req.body.payload.jsonTxt != undefined) {

            jsonObj = req.body.payload.jsonTxt;
            jsonObj = JSON.stringify(jsonObj, null, 4);

            //updating db.json
            fs.writeFile("db.json", jsonObj, function (err, data) {
                if (err) {
                    return console.error(err);
                }
                console.log("Successful write to file");
            });
        } else{
            //Logging an error message
            console.log("Something was wrong with the Json");

        }
    }
    res.end("yes");
});

//Sending a front wall to the user if they acess the page from a browser
app.get('/', function(req, res) {
    res.sendFile(__dirname + "/index.html");
});


 app.listen(8080,function(){
    console.log("Started on PORT 8080");
});
