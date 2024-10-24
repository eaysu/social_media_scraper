from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from factories.youtube_factory import YouTubeScraperFactory
from factories.twitter_factory import TwitterScraperFactory
from factories.instagram_factory import InstagramScraperFactory
from factories.reddit_factory import RedditScraperFactory
from factories.sikayetvar_factory import SikayetVarScraperFactory

app = FastAPI()

# Request body models
class YouTubeRequest(BaseModel):
    search_query: str

class InstagramRequest(BaseModel):
    search_query: str

class TwitterRequest(BaseModel):
    search_query: str

class RedditRequest(BaseModel):
    search_query: str

class SikayetVarRequest(BaseModel):
    search_query: str    

# Routes
@app.post('/scrape/youtube')
async def scrape_youtube(request: YouTubeRequest):
    search_query = request.search_query
    if not search_query:
        raise HTTPException(status_code=400, detail="Missing YouTube search query")

    factory = YouTubeScraperFactory()
    scraper = factory.create_scraper()
    result = scraper.scrape(search_query)
    
    # Ensure the result is JSON serializable (e.g., convert to dict if necessary)
    return {"result": result}

@app.post('/scrape/instagram')
async def scrape_instagram(request: InstagramRequest):
    search_query = request.search_query
    if not search_query:
        raise HTTPException(status_code=400, detail="Missing Instagram search query")

    factory = InstagramScraperFactory()
    scraper = factory.create_scraper()
    result = scraper.scrape(search_query)
    
    # Ensure the result is JSON serializable
    return {"message": result}

@app.post('/scrape/twitter')
async def scrape_twitter(request: TwitterRequest):
    search_query = request.search_query
    if not search_query:
        raise HTTPException(status_code=400, detail="Missing Twitter search query")

    factory = TwitterScraperFactory()
    scraper = factory.create_scraper()
    result = await scraper.scrape(search_query)  # Await the asynchronous function
    
    # Ensure the result is JSON serializable
    return {"message": result}

@app.post('/scrape/reddit')
async def scrape_reddit(request: RedditRequest):
    search_query = request.search_query
    if not search_query:
        raise HTTPException(status_code=400, detail="Missing Reddit search query")

    factory = RedditScraperFactory()
    scraper = factory.create_scraper()
    result = scraper.scrape(search_query)
    
    # Ensure the result is JSON serializable
    return {"message": result}

@app.post('/scrape/sikayetvar')
async def scrape_sikayetvar(request: SikayetVarRequest):
    search_query = request.search_query
    if not search_query:
        raise HTTPException(status_code=400, detail="Missing Sikayet Var search query")

    factory = SikayetVarScraperFactory()
    scraper = factory.create_scraper()
    result = scraper.scrape(search_query)
    
    # Ensure the result is JSON serializable
    return {"message": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
