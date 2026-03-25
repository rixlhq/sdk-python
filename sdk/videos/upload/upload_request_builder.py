from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .complete.complete_request_builder import CompleteRequestBuilder
    from .init.init_request_builder import InitRequestBuilder

class UploadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /videos/upload
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UploadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/videos/upload", path_parameters)
    
    @property
    def complete(self) -> CompleteRequestBuilder:
        """
        The complete property
        """
        from .complete.complete_request_builder import CompleteRequestBuilder

        return CompleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def init(self) -> InitRequestBuilder:
        """
        The init property
        """
        from .init.init_request_builder import InitRequestBuilder

        return InitRequestBuilder(self.request_adapter, self.path_parameters)
    

