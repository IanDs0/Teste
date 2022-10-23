const formidable = require("formidable");
const request = require("request");
const fs = require("fs");

const axios = require('axios');
//webhook => "https://glitch.com/edit/#!/probable-ember-science"

exports.createMessageTemplate = async function (req, res){
  const { img, preco, produto, link, telefone } = req.body;
  if (!img || !preco || !produto || !link || !telefone) {
    return res.status(400).json({
      error: "Required Fields: name, language, category and components",
    });
  }


  let teste = await axios({
    method: 'post',
    url: `https://graph.facebook.com/${process.env.VERSION}/${process.env.PHONE_NUMBER_ID}/messages`,
    headers: {
    'Authorization': `Bearer ${process.env.ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
    },
    data:{ 
      "messaging_product": "whatsapp",
      "recipient_type": "individual",
      "to": telefone,

      "type": "template",
      "template": {
        "name": "oferta_1",
        "language": {
            "code": "pt_BR",
        },
        "components": [
          {
              "type": "header",
              "parameters": [{
                  "type": "image",
                  "image": {
                      "link": img
                  }
              }]
          },
          {
              "type": "body",
              "parameters": [
                  {
                      "type": "text",
                      "text": preco
                  },
                  {
                      "type": "text",
                      "text": produto
                  },
                  {
                    "type": "text",
                    "text": link
                  }
              ] 
          },
        ]
      }




    },
  })
  .catch(function (error) {
    if (error.response) {
      console.log(error.response.data);
      console.log(error.response.status);
      //console.log(error.response.headers);
    } else if (error.request) {
      console.log(error.request);
    } else {
      console.log('Error', error.message);
    }
    console.log(error.config);
    return res.status(error.response.status).json({
      response: error.response.status,
    });
  })
  .then(function(response) {
    return res.status(response.status).json({
      response: response.status,
    });
 });
};
