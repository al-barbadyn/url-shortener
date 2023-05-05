# Url Shortener

## API to create and delete short urls
### Create (POST /api/v1/api/v1/url-shortener/ with url in body)
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/url-shortener/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "url": "https://translate.google.com"
}'

Response: 
{
    "short_url": "http://127.0.0.1:8000/BgYGgW"
}
```

### Delete (DELETE /api/v1/api/v1/url-shortener/ with short_url in body)
```
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/url-shortener/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "short_url": "http://127.0.0.1:8000/BgYGgW"
}'

Response:
204 or 404 if short url does not exist
```

### Redirect
```
Go to http://127.0.0.1:8000/BgYGgW to be redirected to your link (https://translate.google.com)
```
