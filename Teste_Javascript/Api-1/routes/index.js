var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.send({ title: 'Express', url: 'http://localhost:8080' });
});

module.exports = router;
