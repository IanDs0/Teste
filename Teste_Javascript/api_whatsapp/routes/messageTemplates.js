const express = require("express");
const router = express.Router();

const {
  createMessageTemplate,
} = require("../controller/messageTemplates");

router.post("/messageTemplate", createMessageTemplate);

module.exports = router;
