import os
import requests
import random
from models.schemas import Base, Strategy
import config.langchain_helper as lch


class BrandService:

    def get_brand_name(self, base: Base):
        response = lch.generate_brand_name(niche=base.niche, industry=base.industry)
        return response

    def get_font(self):
        API_KEY = os.getenv("GOOGLE_FONTS_API_KEY")
        url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY
        response = requests.get(url, timeout=5)

        fonts = response.json()
        list_of_fonts = fonts["items"]

        random_fonts = random.sample(list_of_fonts, 3)

        return random_fonts

    def get_color_pallete(self, base: Base):
        response = lch.generate_brand_color(niche=base.niche, industry=base.industry)
        return response

    def get_brand_messaging(self, base: Base):
        response = lch.generate_brand_messaging(
            industry=base.industry, niche=base.niche
        )
        return response

    def get_brand_strategy(self, brand_strategy: Strategy):
        industry = brand_strategy.industry
        niche = brand_strategy.niche
        country = brand_strategy.country
        response = lch.generate_business_strategy(
            industry=industry, niche=niche, country=country
        )
        return response

    def get_logo(self, base: Base):
        response = lch.generate_logo(industry=base.industry, niche=base.niche)
        return response

    def get_photography(self, base: Base):
        response = lch.generate_pics(industry=base.industry)
        return response

    def get_illustration(self, base: Base):
        response = lch.generate_pattern(industry=base.industry)
        return response

    def store_brand_name(self, base: Base):
        pass

    def store_font(self, base: Base):
        pass

    def store_color_pallete(self, base: Base):
        pass

    def store_brand_messaging(self, base: Base):
        pass

    def store_brand_strategy(self, brand_strategy: Strategy):
        pass

    def store_brand_logo(self, base: Base):
        pass

    def store_brand_photography(self, base: Base):
        pass

    def store_brand_illustration(self, base: Base):
        pass

    def store_brand_presentation(self, base: Base):
        pass
