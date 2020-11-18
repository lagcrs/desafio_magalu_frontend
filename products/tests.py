from django.test import TestCase, Client
from django.test import client
from .models import Products

# ! TODO: should not create a product without a user_id


class ProductsModelTests(TestCase):

    client = Client()

    def test_status_200_on_list_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    # ? TODO: Magalu requirement
    def test_product_has_title_attribute(self):
        product = Products(title="Fake Product")
        self.assertEqual(product.title, "Fake Product")

    # ? TODO: Magalu requirement
    def test_product_has_unit_price_attribute(self):
        product = Products(unit_price=99.99)
        self.assertEqual(product.unit_price, 99.99)

    # ? TODO: Magalu requirement
    def test_product_has_product_code_attribute(self):
        product = Products(product_code="12732ehwy7qe67t3ug1")
        self.assertEqual(product.product_code, "12732ehwy7qe67t3ug1")

    # ? TODO: Magalu requirement
    def test_product_has_quantity_attribute(self):
        product = Products(quantity=10)
        self.assertEqual(product.quantity, 10)
    

    # ? TODO: Magalu requirement
    def test_should_not_create_product_without_title(self):
        data = {"quantity": 0, "unit_price": 0, "product_code": ""}
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, 400)

    # ? TODO: Magalu requirement
    def test_should_not_create_product_without_product_code(self):
        data = {"quantity": 0, "unit_price": 0, "title": ""}
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, 400)

    # ? TODO: Magalu requirement
    def test_should_not_create_product_without_quantity(self):
        data = {"product_code": 0, "unit_price": 0, "title": ""}
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, 400)

    # ? TODO: Magalu requirement
    def test_should_not_create_product_without_unit_price(self):
        data = {"product_code": 0, "quantity": 0, "title": ""}
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, 400)

    # ? TODO: Magalu requirement
    def test_should_be_able_to_create_a_product(self):
        data = {
            "product_code": "767326",
            "quantity": 10,
            "title": "Fake product",
            "unit_price": 99.99,
            
        }
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], "Fake product")

    # ? TODO: Magalu requirement
    def test_should_not_be_able_to_list_deleted_products(self):
        data = {
            "product_code": "767326",
            "quantity": 10,
            "title": "Fake product",
            "unit_price": 99.99,
            "status": "deleted"

        }
        self.client.post('/products/', data)
        
        response = self.client.get('/products/')
        self.assertEqual(response.data, [])

    # ? TODO: Magalu requirement
    def test_should_not_be_able_to_show_deleted_product(self):
        data = {
            "product_code": "767326",
            "quantity": 10,
            "title": "Fake product",
            "unit_price": 99.99,
            "status": "deleted"
        }
        response = self.client.post('/products/', data)
        product_id = response.data["id"]
        
        response = self.client.get('/products/{}/'.format(product_id))
        self.assertEqual(response.status_code, 404)                 
