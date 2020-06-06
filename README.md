# Spotify-Aggregation

Simple restapi to get most popular songs according to year, popular songs by artist and popular artist with genre.

### Get popular song by year
```bash
GET songs/{year}
```
### Get popular song by artist
```bash
GET songs/{artist}
```
### Get popular artist by genre
```bash
GET songartists/{genre}
```
### Get popular song by year per page
```bash
GET songs/{year}?page={pageno}&size={size}
```
### Get popular song by artist per page
```bash
GET songs/{artist}?page={pageno}&size={size}
```
### Get popular artist by genre per page
```bash
GET songartists/{genre}?page={pageno}&size={size}
```
