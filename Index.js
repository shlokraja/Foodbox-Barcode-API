var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.get('/PostBarcode',function(req,res) {
//io.on('connection', function(socket){
  //socket.on('data-matrix', function(msg){
    io.emit('data-matrix', req.query.barcode);	
    console.log(req.query.barcode);
    res.send("Done" + req.query);
});


http.listen(3000, function(){
  console.log('listening on *:3000');
}); 

io.on('connection', function(socket){
console.log("Socket");
});