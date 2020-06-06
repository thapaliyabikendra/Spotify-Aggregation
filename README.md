# Spotify-Aggregation

Simple restapi to get most popular songs according to year, popular songs by artist and popular artist with genre.

### Get popular song by year
```bash
GET songs/year/{year}
```
### Get popular song by artist
```bash
GET songs/artist/{artist}
```
### Get popular artist by genre
```bash
GET artists/{genre}
```
### Get popular genres
```bash
GET genres
```
### Get popular song by year per page
```bash
GET songs/year/{year}?page={pageno}&size={size}
```
### Get popular song by artist per page
```bash
GET songs/artist/{artist}?page={pageno}&size={size}
```
### Get popular artist by genre per page
```bash
GET artists/{genre}?page={pageno}&size={size}
```
### Get popular genres per page
```bash
GET genres?page={pageno}&size={size}
```