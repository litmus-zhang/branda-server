from fastapi.testclient import TestClient
import requests
from .main import app

projectId = "new-branda"
def clear_firestore(PROJECT_ID: str = projectId):
    requests.delete(f'http://localhost:8080/emulator/v1/projects/{PROJECT_ID}/databases/(default)/documents', timeout=5000)

def clear_auth(PROJECT_ID: str = projectId):
    requests.delete(f'http://localhost:9099/emulator/v1/projects/{PROJECT_ID}/accounts', timeout=5000)
client = TestClient(app, base_url="http://localhost:8000/api/v1")
def test_status():
    res = client.get('/status')
    assert res.status_code == 200
    assert res.json()['message'] == "All system operational"
    assert res.json()['status'] == "OK"
class TestAuth():
    def test_signup(self):
        res = client.post('/signup')
        assert res.status_code == 201
        assert res.json()['message'] == "User registration successful"

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