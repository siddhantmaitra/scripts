const data  = {
  "currentlyFree": [
    {
      "title": "112 Operator",
      "description": "Manage emergency services in any city in the world! Take calls and dispatch rescue forces. Handle difficult situations, now depending on the weather, and traffic. Help the citizens through cataclysms and natural disasters, becoming a better emergency number operator every day!",
      "originalPrice": "₹899.00",
      "startDate": "2025-08-07T15:00:00.000Z",
      "endDate": "2025-08-14T15:00:00.000Z",
      "image": "https://cdn1.epicgames.com/spt-assets/6036e5ea111a448ea1b41d5ab3800d99/112-operator-1smmi.jpg",
      "url": "https://store.epicgames.com/en-US/p/112-operator-f34b0b"
    },
    {
      "title": "Road Redemption",
      "description": "Road Redemption lets you lead a biker gang on an epic journey across the country in this driving combat road rage adventure.",
      "originalPrice": "₹719.00",
      "startDate": "2025-08-07T15:00:00.000Z",
      "endDate": "2025-08-14T15:00:00.000Z",
      "image": "https://cdn1.epicgames.com/spt-assets/ee0cf0e1ab6a4e1c83e5de0681fea012/road-redemption-1upeb.png",
      "url": "https://store.epicgames.com/en-US/p/road-redemption-ce16fb"
    }
  ],
  "upcomingFree": [
    {
      "title": "Totally Reliable Delivery Service Standard Edition",
      "description": "Buckle up your back brace and fire up the delivery truck, it's time to deliver! Join up to three friends and haphazardly get the job done in an interactive sandbox world. Delivery attempted, that's a Totally Reliable Delivery Service guarantee!",
      "originalPrice": "₹446.00",
      "startDate": "2025-08-14T15:00:00.000Z",
      "endDate": "2025-08-21T15:00:00.000Z",
      "image": "https://cdn1.epicgames.com/52b90f9a982a404781b189f6a7903226/offer/EGS_TotallyReliableDeliveryService_WereFiveGames_S1-2560x1440-47e6e9562d62705a75ea7b7096d0b8dc.jpg",
      "url": "https://store.epicgames.com/en-US/p/totally-reliable-delivery-service"
    },
    {
      "title": "Hidden Folks",
      "description": "Search for hidden folks in hand-drawn, interactive, miniature landscapes. Unfurl tent flaps, cut through bushes, slam doors, and poke some crocodiles! Rooooaaaarrrr!!!!!",
      "originalPrice": "₹539.00",
      "startDate": "2025-08-14T15:00:00.000Z",
      "endDate": "2025-08-21T15:00:00.000Z",
      "image": "https://cdn1.epicgames.com/spt-assets/7bfd56b0586348dcb139945d9e59f988/hidden-folks-1b7hh.png",
      "url": "https://store.epicgames.com/en-US/p/hidden-folks-239d16"
    }
  ]
}

const API_URL = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=IN&allowCountries=IN';
const USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
const CONTENT_TYPE = 'application/json';
const TIMEOUT = 10000;

async function getFreeGames() {
   try {
       const response = await fetch(API_URL, {
           method: 'GET',
           headers: {
               'User-Agent': USER_AGENT,
               'Content-Type': CONTENT_TYPE,
               'Accept': 'application/json'
           },
           signal: AbortSignal.timeout(TIMEOUT)
       });
       
       const data = await response.json();
       return data;
    }catch(err){
      return "error during fetch";
    }
}

function deepIterator (target) {
  if (typeof target === 'object') {
    for (const key in target) {
      deepIterator(target[key]);
    }
  } else {
    console.log(target);
  }
}



const iterate = (obj) => {
  const stack = [obj];
  while (stack?.length > 0) {
    const currentObj = stack.pop();
    Object.keys(currentObj).forEach(key => {
      console.log(`key: ${key}, value: ${currentObj[key]}`);
      if (typeof currentObj[key] === 'object' && currentObj[key] !== null) {
        stack.push(currentObj[key]);
      }
    });
  }
};

//const data2 = getFreeGames().then(result =>deepIterator(result)).catch(error => console.log(error))
// iterate(data);
// deepIterator(data);

const data2 = await getFreeGames();

// console.log(data2)c
deepIterator(data2);
