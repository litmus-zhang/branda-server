from fastapi.testclient import TestClient
from app.main import app
import pytest
from config.firebase import clear_firestore_data, delete_all_auth_users


client = TestClient(app, base_url="http://localhost:8000/api/v1")


@pytest.fixture(autouse=True)
def clear_test_data():
    yield
    clear_firestore_data()
    delete_all_auth_users()


def test_status():
    res = client.get("/status")
    assert res.status_code == 200
    assert res.json()["message"] == "All system operational"
    assert res.json()["status"] == "OK"


class TestAuth:
    def test_signup(self):
        res = client.post(
            "/signup", json={"email": "test@gmail.com", "password": "test123"}
        )
        assert res.status_code == 201
        assert res.json()["message"] == "User registration successful"
        duplicate_res = client.post(
            "/signup", json={"email": "test@gmail.com", "password": "test123"}
        )
        assert duplicate_res.status_code == 409
        assert duplicate_res.json()["message"] == "User already exists"

    def test_login(self):
        res = client.post(
            "/signup", json={"email": "test@gmail.com", "password": "test123"}
        )
    # def test_login_with_google(self):
    #     pass

    # def test_logout(self):
    #     pass


# class TestBrand():
#     def test_get_brand_names(self):
#         res = client.post('/brand_name', params={"niche": "Finance", "industry":"Fintech"})
#         assert res.status_code == 200
#         assert res.json()['data'] != None
#         assert res.json()['message'] == "Brand names fetched successfully"

#     def test_post_brand_name(self):
#         res = client.post('/brand_name', json={"name": "Jason Statham"})
#         assert res.status_code == 201
#         assert res.json()['message'] == "Brand name saved successfully"

#     def test_get_brand_logo(self):
#         pass

#     def test_post_brand_logo(self):
#         pass

#     def test_get_brand_font(self):
#         pass

#     def test_post_brand_font(self):
#         pass

#     def test_get_brand_color(self):
#         pass

#     def test_post_brand_color(self):
#         pass

#     def test_get_brand_strategy(self):
#         pass

#     def test_post_brand_strategy(self):
#         pass

#     def test_get_brand_messaging(self):
#         pass

#     def test_post_brand_messaging(self):
#         pass

#     def test_get_brand_photography(self):
#         pass

#     def test_post_brand_photography(self):
#         pass

#     def test_get_brand_illustration(self):
#         pass

#     def test_post_brand_illustration(self):
#         pass

#     def test_get_brand_presentation(self):
#         pass

#     def test_post_brand_presentation(self):
#         pass


# class UserBrand():
# def test_get_all_user_brands(self):
#     pass

# def test_get_a_user_brands(self):
#     pass

# def test_update_a_user_brands(self):
#     pass

# def test_delete_a_user_brands(self):
#     pass
