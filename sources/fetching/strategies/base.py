# sources/fetching/strategies/base.py
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from datetime import datetime
from ..types import FetchResult, ContentQuality
from ..strategy import FetchStrategy
from ..config import FetcherConfig
import logging

logger = logging.getLogger(__name__)

class ContentFetchStrategy(ABC):
    """Base class for content fetch strategies"""
    
    strategy_type: FetchStrategy = None  # Set by subclasses
    
    @abstractmethod
    async def fetch(self, url: str, config: FetcherConfig) -> FetchResult:
        """Fetch content using this strategy"""
        pass
    
    @abstractmethod
    async def cleanup(self):
        """Cleanup strategy resources"""
        pass
    
    def create_result(
        self,
        content: Optional[str],
        quality: ContentQuality,
        error: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> FetchResult:
        """Create a standardized fetch result"""
        return FetchResult(
            content=content,
            quality=quality,
            strategy=self.strategy_type,
            error=error,
            metadata=metadata or {}
        )

    
    async def validate_content(
        self,
        content: Optional[str],
        config: FetcherConfig
    ) -> ContentQuality:
        """Validate fetched content"""
        if not content:
            return ContentQuality.EMPTY
        
        return config.validation.validate(content)