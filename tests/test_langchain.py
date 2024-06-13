from config.langchain_helper import (
    generate_brand_name,
    generate_brand_color,
    generate_brand_messaging,
    generate_business_strategy,
)


class TestLLMService:
    def test_get_brand_name(self):
        response = generate_brand_name(niche="tech", industry="software")
        assert response is not None
        assert response != ""
        assert isinstance(response, list)

    def test_get_brand_color(self):
        response = generate_brand_color(niche="tech", industry="software")
        assert response is not None
        assert response != ""
        assert isinstance(response, list)

    def test_generate_brand_messaging(self):
        response = generate_brand_messaging(industry="software", niche="tech")
        assert response is not None
        assert response != ""
        assert isinstance(response, list)

    def test_generate_business_strategy(self):
        response = generate_business_strategy(
            industry="software", niche="tech", country="USA"
        )
        assert response is not None
        assert response != ""
        assert isinstance(response, list)

    # def test_generate_logo(self):
    #     response = generate_logo(industry="software", niche="tech")
    #     assert response is not None
    #     assert response != ""

    # def test_generate_pics(self):
    #     response = generate_pics(industry="software")
    #     assert response is not None
    #     assert response != ""

    # def test_generate_pattern(self):
    #     response = generate_pattern(industry="software")
    #     assert response is not None
    #     assert response != ""
