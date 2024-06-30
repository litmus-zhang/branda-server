import os
import requests
import random
from config.database import get_db
from models import models
from models.schemas import Base, Strategy, BaseBody
import config.langchain_helper as lch
from fastapi.responses import JSONResponse
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


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

    def store_brand_name(
        self, base: BaseBody, userId: str | int, db: Session = Depends(get_db)
    ):
        try:
            new_brand = models.Brand(**base.model_dump(), owner_id=int(userId))
            db.add(new_brand)
            db.commit()
            db.refresh(new_brand)

            return JSONResponse(
                content={
                    "message": "Brand name saved successfully",
                    "data": {"brand Id": new_brand.id},
                },
                status_code=201,
            )

        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_font(self, base: BaseBody, brandId: str, db: Session = Depends(get_db)):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"font": base.font}
            )
            db.commit()

            return JSONResponse(
                content={
                    "message": "Brand font saved successfully",
                },
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_color_pallete(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"color": base.color}
            )
            db.commit()

            return JSONResponse(
                content={"message": "Brand color saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_messaging(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"messaging": base.messaging}
            )
            db.commit()
            return JSONResponse(
                content={"message": "Brand messaging saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_strategy(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"strategy": base.strategy}
            )
            db.commit()
            return JSONResponse(
                content={"message": "Brand strategy saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_logo(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"logo": base.logo}
            )
            db.commit()

            return JSONResponse(
                content={"message": "Brand logo saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_photography(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"photography": base.photography}
            )
            db.commit()
            return JSONResponse(
                content={"message": "Brand photography saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_illustration(
        self, base: BaseBody, brandId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"illustration": base.illustration}
            )
            db.commit()

            return JSONResponse(
                content={"message": "Brand illustration saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def store_brand_presentation(
        self, base: BaseBody, brandId: str, userId: str, db: Session = Depends(get_db)
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {"presentation": base.presentation}
            )
            db.commit()
            return JSONResponse(
                content={"message": "Brand presentation saved successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc

    def update_brand_details(
        self, base: BaseBody, brandId: str, userId: str, db: Session
    ):
        try:
            db.query(models.Brand).filter(models.Brand.id == brandId).update(
                {
                    "name": base.name,
                    "font": base.font,
                    "strategy": base.strategy,
                    "color": base.color,
                    "logo": base.logo,
                    "messaging": base.messaging,
                    "photography": base.photography,
                    "illustration": base.illustration,
                    "presentation": base.presentation,
                }
            )
            db.commit()
            return JSONResponse(
                content={"message": "Brand details updated successfully"},
                status_code=201,
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc
