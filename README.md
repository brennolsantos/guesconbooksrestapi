# Guescon Books Rest API

This rest api provides a base to a library/ecommerce, currently supporting baskets, basket items, books, magazines,
authors, genres and companies. I wrote this api using Django and Django Rest Framework, with MySQL for default database and
Redis for cache 

# URLS
To use this api, know that Basket's are linked to current users, only admins can create, destroy and update books, magazines,
authors, companies and genres. Promotions can be supported, but a little bit of code would be incremented to improve it. 
Are so many urls for manage the data and list books and magazines, also to login and register. A special view "buy-item" is
used for the current user buy a book or magazine, adding it to its basket 
