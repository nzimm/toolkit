var sqlite = require('sqlite3').verbose();
var db = new sqlite3.Database('/database.db');

$(document).ready(function(){
    $("#serveQuery").click(function(){
        $("#results").text($("#query").val());
        //db.each(`SELECT ${$("#query").val()} FROM users`, function(err, row) {
        //    console.log(row.$("#query").val());
        //});
    });
});

//$(document).ready(function(){
//    $("#serveQuery").click(function(){
//        $("#results").text(db.each(`SELECT ${$("#query").val()} FROM users`, function(err, row) {
//            console.log(row.$("#query").val())
//            });
//        });
//    });
//);
