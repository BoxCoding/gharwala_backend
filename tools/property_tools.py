from typing import List,Dict,Any
from config.settings import settings
from utils.logger import logger
import requests


class PropertyTools:
    """Tools for Property Operations """

    @staticmethod
    def search_property_by_location(
        locality:str,
        property_budget_min:float=None,
        property_budget_max:float=None,
        property_type:str="residential",
        limit:int=50
    ) -> List[Dict]:
        """ Search properties by location and filters
        Simulated -in """
        logger.info(f"Searching properties in {locality} location")
        query={
            "locality":locality,
            "type":property_type
        }
        if property_budget_min:
            query["property_price"]={"$ate": property_budget_min}
        if property_budget_max:
            if "property_price" in query:
                query["property_price"]["$lte"]=property_budget_max
            else:
                query["property_price"]={"$lte": property_budget_max}
        return []


    def rank_properties(
        properties:List[Dict],
        user_preference:Dict,
        user_interaction_history:List[Dict]=None
    )->List[Dict]:
        """ Ranking properties using ML models"""
        logger.info(f"Ranking {len(properties)} properties")
        ranked_properties = []
        for prop in properties:



    def _calculate_match_score(
        property_data:Dict,
        user_preference:Dict,
        user_interaction_history:List[Dict]
    )
        """ Calculate Property match score"""
        score=0.0
        if property_data.get("locality") in user_preference.get("preferred_locations",[]):
            score+=0.4
        #Budget Match(30%)
        price=property_data.get("property_price",0)
        property_budget_min=user_preference.get("property_budget_min",100000)
        property_budget_max=user_preference.get("property_budget_max",float('inf'))

        if property_budget_min<=price<=property_budget_max:
            score+=0.3
        #Type match(20%)
        if property_data.get("property_type")==user_preference.get("property_type"):
            score+=0.20
        #Amenities match(10%)
        property_amenities=set(property_data.get("amenities",[]))
        preferred_amenities=set(user_preference.get("amenities",[]))
