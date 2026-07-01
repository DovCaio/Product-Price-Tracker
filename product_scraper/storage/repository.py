from .database import Session
from .models import Product, PriceHistory


class ProductRepository:


    def save(self, item):

        session = Session()

        try:

            product = (
                session
                .query(Product)
                .filter_by(
                    url=item["url"]
                )
                .first()
            )


            if product is None:

                product = Product(

                    name=item["name"],

                    url=item["url"],

                    store=item["store"]

                )

                session.add(product)

                session.commit()

                session.refresh(product)



            price_history = PriceHistory(

                product_id=product.id,

                price=float(
                    item["price"]
                )

            )


            session.add(price_history)


            session.commit()


        except Exception as error:

            session.rollback()

            raise error


        finally:

            session.close()