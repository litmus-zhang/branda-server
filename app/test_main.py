from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)
def test_status():
    res = client.get('/status')
    assert res.status_code == 200
    assert res.json()['message'] == "All system operational"
    assert res.json()['status'] == "OK"
class TestAuth():
    def test_register_with_google(self):
        pass

    def test_login_with_google(self):
        pass

    def test_logout(self):
        pass


class TestBrand():
    def test_get_brand_names(self):
        res = client.get('/brand_name', params={"niche": "Finance", "industry":"Fintech"})
        assert res.status_code == 200
        assert res.json()['data'] != None
        assert res.json()['message'] == "Brand names fetched successfully"

    def test_post_brand_name(self):
        res = client.post('/brand_name', json={"name": "Jason Statham"})
        assert res.status_code == 201
        assert res.json()['message'] == "Brand name saved successfully"

    def test_get_brand_logo(self):
        pass

    def test_post_brand_logo(self):
        pass

    def test_get_brand_font(self):
        pass

    def test_post_brand_font(self):
        pass

    def test_get_brand_color(self):
        pass

    def test_post_brand_color(self):
        pass

    def test_get_brand_strategy(self):
        pass

    def test_post_brand_strategy(self):
        pass

    def test_get_brand_messaging(self):
        pass

    def test_post_brand_messaging(self):
        pass

    def test_get_brand_photography(self):
        pass

    def test_post_brand_photography(self):
        pass

    def test_get_brand_illustration(self):
        pass

    def test_post_brand_illustration(self):
        pass

    def test_get_brand_presentation(self):
        pass

    def test_post_brand_presentation(self):
        pass


class UserBrand():
    def test_get_all_user_brands():
        pass

    def test_get_a_user_brands():
        pass

    def test_update_a_user_brands():
        pass

    def test_delete_a_user_brands():
        pass