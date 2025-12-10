from sqlalchemy import create_engine, Column,String,Float,Datetime,JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from datetime import datetime
from config.settings import settings
from utils.logger import logger

#SQLAlchemy setup
Base=declarative_base()
engine=create_engine(settings.postgres_database_url)
SessionLocal=sessionmaker(bind=engine)

#MongoDB setup
mongo_client=MongoClient(settings.MONGODB_URL)
mongodb=mongo_client[settings.MONGODB_NAME]


class DatabaseTools:
    """Database Operations"""
    @staticmethod
    def save_property(property_data:dict):
        """ Save property listing to Database"""
        try:
            properties_collection=mongodb["properties"]
            result=properties_collection.insert_one(
                {
                    **property_data,
                    "created_at":datetime.now(),
                    "updated_at":datetime.now()
                }
            )
            logger.info(f"Property saved: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error in saving property: {e}")
            raise


    @staticmethod
    def get_property(property_id:str):
        """ Get Property by Id """
        try:
            properties_collection=mongodb["properties"]
            property_doc=properties_collection.find_one({"property_id":property_id})
            return property_doc
        except Exception as e:
            logger.error(f"Error geeting property : {e}")
            return None


    @staticmethod
    def search_properties(query:dict,limit:int=50):
        """ Search properties with quuery"""
        try:
            properties_collection=mongodb["properties"]
            results=list(properties_collection.find(query).limit(limit))
            return results
        except Exception as e:
            logger.error(f"Error searching properties:{e}")
            return []
    

    @staticmethod
    def save_price_estimate(estimate_data:dict):
        """Save price estimate to database"""
        try:
            estimate_collection=mongodb["price_estimation"]
            result=estimate_collection.insert_one({
                **estimate_data,
                "created_at":datetime.now()
            })
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving price estimate : {e}")
            raise

    
    @staticmethod
    def save_chat_history(session_id:str,message:dict):
        """Save chat message to database"""
        try:
            chats_collections=mongodb["chats_details"]
            chats_collections.insert_one({
                "session_id":session_id,
                **message,
                "record_time": datetime.now()
            })
        except Exception as e:
            logger.error(f"Error saving chat: {e}")
            raise

    
    def get_chat_history(session_id:str,limit:int=50):
        """ Get Chat History """
        try:
            chats_collections=mongodb["chats_details"]
            history=list(chats_collections.find(
                {"session_id":session_id}
                ).sort("record_time",-1).limit(limit))
            return list(reversed(history))
        except Exception as e:
            logger.error(f"Error getting chat history: {e}")
            return[]