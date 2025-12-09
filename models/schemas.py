from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class PropertyRequirements(BaseModel):
    property_type: str = Field(..., description="The type of property required")
    property_subtype: Optional[str] = Field(None, description="The subtype of the property required")
    property_location: str = Field(..., description="The location of the property required")
    property_area: float = Field(..., description="The area of the property required")
    property_bedrooms: int = Field(..., description="The number of bedrooms required")
    property_bathrooms: int = Field(..., description="The number of bathrooms required")
    property_garage: Optional[bool] = Field(False, description="Whether the property has a garage")
    property_amenities: Optional[List[str]] = Field(..., description="The amenities of the property required")
    property_budget_min:Optional[float] = Field(None, description="The minimum budget for the property")
    property_budget_max:Optional[float] = Field(None, description="The maximum budget for the property")
    investment_intent:str = Field(..., description="The investment intent for the property")
    timeline:str="flexible"
    confidence:float=0.90

class propertyListing(BaseModel):
    ""Property listing schema""
    property_id:str = Field(..., description="The ID of the property")
    property_title:str = Field(..., description="The title of the property")
    property_description:str = Field(..., description="The description of the property")
    property_type:str = Field(..., description="The type of the property")
    property_subtype:Optional[str] = Field(None, description="The subtype of the property")
    property_address:str = Field(..., description="The address of the property")
    property_location:str = Field(..., description="The location of the property")
    property_locality:str = Field(..., description="The locality of the property")
    property_latitude:Optional[float] = Field(None, description="The latitude of the property")
    property_longitude:Optional[float] = Field(None, description="The longitude of the property")
    property_price:float = Field(..., description="The price of the property")
    property_area:float = Field(..., description="The area of the property")
    property_bedrooms:int = Field(..., description="The number of bedrooms in the property")
    property_bathrooms:int = Field(..., description="The number of bathrooms in the property")
    property_garage:Optional[bool] = Field(False, description="Whether the property has a garage")
    property_amenities:Optional[List[str]] = Field(..., description="The amenities of the property")
    property_images:Optional[List[str]] = Field(..., description="The images of the property")
    property_video:Optional[str] = Field(None, description="The video of the property")
    property_status:str = Field(..., description="The status of the property")
    created_at:datetime = Field(default_factory=datetime.now, description="The date and time the property was created")
    updated_at:datetime = Field(default_factory=datetime.now, description="The date and time the property was updated")
    is_active:bool = Field(True, description="Whether the property is active")
    is_featured:bool = Field(False, description="Whether the property is featured")
    is_verified:bool = Field(False, description="Whether the property is verified")
    is_approved:bool = Field(False, description="Whether the property is approved")
    is_rejected:bool = Field(False, description="Whether the property is rejected")
    is_deleted:bool = Field(False, description="Whether the property is deleted")
    is_archived:bool = Field(False, description="Whether the property is archived")
    is_sold:bool = Field(False, description="Whether the property is sold")
    is_rented:bool = Field(False, description="Whether the property is rented")
    is_leased:bool = Field(False, description="Whether the property is leased")
    is_rented:bool = Field(False, description="Whether the property is rented")

class PriceEstimation(BaseModel):
    ""Price estimation schema""
    property_id:str = Field(..., description="The ID of the property")
    property_location:str = Field(..., description="The location of the property")
    property_type:str = Field(..., description="The type of the property")
    property_subtype:Optional[str] = Field(None, description="The subtype of the property")
    property_area:float = Field(..., description="The area of the property")
    property_configuration:str = Field(..., description="The configuration of the property")
    property_estimated_price:float = Field(..., description="The estimated price of the property")
    lower_bound_price:float = Field(..., description="The lower bound price of the property")
    upper_bound_price:float = Field(..., description="The upper bound price of the property")
    confidence:float = Field(0.90, description="The confidence of the price estimation")
    price_drivers:Dict[str, float] = Field(..., description="The price drivers of the property")
    rental_yield:Optional[float] = Field(None, description="The rental yield of the property")
    created_at:datetime = Field(default_factory=datetime.now, description="The date and time the price estimation was created")
    updated_at:datetime = Field(default_factory=datetime.now, description="The date and time the price estimation was updated")
   
class NewsItem(BaseModel):
    ""News/market intelligence schema""
    news_id:str = Field(default_factory=lambda: str(uuid.uuid4()), description="The ID of the news item")
    news_title:str = Field(..., description="The title of the news item")
    news_summary:str = Field(..., description="The summary of the news item")
    news_source:str = Field(..., description="The source of the news item")
    news_url:str = Field(..., description="The URL of the news item")
    locality:str = Field(..., description="The locality of the news item")
    impact_type:str = Field(..., description="The impact type of the news item")
    published_at:datetime = Field(default_factory=datetime.now, description="The date and time the news item was published")
    relevance_score:float = Field(0.90, description="The relevance score of the news item")

class ChatMessage(BaseModel):
    ""Chat message schema""
    session_id:str = Field(default_factory=lambda: str(uuid.uuid4()), description="The ID of the chat session")
    user_id:str = Field(..., description="The ID of the user")
    message:str = Field(..., description="The message of the chat")
    agent_type:Optional[str] = Field(None, description="The type of the agent")
    metadata:Dict[str, Any] = Field(..., description="The metadata of the chat message")
    created_at:datetime = Field(default_factory=datetime.now, description="The date and time the chat message was created")

class ChatResponse(BaseModel):
    ""Chat response schema""
    session_id:str = Field(default_factory=lambda: str(uuid.uuid4()), description="The ID of the chat session")
    response:str = Field(..., description="The response of the chat")
    agent_executed:Optional[str] = Field(None, description="The agent that executed the chat")
    intent:Optional[str] = Field(None, description="The intent of the chat")
    confidence:float
    recommendation:Optional[List[propertyListing]]=None
    price_estimation:Optional[PriceEstimation]=None
    timestamp:datetime=Field(default_factory=datetime.now())