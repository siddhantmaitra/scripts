// Configuration - edit these values as needed
//const API_URL = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions';
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
       const elements = data.data?.Catalog?.searchStore?.elements || data.Catalog?.searchStore?.elements || [];
       
       const currentlyFree = elements
           .filter(game => 
               game.price?.totalPrice?.discountPrice === 0 &&
               game.promotions?.promotionalOffers?.length > 0 &&
               game.promotions.promotionalOffers[0]?.promotionalOffers?.[0]?.discountSetting?.discountPercentage === 0
           )
           .map(game => ({
               title: game.title,
               description: game.description || '',
               originalPrice: game.price.totalPrice.fmtPrice.originalPrice,
               startDate: game.promotions.promotionalOffers[0].promotionalOffers[0].startDate,
               endDate: game.promotions.promotionalOffers[0].promotionalOffers[0].endDate,
               image: game.keyImages?.find(img => img.type === 'OfferImageWide')?.url || null,
               url: game.offerMappings[0]?.pageSlug ? `https://store.epicgames.com/en-US/p/${game.offerMappings[0].pageSlug}` : null,
           }));

       const upcomingFree = elements
           .filter(game =>
               game.promotions?.upcomingPromotionalOffers?.length > 0 &&
               game.promotions.upcomingPromotionalOffers[0]?.promotionalOffers?.[0]?.discountSetting?.discountPercentage === 0
           )
           .map(game => ({
               title: game.title,
               description: game.description || '',
               originalPrice: game.price.totalPrice.fmtPrice.originalPrice,
               startDate: game.promotions.upcomingPromotionalOffers[0].promotionalOffers[0].startDate,
               endDate: game.promotions.upcomingPromotionalOffers[0].promotionalOffers[0].endDate,
               image: game.keyImages?.find(img => img.type === 'OfferImageWide')?.url || null,            
               url: game.offerMappings[0]?.pageSlug ? `https://store.epicgames.com/en-US/p/${game.offerMappings[0].pageSlug}` : null,
           }));

       return { currentlyFree, upcomingFree };
       
   } catch (error) {
       throw new Error(`Failed to fetch: ${error.message}`);
   }
}

getFreeGames()
   .then(result => {
       console.log(JSON.stringify(result, null, 2));
   })
   .catch(error => console.error('Error:', error.message));
