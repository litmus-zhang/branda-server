from fastapi.testclient import TestClient
from app.main import app
import pytest


client = TestClient(app, base_url="http://localhost:8000/api/v1")


@pytest.fixture(autouse=True, scope="module")
def clear_test_data():
    yield
    # clear test data


def test_status():
    res = client.get("/status")
    assert res.status_code == 200
    assert res.json()["message"] == "All system operational"
    assert res.json()["status"] == "OK"


# @pytest.fixture(scope="module")
def user_signup(email="test@gmail.com", password="test123"):
    response = client.post("/signup", json={"email": email, "password": password})
    return response


# @pytest.fixture(scope="module")
def user_login(email="test@gmail.com", password="test123"):
    response = client.post("/login", json={"email": email, "password": password})
    return response


class TestAuth:
    def test_signup(self):
        res = user_signup()
        assert res.status_code == 201
        assert res.json()["message"] == "User registration successful"
        duplicate_res = user_signup()
        assert duplicate_res.status_code == 409
        assert duplicate_res.json()["detail"]["message"] == "User already exists"

    def test_login(self):
        res = user_login()
        assert res.status_code == 200
        assert res.json()["message"] == "User login successful"

    # def test_login_with_google(self):
    #     pass

    # def test_logout(self):
    #     pass


class TestBrand:
    def test_create_brand_names(self):
        userId = ""
        res = client.post(
            f"/{userId}/brands/brand_name",
            json={"niche": "Finance", "industry": "Fintech"},
        )
        assert res.status_code == 200
        assert res.json()["data"] != None
        assert res.json()["message"] == "Brand names fetched successfully"


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
