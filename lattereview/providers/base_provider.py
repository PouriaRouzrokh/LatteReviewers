from typing import Optional, Any
import pydantic

class BaseProvider(pydantic.BaseModel):
    provider: str = "DefaultProvider"  
    client: Optional[Any] = None  
    api_key: Optional[str] = None 
    model: str = "default-model" 
    output_json_format: Optional[Any] = None  
    last_response: Optional[Any] = None 

    class Config:
        arbitrary_types_allowed = True

    def create_client(self) -> Any:
        raise NotImplementedError("Subclasses must implement `create_client`")
    
    async def get_response(self, messages: str, message_list: list = None, system_message: str = None) -> Any:
        raise NotImplementedError("Subclasses must implement `get_response`")
    
    async def get_json_response(self, messages: str, message_list: list = None, system_message: str = None) -> Any:
        raise NotImplementedError("Subclasses must implement `get_json_response`")
    
    def _prepare_message_list(self, message: str, message_list: list = None, system_message: str = None) -> list:
        raise NotImplementedError("Subclasses must implement `_prepare_message_list`")
    
    async def _fetch_response(self, message_list: list, kwargs: dict = dict()) -> Any:
        raise NotImplementedError("Subclasses must implement `_fetch_response`")
    
    async def _fetch_json_response(self, message_list: list, kwargs: dict = dict()) -> Any:
        raise NotImplementedError("Subclasses must implement `_fetch_json_response`")
    
    def _extract_content(self, response: Any) -> Any:
        raise NotImplementedError("Subclasses must implement `_extract_content`")