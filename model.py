from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User object"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """Display when printing a User object"""

        return "<User: {} email: {}>".format(self.user_id, self.email)



class Product(db.Model):
    """Product object"""

    __tablename__ = "products"

    asin = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    author = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False) # link to image

    def __repr__(self):
        """Display when printing a Product object"""

        return "<Product: {} name: {}>".format(self.asin, self.title)


class Review(db.Model):
    """Review object"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    reviewer_id = db.Column(db.Text, nullable=False)
    reviewer_name = db.Column(db.Text)
    review = db.Column(db.Text, nullable=False)
    asin = db.Column(db.Text, db.ForeignKey('products.asin'))
    helpful_total = db.Column(db.Integer)
    helpful_fraction = db.Column(db.Integer)
    rating = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text)
    # time = db.Column(db.DateTime)

    def __repr__(self):
        """Display when printing a Review object"""

        return "<Review: {} product: {}>".format(self.review_id, self.summary)


# class RatingDistribution(db.Model)
#     """Object to hold how many 1-5 star ratings a product receieved"""

#     __tablename__ = ""



class FavoriteProduct(db.Model):
    """User favorite product object"""

    __tablename__ = "favorite_products"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    asin = db.Column(db.Text, db.ForeignKey('products.asin'))

    def __repr__(self):
        """Display when printing a FavoriteProduct object"""

        return "<FavoriteProduct: {} product: {}>".format(self.review_id, self.asin)


class FavoriteReview(db.Model):
    """User favorite review object"""

    __tablename__ = "favorite_reviews"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.review_id'))

    def __repr__(self):
        """Display when printing a FavoriteReview object"""

        return "<FavoriteReview: {} >".format(self.review_id)



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///reviewgenius'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # Work with database directly if run interactively

    from server import app
    connect_to_db(app)
    print "Connected to DB."
