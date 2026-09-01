"""
resilience/__init__.py - Módulo de resiliência (reconstruído)
Compatível com ecossistema 3-execucao + guards + governance
"""

import time
import logging
from functools import wraps
from typing import Callable, Any, Optional

logger = logging.getLogger("resilience")

class ResilienceManager:
    """Gerenciador de resiliência: retry, fallback, circuit breaker simples"""
    def __init__(self, max_retries: int = 3, backoff: float = 0.5):
        self.max_retries = max_retries
        self.backoff = backoff
        self.failures = {}

    def retry(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, self.max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    logger.warning(f"[Resilience] Tentativa {attempt}/{self.max_retries} falhou em {func.__name__}: {e}")
                    if attempt < self.max_retries:
                        time.sleep(self.backoff * attempt)
            logger.error(f"[Resilience] {func.__name__} falhou após {self.max_retries} tentativas")
            raise last_exc
        return wrapper

    def circuit_breaker(self, key: str, threshold: int = 5):
        """Simples contador de falhas"""
        fails = self.failures.get(key, 0)
        if fails >= threshold:
            logger.error(f"[CircuitBreaker] Circuito aberto para {key}")
            return False
        return True

def with_resilience(max_retries=3, backoff=0.5):
    """Decorator rápido: @with_resilience()"""
    manager = ResilienceManager(max_retries=max_retries, backoff=backoff)
    return manager.retry

__all__ = ["ResilienceManager", "with_resilience"]
