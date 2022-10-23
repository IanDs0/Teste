const padrão = [
    {
        "recipient_type":"",
        "to": "",
        "type": "image",
        "image": {
            "type": "button",
            "header": { 
                "type": "text" | "image" ,
                "text": "your text",
                
                "image": {
                    "id": "your-media-id"
                },
                
                "image": {
                    "link": "http(s)://the-url",
                    "provider": {
                    "name": "provider-name"
                    }
                }
            }, 
            "body": {
                "text": "your-text-body-content"
            },
            "footer": { //OPCIONAL
                "text": "your-text-footer-content"
            },
            
        }
    }

]

/*
"image": {
        "link": "http(s)://the-url",
        "provider": {
            "name" : "provider-name"
        },
        "caption": "your-image-caption"
    }
    // "image": {
    //     "id": "your-media-id",
    //     "caption": "your-image-caption"
    // } 
*/