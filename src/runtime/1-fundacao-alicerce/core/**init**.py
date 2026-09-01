"""
MESH - Fundação Alicerce - Core Package
Este pacote contém o núcleo operacional do MESH.

Regra combinada:
- Constituição (constitution/) = EVOLUTIVA e aperfeiçoável
- Histórico (event_store.py) = IMUTÁVEL, fiel e hash-chained

Componentes:
- EventStore: memória imutável de eventos
- Executor: executa com zero-trust (não pode validar própria proposta)
"""

from ..constitution.constitution import Constitution
from .event_store import EventStore
from .executor import Executor

__all__ = ["Constitution", "EventStore", "Executor"]
